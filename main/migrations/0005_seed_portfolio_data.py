from datetime import datetime, timezone

from django.db import migrations


def seed_portfolio_data(apps, schema_editor):
    Experience = apps.get_model("main", "Experience")
    Project = apps.get_model("main", "Project")

    # =====================================================
    # PROJECTS
    # =====================================================

    Project.objects.update_or_create(
        title="Personal Portfolio",
        defaults={
            "description": (
                "Website portfolio pribadi yang dibangun menggunakan "
                "Django, HTML5, dan CSS3 dengan responsive layout, "
                "semantic HTML, serta interactive UI elements."
            ),
            "year": 2026,
            "role": "Developer",
            "focus": "Web UI",
            "technologies": "Django, Python, HTML5, CSS3",
            "repository_url": (
                "https://github.com/JeudiAugusto/myportofolio"
            ),
        },
    )

    Project.objects.update_or_create(
        title="Cashie",
        defaults={
            "description": (
                "Aplikasi web pengelola keuangan yang dikembangkan "
                "menggunakan PHP dan JavaScript dengan fitur "
                "authentication, dashboard, CRUD, dan AJAX."
            ),
            "year": 2025,
            "role": "Team Project",
            "focus": "Finance Web App",
            "technologies": (
                "PHP, JavaScript, SQL, CRUD, AJAX"
            ),
            "repository_url": (
                "https://github.com/fzdhl/cashie"
            ),
        },
    )

    # =====================================================
    # EXPERIENCE
    # =====================================================

    experience, _ = Experience.objects.update_or_create(
        title="Staff Kajian dan Aksi Strategis",
        defaults={
            "description": (
                "Berperan sebagai Staff Kajian dan Aksi Strategis "
                "BEM Fasilkom UI 2026 dalam kegiatan organisasi "
                "kemahasiswaan serta pengembangan kemampuan analisis, "
                "kolaborasi, dan komunikasi."
            ),
            "category": "organization",
            "thumbnail": (
                "img/experience/"
                "kastrat-bem-fasilkom-2026.jpg"
            ),
            "ended_at": None,
        },
    )

    Experience.objects.filter(
        pk=experience.pk
    ).update(
        started_at=datetime(
            2026,
            5,
            25,
            tzinfo=timezone.utc,
        )
    )


def reverse_seed_portfolio_data(apps, schema_editor):
    Project = apps.get_model("main", "Project")
    Experience = apps.get_model("main", "Experience")

    Project.objects.filter(
        title__in=[
            "Personal Portfolio",
            "Cashie",
        ]
    ).delete()

    Experience.objects.filter(
        title="Staff Kajian dan Aksi Strategis"
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_project"),
    ]

    operations = [
        migrations.RunPython(
            seed_portfolio_data,
            reverse_seed_portfolio_data,
        ),
    ]