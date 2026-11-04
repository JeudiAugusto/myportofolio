import uuid

from django.contrib.auth.models import Group, User
from django.urls import reverse
from django.test import override_settings
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from main.models import Experience, Project


@override_settings(PASSWORD_HASHERS=["django.contrib.auth.hashers.MD5PasswordHasher"])
class ProjectAPITest(APITestCase):
    def setUp(self):
        Project.objects.all().delete()
        self.owner = User.objects.create_superuser(
            username="owner", password="test-password", email="owner@example.com",
        )
        self.visitor = User.objects.create_user(username="visitor", password="test-password")
        self.project = Project.objects.create(
            title="Portfolio", description="My website", technologies="Django", year=2026, role="Developer", focus="Web",
        )
        self.list_url = reverse("api:project-list")
        self.detail_url = reverse("api:project-detail", args=[self.project.id])
        self.star_url = reverse("api:project-star", args=[self.project.id])
        self.payload = {
            "title": "New project", "description": "A useful app", "technologies": "Python", "year": 2026, "role": "Developer", "focus": "Web",
            "repository_url": "https://example.com/",
        }

    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], str(self.project.id))
        self.assertFalse(response.data[0]["is_starred"])
        self.assertNotIn("fields", response.data[0])
        self.assertEqual(self.client.get(self.detail_url).status_code, status.HTTP_200_OK)

    def test_search_and_empty_results(self):
        response = self.client.get(self.list_url, {"title": "PORT"})
        self.assertEqual(len(response.data), 1)
        response = self.client.get(self.list_url, {"title": "not-found"})
        self.assertEqual(response.data, [])

    def test_missing_project(self):
        url = reverse("api:project-detail", args=[uuid.uuid4()])
        self.assertEqual(self.client.get(url).status_code, status.HTTP_404_NOT_FOUND)

    def test_guest_and_visitor_cannot_write(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)
            self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
            self.assertEqual(self.client.patch(self.detail_url, {"title": "Changed"}, format="json").status_code, 403)
            self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
        self.assertEqual(Project.objects.count(), 1)
        self.project.refresh_from_db()
        self.assertEqual(self.project.title, "Portfolio")

    def test_owner_can_create(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Project.objects.filter(pk=response.data["id"]).exists())

    def test_validation(self):
        self.client.force_authenticate(user=self.owner)
        for changes, field in [
            ({"title": "   "}, "title"),
            ({"title": '<img src="x" onerror="alert(1)">'}, "title"),
            ({"repository_url": "javascript:alert(1)"}, "repository_url"),
        ]:
            response = self.client.post(self.list_url, {**self.payload, **changes}, format="json")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn(field, response.data)
        self.assertEqual(Project.objects.count(), 1)

    def test_patch_put_and_delete(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.patch(self.detail_url, {"title": "Changed"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.project.refresh_from_db()
        self.assertEqual(self.project.description, "My website")
        response = self.client.put(self.detail_url, {"title": "Incomplete"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.put(self.detail_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b"")
        self.assertFalse(Project.objects.filter(pk=self.project.id).exists())

    def test_star_requires_login_and_toggles(self):
        self.assertEqual(self.client.post(self.star_url).status_code, status.HTTP_403_FORBIDDEN)
        self.client.force_authenticate(user=self.visitor)
        response = self.client.post(self.star_url)
        self.assertTrue(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 1)
        response = self.client.post(self.star_url)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 0)

    def test_computed_fields_are_read_only(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, {
            **self.payload, "star_count": 99, "is_starred": True,
            "starred_by_names": "forged", "starred_by": [self.visitor.id],
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])

    def test_staff_and_editor_cannot_manage_tutorial_projects(self):
        self.visitor.is_staff = True
        self.visitor.save()
        self.visitor.groups.add(Group.objects.get_or_create(name="Editor")[0])
        self.client.force_authenticate(user=self.visitor)
        response = self.client.patch(self.detail_url, {"title": "Changed"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_wrong_method(self):
        self.client.force_authenticate(user=self.owner)
        self.assertEqual(self.client.delete(self.list_url).status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_session_write_without_csrf_is_rejected(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username="owner", password="test-password"))
        response = client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Project.objects.count(), 1)

    def test_session_write_with_csrf_succeeds(self):
        client = APIClient(enforce_csrf_checks=True)
        client.login(username="owner", password="test-password")
        # The Browsable API form renders a real CSRF token into the response.
        page = client.get(self.list_url, HTTP_ACCEPT="text/html")
        self.assertEqual(page.status_code, status.HTTP_200_OK)
        token = client.cookies["csrftoken"].value
        response = client.post(
            self.list_url, self.payload, format="json", HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


@override_settings(PASSWORD_HASHERS=["django.contrib.auth.hashers.MD5PasswordHasher"])
class ExperienceAPITest(APITestCase):
    def setUp(self):
        Experience.objects.all().delete()
        self.owner = User.objects.create_superuser("experience-owner", "owner@example.com", "test-password")
        self.editor = User.objects.create_user("editor", password="test-password")
        self.editor.groups.add(Group.objects.get_or_create(name="Editor")[0])
        self.visitor = User.objects.create_user("reader", password="test-password")
        self.experience = Experience.objects.create(title="Organization", description="Activities", category="organization")
        self.list_url = reverse("api:experience-list")
        self.detail_url = reverse("api:experience-detail", args=[self.experience.pk])
        self.star_url = reverse("api:experience-star", args=[self.experience.pk])
        self.payload = {"title": "Research", "description": "Research work", "category": "research", "thumbnail": ""}

    def test_public_read_search_and_missing(self):
        response = self.client.get(self.list_url, {"title": "ORGAN"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["category_display"], "Organization")
        self.assertEqual(response.data[0]["id"], str(self.experience.pk))
        self.assertTrue(response.data[0]["is_ongoing"])
        self.assertEqual(self.client.get(self.list_url, {"title": "absent"}).data, [])
        self.assertEqual(self.client.get(self.detail_url).status_code, 200)
        self.assertEqual(self.client.get(reverse("api:experience-detail", args=[uuid.uuid4()])).status_code, 404)

    def test_guest_and_reader_cannot_manage(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)
            self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
            self.assertEqual(self.client.patch(self.detail_url, self.payload, format="json").status_code, 403)
            self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
        self.assertEqual(Experience.objects.count(), 1)

    def test_editor_can_update_but_not_create_or_delete(self):
        self.client.force_authenticate(user=self.editor)
        self.assertEqual(self.client.patch(self.detail_url, {"title": "Edited"}, format="json").status_code, 200)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Edited")
        self.assertEqual(self.experience.description, "Activities")
        self.assertEqual(self.client.put(self.detail_url, self.payload, format="json").status_code, 200)
        self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
        self.assertEqual(self.client.delete(self.detail_url).status_code, 403)

    def test_owner_create_and_delete(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Experience.objects.filter(pk=response.data["id"]).exists())
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.content, b"")
        self.assertFalse(Experience.objects.filter(pk=self.experience.pk).exists())

    def test_validation_and_read_only_fields(self):
        self.client.force_authenticate(user=self.owner)
        for field, value in [("title", "<b></b>"), ("category", "invalid")]:
            response = self.client.post(self.list_url, {**self.payload, field: value}, format="json")
            self.assertEqual(response.status_code, 400)
            self.assertIn(field, response.data)
        response = self.client.post(self.list_url, {**self.payload, "title": "<b>Clean</b>", "star_count": 100, "starred_by": [self.visitor.pk]}, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], "Clean")
        self.assertEqual(response.data["star_count"], 0)

    def test_star_uses_experience_and_current_user(self):
        self.assertEqual(self.client.post(self.star_url).status_code, 403)
        self.client.force_authenticate(user=self.visitor)
        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["is_starred"])
        self.assertEqual(response.data["starred_by_names"], "reader")
        self.assertNotIn("email", response.data)
        self.assertTrue(self.experience.starred_by.filter(pk=self.visitor.pk).exists())
        self.client.force_authenticate(user=self.editor)
        self.assertFalse(self.client.get(self.detail_url).data["is_starred"])
        self.client.force_authenticate(user=self.visitor)
        self.assertEqual(self.client.post(self.star_url).data["star_count"], 0)
        self.assertEqual(self.client.get(self.star_url).status_code, 405)

    def test_session_csrf_for_member_star(self):
        client = APIClient(enforce_csrf_checks=True)
        client.force_login(self.visitor)
        self.assertEqual(client.post(self.star_url).status_code, 403)
        page = client.get(reverse("main:show_experience"))
        self.assertEqual(page.status_code, 200)
        token = client.cookies["csrftoken"].value
        self.assertEqual(client.post(self.star_url, HTTP_X_CSRFTOKEN=token).status_code, 200)

    def test_safe_methods_do_not_mutate(self):
        self.client.force_authenticate(user=self.owner)
        for url in [self.list_url, self.detail_url]:
            self.assertEqual(self.client.head(url).status_code, 200)
            self.assertEqual(self.client.options(url).status_code, 200)
        self.assertEqual(Experience.objects.count(), 1)
        self.assertEqual(self.experience.starred_by.count(), 0)
