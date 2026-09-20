from django.forms import (
    ModelForm,
    NumberInput,
    Select,
    Textarea,
    TextInput,
    URLInput,
)

from main.models import Experience, Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project

        fields = [
            "title",
            "description",
            "year",
            "role",
            "focus",
            "technologies",
            "repository_url",
        ]

        labels = {
            "title": "Nama Project",
            "description": "Deskripsi Project",
            "year": "Tahun",
            "role": "Peran",
            "focus": "Fokus Project",
            "technologies": "Teknologi yang Digunakan",
            "repository_url": "URL Repository",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: Personal Portfolio",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": (
                        "Jelaskan project yang kamu kerjakan..."
                    ),
                    "rows": 4,
                }
            ),
            "year": NumberInput(
                attrs={
                    "placeholder": "2026",
                    "min": 2000,
                    "max": 2100,
                }
            ),
            "role": TextInput(
                attrs={
                    "placeholder": "Contoh: Developer",
                    "maxlength": 100,
                }
            ),
            "focus": TextInput(
                attrs={
                    "placeholder": "Contoh: Web Development",
                    "maxlength": 150,
                }
            ),
            "technologies": TextInput(
                attrs={
                    "placeholder": (
                        "Django, Python, HTML5, CSS3"
                    ),
                }
            ),
            "repository_url": URLInput(
                attrs={
                    "placeholder": (
                        "https://github.com/username/project"
                    ),
                }
            ),
        }


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience

        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
        ]

        labels = {
            "title": "Nama Experience",
            "description": "Deskripsi Experience",
            "category": "Kategori",
            "thumbnail": "Path Thumbnail",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": (
                        "Contoh: Staff Kajian dan Aksi Strategis"
                    ),
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": (
                        "Jelaskan pengalaman dan tanggung jawab..."
                    ),
                    "rows": 5,
                }
            ),
            "category": Select(),
            "thumbnail": TextInput(
                attrs={
                    "placeholder": (
                        "Contoh: img/experience/kegiatan.jpg"
                    ),
                    "maxlength": 255,
                }
            ),
        }