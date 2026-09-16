import json

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Project


class MainTest(TestCase):

    def setUp(self):
        # Bersihkan data yang mungkin dibuat oleh data migration
        # agar setiap test memiliki kondisi awal yang terkontrol.
        Experience.objects.all().delete()
        Project.objects.all().delete()

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
        response = self.client.get(
            reverse("main:show_main")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertTemplateUsed(
            response,
            "index.html",
        )

        self.assertTemplateUsed(
            response,
            "base.html",
        )

        self.assertContains(
            response,
            self.project.title,
        )

        self.assertNotContains(
            response,
            self.experience.title,
        )

        self.assertContains(
            response,
            f'href="{reverse("main:show_projects")}"',
        )

        self.assertContains(
            response,
            f'href="{reverse("main:show_experience")}"',
        )

    def test_nonexistent_page_returns_404(self):
        response = self.client.get(
            "/halaman-yang-tidak-ada/"
        )

        self.assertEqual(
            response.status_code,
            404,
        )

    # =========================================================
    # EXPERIENCE
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

        self.assertTrue(
            self.experience.is_ongoing
        )

    def test_experience_page(self):
        response = self.client.get(
            reverse("main:show_experience")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertTemplateUsed(
            response,
            "experience.html",
        )

        self.assertTemplateUsed(
            response,
            "base.html",
        )

        self.assertContains(
            response,
            self.experience.title,
        )

        self.assertContains(
            response,
            self.experience.description,
        )

        self.assertContains(
            response,
            "Organization",
        )

        self.assertContains(
            response,
            "Sedang berlangsung",
        )

        self.assertContains(
            response,
            f'href="{reverse("main:show_main")}"',
        )

    def test_empty_experience_page(self):
        Experience.objects.all().delete()

        response = self.client.get(
            reverse("main:show_experience")
        )

        self.assertContains(
            response,
            "Belum ada pengalaman yang ditambahkan.",
        )

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()

        response = self.client.get(
            reverse("main:show_experience")
        )

        self.experience.refresh_from_db()

        self.assertFalse(
            self.experience.is_ongoing
        )

        self.assertContains(
            response,
            "Selesai",
        )

    # =========================================================
    # PROJECT MODEL
    # =========================================================

    def test_project_model(self):
        self.assertEqual(
            str(self.project),
            "Cashie",
        )

        self.assertEqual(
            self.project.year,
            2025,
        )

        self.assertEqual(
            self.project.role,
            "Team Project",
        )

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

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertTemplateUsed(
            response,
            "projects.html",
        )

        self.assertTemplateUsed(
            response,
            "base.html",
        )

        self.assertContains(
            response,
            self.project.title,
        )

        self.assertContains(
            response,
            self.project.description,
        )

        self.assertContains(
            response,
            "PHP",
        )

        self.assertContains(
            response,
            "JavaScript",
        )

        self.assertContains(
            response,
            "Team Project",
        )

        self.assertContains(
            response,
            "Finance Web App",
        )

        self.assertContains(
            response,
            self.project.repository_url,
        )

    def test_empty_projects_page(self):
        Project.objects.all().delete()

        response = self.client.get(
            reverse("main:show_projects")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

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
        response = self.client.get(
            reverse("main:create_project")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertTemplateUsed(
            response,
            "create_project.html",
        )

        self.assertTemplateUsed(
            response,
            "base.html",
        )

        self.assertContains(
            response,
            "Nama Project",
        )

        self.assertContains(
            response,
            "Add Project",
        )

    def test_create_project_with_valid_data(self):
        project_data = {
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
            project_data,
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

        created_project = Project.objects.get(
            title="Tutorial 03 Project"
        )

        self.assertEqual(
            created_project.year,
            2026,
        )

        self.assertEqual(
            created_project.role,
            "Developer",
        )

        self.assertContains(
            response,
            "Project berhasil ditambahkan!",
        )

    def test_create_project_with_invalid_data(self):
        initial_project_count = Project.objects.count()

        invalid_data = {
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
            invalid_data,
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertTemplateUsed(
            response,
            "create_project.html",
        )

        self.assertEqual(
            Project.objects.count(),
            initial_project_count,
        )

        self.assertTrue(
            response.context["form"].errors
        )

        self.assertIn(
            "title",
            response.context["form"].errors,
        )

    # =========================================================
    # JSON DATA DELIVERY
    # =========================================================

    def test_projects_json_endpoint(self):
        response = self.client.get(
            reverse("main:get_projects_json")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertEqual(
            response["Content-Type"],
            "application/json",
        )

        data = json.loads(
            response.content
        )

        self.assertEqual(
            len(data),
            1,
        )

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
            {
                "title": "cash",
            },
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        data = json.loads(
            response.content
        )

        self.assertEqual(
            len(data),
            1,
        )

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
            {
                "title": "Cashie",
            },
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertContains(
            response,
            "Cashie",
        )

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
            {
                "title": "cashie",
            },
        )

        self.assertContains(
            response,
            "Cashie",
        )

    # =========================================================
    # DELETE PROJECT
    # =========================================================

    def test_delete_project_with_post(self):
        delete_url = reverse(
            "main:delete_project",
            kwargs={
                "project_id": self.project.id,
            },
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
        delete_url = reverse(
            "main:delete_project",
            kwargs={
                "project_id": self.project.id,
            },
        )

        response = self.client.get(
            delete_url
        )

        self.assertEqual(
            response.status_code,
            302,
        )

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
            kwargs={
                "project_id": self.project.id,
            },
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

        self.assertEqual(
            response.status_code,
            404,
        )