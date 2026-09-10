from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Project


class MainTest(TestCase):
    def setUp(self):
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

        self.assertFalse(
            self.experience.is_ongoing
        )

        self.assertContains(
            response,
            "Selesai",
        )

        self.assertNotContains(
            response,
            "Sedang berlangsung",
        )

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