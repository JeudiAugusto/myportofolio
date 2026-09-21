import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Project


class MainTest(TestCase):
    def setUp(self):
        # Bersihkan data dari data migration agar kondisi setiap test terkontrol.
        Experience.objects.all().delete()
        Project.objects.all().delete()

        self.admin_user = User.objects.create_superuser(
            username="testadmin",
            password="testpassword123",
        )

        self.experience = Experience.objects.create(
            title="Staff Kajian dan Aksi Strategis",
            description=(
                "Berperan sebagai Staff Kajian dan Aksi Strategis "
                "BEM Fasilkom UI 2026."
            ),
            category="organization",
        )

        self.project = Project.objects.create(
            title="Cashie",
            description=(
                "Aplikasi web pengelola keuangan yang dikembangkan "
                "menggunakan PHP dan JavaScript."
            ),
            year=2025,
            role="Team Project",
            focus="Finance Web App",
            technologies="PHP, JavaScript, SQL, CRUD, AJAX",
            repository_url="https://github.com/fzdhl/cashie",
        )

    # =========================================================
    # MAIN PAGE
    # =========================================================

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertContains(response, self.project.title)
        self.assertNotContains(response, self.experience.title)
        self.assertContains(
            response,
            f'href="{reverse("main:show_projects")}"',
        )
        self.assertContains(
            response,
            f'href="{reverse("main:show_experience")}"',
        )

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")
        self.assertEqual(response.status_code, 404)

    # =========================================================
    # EXPERIENCE MODEL & PAGE
    # =========================================================

    def test_experience_model(self):
        self.assertEqual(
            str(self.experience),
            "Staff Kajian dan Aksi Strategis",
        )
        self.assertEqual(
            self.experience.category,
            "organization",
        )
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Organization")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(
            response,
            f'href="{reverse("main:show_main")}"',
        )

    def test_empty_experience_page(self):
        Experience.objects.all().delete()

        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "Belum ada pengalaman yang ditambahkan.",
        )

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()

        response = self.client.get(reverse("main:show_experience"))
        self.experience.refresh_from_db()

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")

    def test_experience_page_has_management_links(self):
        response = self.client.get(reverse("main:show_experience"))

        create_url = reverse("main:create_experience")
        update_url = reverse(
            "main:update_experience",
            kwargs={"experience_id": self.experience.id},
        )
        delete_url = reverse(
            "main:delete_experience",
            kwargs={"experience_id": self.experience.id},
        )

        self.assertContains(response, f'href="{create_url}"')
        self.assertContains(response, update_url)
        self.assertContains(response, delete_url)

    # =========================================================
    # CREATE EXPERIENCE
    # =========================================================

    def test_create_experience_page_is_accessible(self):
        response = self.client.get(
            reverse("main:create_experience")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "create_experience.html",
        )
        self.assertTemplateUsed(response, "base.html")
        self.assertContains(response, "Nama Experience")
        self.assertContains(response, "Add Experience")

    def test_create_experience_with_valid_data(self):
        initial_count = Experience.objects.count()

        data = {
            "title": "Tugas 3 Test Experience",
            "description": (
                "Experience untuk menguji fitur create pada Tugas 3 PBP."
            ),
            "category": "volunteer",
            "thumbnail": "",
        }

        response = self.client.post(
            reverse("main:create_experience"),
            data,
            follow=True,
        )

        self.assertRedirects(
            response,
            reverse("main:show_experience"),
        )
        self.assertEqual(
            Experience.objects.count(),
            initial_count + 1,
        )

        created = Experience.objects.get(
            title="Tugas 3 Test Experience"
        )

        self.assertEqual(created.category, "volunteer")
        self.assertEqual(
            created.description,
            "Experience untuk menguji fitur create pada Tugas 3 PBP.",
        )
        self.assertContains(
            response,
            "Experience berhasil ditambahkan!",
        )

    def test_create_experience_with_invalid_data(self):
        initial_count = Experience.objects.count()

        data = {
            "title": "",
            "description": "Experience tanpa judul.",
            "category": "research",
            "thumbnail": "",
        }

        response = self.client.post(
            reverse("main:create_experience"),
            data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "create_experience.html",
        )
        self.assertEqual(
            Experience.objects.count(),
            initial_count,
        )
        self.assertTrue(response.context["form"].errors)
        self.assertIn(
            "title",
            response.context["form"].errors,
        )

    # =========================================================
    # UPDATE EXPERIENCE
    # =========================================================

    def test_update_experience_page_is_accessible(self):
        update_url = reverse(
            "main:update_experience",
            kwargs={"experience_id": self.experience.id},
        )

        response = self.client.get(update_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "update_experience.html",
        )
        self.assertTemplateUsed(response, "base.html")
        self.assertEqual(
            response.context["form"].instance.id,
            self.experience.id,
        )
        self.assertEqual(
            response.context["form"].instance.title,
            self.experience.title,
        )
        self.assertContains(response, "Save Changes")

    def test_update_experience_with_valid_data(self):
        initial_count = Experience.objects.count()
        original_id = self.experience.id

        data = {
            "title": "Updated Experience",
            "description": (
                "Experience yang sudah diperbarui melalui ModelForm."
            ),
            "category": "research",
            "thumbnail": "",
        }

        response = self.client.post(
            reverse(
                "main:update_experience",
                kwargs={"experience_id": self.experience.id},
            ),
            data,
            follow=True,
        )

        self.assertRedirects(
            response,
            reverse("main:show_experience"),
        )
        self.assertEqual(
            Experience.objects.count(),
            initial_count,
        )

        self.experience.refresh_from_db()

        self.assertEqual(self.experience.id, original_id)
        self.assertEqual(
            self.experience.title,
            "Updated Experience",
        )
        self.assertEqual(
            self.experience.category,
            "research",
        )
        self.assertEqual(
            self.experience.description,
            "Experience yang sudah diperbarui melalui ModelForm.",
        )
        self.assertContains(
            response,
            "Experience berhasil diperbarui!",
        )

    def test_update_experience_url_uses_uuid(self):
        update_url = reverse(
            "main:update_experience",
            kwargs={"experience_id": self.experience.id},
        )

        self.assertEqual(
            update_url,
            (
                f"/experience/"
                f"{self.experience.id}/"
                f"update/"
            ),
        )

    # =========================================================
    # EXPERIENCE JSON DATA DELIVERY
    # =========================================================

    def test_experiences_json_endpoint(self):
        response = self.client.get(
            reverse("main:get_experiences_json")
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response["Content-Type"],
            "application/json",
        )

        data = json.loads(response.content)

        self.assertEqual(len(data), 1)
        self.assertEqual(
            data[0]["model"],
            "main.experience",
        )
        self.assertEqual(
            data[0]["pk"],
            str(self.experience.id),
        )
        self.assertEqual(
            data[0]["fields"]["title"],
            self.experience.title,
        )
        self.assertEqual(
            data[0]["fields"]["category"],
            "organization",
        )

    def test_experience_page_uses_deserialized_list(self):
        response = self.client.get(
            reverse("main:show_experience")
        )

        experience_list = response.context["experience_list"]

        self.assertIsInstance(experience_list, list)
        self.assertEqual(len(experience_list), 1)
        self.assertIsInstance(
            experience_list[0],
            Experience,
        )
        self.assertEqual(
            experience_list[0].id,
            self.experience.id,
        )
        self.assertEqual(
            experience_list[0].title,
            self.experience.title,
        )

    # =========================================================
    # DELETE EXPERIENCE
    # =========================================================

    def test_delete_experience_with_post(self):
        delete_url = reverse(
            "main:delete_experience",
            kwargs={"experience_id": self.experience.id},
        )

        response = self.client.post(
            delete_url,
            follow=True,
        )

        self.assertRedirects(
            response,
            reverse("main:show_experience"),
        )
        self.assertFalse(
            Experience.objects.filter(
                id=self.experience.id
            ).exists()
        )
        self.assertContains(
            response,
            "Experience berhasil dihapus!",
        )

    def test_delete_experience_with_get_does_not_delete(self):
        delete_url = reverse(
            "main:delete_experience",
            kwargs={"experience_id": self.experience.id},
        )

        response = self.client.get(delete_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            reverse("main:show_experience"),
        )
        self.assertTrue(
            Experience.objects.filter(
                id=self.experience.id
            ).exists()
        )

    def test_delete_experience_url_uses_uuid(self):
        delete_url = reverse(
            "main:delete_experience",
            kwargs={"experience_id": self.experience.id},
        )

        self.assertEqual(
            delete_url,
            (
                f"/experience/"
                f"{self.experience.id}/"
                f"delete/"
            ),
        )

    def test_delete_nonexistent_experience_returns_404(self):
        nonexistent_uuid = (
            "11111111-1111-1111-1111-111111111111"
        )

        response = self.client.post(
            reverse(
                "main:delete_experience",
                kwargs={
                    "experience_id": nonexistent_uuid,
                },
            )
        )

        self.assertEqual(response.status_code, 404)

    # =========================================================
    # PROJECT MODEL
    # =========================================================

    def test_project_model(self):
        self.assertEqual(str(self.project), "Cashie")
        self.assertEqual(self.project.year, 2025)
        self.assertEqual(self.project.role, "Team Project")
        self.assertEqual(
            self.project.focus,
            "Finance Web App",
        )
        self.assertEqual(
            self.project.technology_list,
            [
                "PHP",
                "JavaScript",
                "SQL",
                "CRUD",
                "AJAX",
            ],
        )

    # =========================================================
    # PROJECT PAGE
    # =========================================================

    def test_projects_page(self):
        response = self.client.get(
            reverse("main:show_projects")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertContains(response, self.project.title)
        self.assertContains(
            response,
            self.project.description,
        )
        self.assertContains(response, "PHP")
        self.assertContains(response, "JavaScript")
        self.assertContains(response, "Team Project")
        self.assertContains(response, "Finance Web App")
        self.assertContains(
            response,
            self.project.repository_url,
        )

    def test_empty_projects_page(self):
        Project.objects.all().delete()

        response = self.client.get(
            reverse("main:show_projects")
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "Belum ada project yang ditambahkan.",
        )

    def test_projects_link_to_experience(self):
        response = self.client.get(
            reverse("main:show_projects")
        )

        self.assertContains(
            response,
            f'href="{reverse("main:show_experience")}"',
        )

    # =========================================================
    # CREATE PROJECT
    # =========================================================

    def test_create_project_page_is_accessible(self):
        self.client.force_login(self.admin_user)
        response = self.client.get(
            reverse("main:create_project")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "create_project.html",
        )
        self.assertTemplateUsed(response, "base.html")
        self.assertContains(response, "Nama Project")
        self.assertContains(response, "Add Project")

    def test_create_project_with_valid_data(self):
        self.client.force_login(self.admin_user)
        data = {
            "title": "Tutorial 03 Project",
            "description": (
                "Project untuk menguji ModelForm pada Tutorial 03."
            ),
            "year": 2026,
            "role": "Developer",
            "focus": "Form & Data Delivery",
            "technologies": "Django, Python, HTML5, CSS3",
            "repository_url": "",
        }

        response = self.client.post(
            reverse("main:create_project"),
            data,
            follow=True,
        )

        self.assertRedirects(
            response,
            reverse("main:show_projects"),
        )
        self.assertTrue(
            Project.objects.filter(
                title="Tutorial 03 Project"
            ).exists()
        )

        created = Project.objects.get(
            title="Tutorial 03 Project"
        )

        self.assertEqual(created.year, 2026)
        self.assertEqual(created.role, "Developer")
        self.assertContains(
            response,
            "Project berhasil ditambahkan!",
        )

    def test_create_project_with_invalid_data(self):
        self.client.force_login(self.admin_user)
        initial_count = Project.objects.count()

        data = {
            "title": "",
            "description": "Project tanpa judul.",
            "year": 2026,
            "role": "Developer",
            "focus": "Testing",
            "technologies": "Django, Python",
            "repository_url": "",
        }

        response = self.client.post(
            reverse("main:create_project"),
            data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "create_project.html",
        )
        self.assertEqual(
            Project.objects.count(),
            initial_count,
        )
        self.assertTrue(response.context["form"].errors)
        self.assertIn(
            "title",
            response.context["form"].errors,
        )

    # =========================================================
    # PROJECT JSON DATA DELIVERY
    # =========================================================

    def test_projects_json_endpoint(self):
        response = self.client.get(
            reverse("main:get_projects_json")
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response["Content-Type"],
            "application/json",
        )

        data = json.loads(response.content)

        self.assertEqual(len(data), 1)
        self.assertEqual(
            data[0]["fields"]["title"],
            "Cashie",
        )
        self.assertEqual(
            data[0]["fields"]["year"],
            2025,
        )

    def test_projects_json_title_filter(self):
        Project.objects.create(
            title="Personal Portfolio",
            description="Portfolio pribadi.",
            year=2026,
            role="Developer",
            focus="Web Development",
            technologies="Django, Python",
        )

        response = self.client.get(
            reverse("main:get_projects_json"),
            {"title": "cash"},
        )

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)

        self.assertEqual(len(data), 1)
        self.assertEqual(
            data[0]["fields"]["title"],
            "Cashie",
        )

    # =========================================================
    # PROJECT SEARCH
    # =========================================================

    def test_projects_page_title_filter(self):
        Project.objects.create(
            title="Personal Portfolio",
            description="Portfolio pribadi.",
            year=2026,
            role="Developer",
            focus="Web Development",
            technologies="Django, Python",
        )

        response = self.client.get(
            reverse("main:show_projects"),
            {"title": "Cashie"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cashie")
        self.assertNotContains(
            response,
            "Personal Portfolio",
        )
        self.assertEqual(
            response.context["title_query"],
            "Cashie",
        )

    def test_projects_page_search_is_case_insensitive(self):
        response = self.client.get(
            reverse("main:show_projects"),
            {"title": "cashie"},
        )

        self.assertContains(response, "Cashie")

    # =========================================================
    # DELETE PROJECT
    # =========================================================

    def test_delete_project_with_post(self):
        self.client.force_login(self.admin_user)
        delete_url = reverse(
            "main:delete_project",
            kwargs={"project_id": self.project.id},
        )

        response = self.client.post(
            delete_url,
            follow=True,
        )

        self.assertRedirects(
            response,
            reverse("main:show_projects"),
        )
        self.assertFalse(
            Project.objects.filter(
                id=self.project.id
            ).exists()
        )
        self.assertContains(
            response,
            "Project berhasil dihapus!",
        )

    def test_delete_project_with_get_does_not_delete(self):
        self.client.force_login(self.admin_user)
        delete_url = reverse(
            "main:delete_project",
            kwargs={"project_id": self.project.id},
        )

        response = self.client.get(delete_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            reverse("main:show_projects"),
        )
        self.assertTrue(
            Project.objects.filter(
                id=self.project.id
            ).exists()
        )

    def test_delete_project_url_uses_uuid(self):
        delete_url = reverse(
            "main:delete_project",
            kwargs={"project_id": self.project.id},
        )

        self.assertEqual(
            delete_url,
            (
                f"/projects/"
                f"{self.project.id}/"
                f"delete/"
            ),
        )

    def test_delete_nonexistent_project_returns_404(self):
        self.client.force_login(self.admin_user)

        nonexistent_uuid = (
            "11111111-1111-1111-1111-111111111111"
        )

        response = self.client.post(
            reverse(
                "main:delete_project",
                kwargs={
                    "project_id": nonexistent_uuid,
                },
            )
        )

        self.assertEqual(response.status_code, 404)