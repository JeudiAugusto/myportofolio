from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from main.forms import ProjectForm
from main.models import Experience, Project


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
        "project_list": Project.objects.all().order_by(
            "-year",
            "title",
        ),
    }

    return render(
        request,
        "index.html",
        context,
    )


def show_experience(request):
    context = {
        "name": "Jeudi Augusto Asadullah",
        "experience_list": Experience.objects.all(),
    }

    return render(
        request,
        "experience.html",
        context,
    )


def get_projects_json(request):
    title_query = request.GET.get(
        "title",
        "",
    ).strip()

    projects = Project.objects.all().order_by(
        "-year",
        "title",
    )

    if title_query:
        projects = projects.filter(
            title__icontains=title_query
        )

    projects_json = serializers.serialize(
        "json",
        projects,
    )

    return HttpResponse(
        projects_json,
        content_type="application/json",
    )


def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    projects = [
        project.object
        for project in projects
    ]

    title_query = request.GET.get(
        "title",
        "",
    ).strip()

    context = {
        "name": "Jeudi Augusto Asadullah",
        "project_list": projects,
        "title_query": title_query,
    }

    return render(
        request,
        "projects.html",
        context,
    )


def create_project(request):
    form = ProjectForm(
        request.POST or None
    )

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(
            request,
            "Project berhasil ditambahkan!",
        )

        return redirect(
            "main:show_projects"
        )

    context = {
        "name": "Jeudi Augusto Asadullah",
        "form": form,
    }

    return render(
        request,
        "create_project.html",
        context,
    )


def delete_project(request, project_id):
    project = get_object_or_404(
        Project,
        pk=project_id,
    )

    if request.method == "POST":
        project.delete()

        messages.success(
            request,
            "Project berhasil dihapus!",
        )

        return redirect(
            "main:show_projects"
        )

    return redirect(
        "main:show_projects"
    )