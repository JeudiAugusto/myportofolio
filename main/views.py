from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Jeudi Augusto Asadullah",
        "npm": "2506656822",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Halo! Saya Jeudi Augusto Asadullah, mahasiswa Sistem Informasi "
            "Universitas Indonesia yang sedang mempelajari pengembangan web "
            "menggunakan Django."
        ),
    }

    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Jeudi Augusto Asadullah",
        "experience_list": Experience.objects.all(),
    }

    return render(request, "experience.html", context)