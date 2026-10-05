import datetime
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import (get_object_or_404, redirect,render,)
from main.forms import ExperienceForm, ProjectForm
from main.models import Experience, Project
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST

def register(request):
    form = UserCreationForm(
        request.POST or None
    )

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(
            request,
            "Akun berhasil dibuat. Silakan login.",
        )

        return redirect(
            "main:login"
        )

    context = {
        "name": "Jeudi Augusto Asadullah",
        "form": form,
    }

    return render(
        request,
        "register.html",
        context,
    )

def login_user(request):
    form = AuthenticationForm(
        request,
        data=request.POST or None,
    )

    if request.method == "POST" and form.is_valid():
        user = form.get_user()

        login(
            request,
            user,
        )

        response = redirect(
            "main:show_main"
        )

        response.set_cookie(
            "last_login",
            datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        )

        return response

    context = {
        "name": "Jeudi Augusto Asadullah",
        "form": form,
    }

    return render(
        request,
        "login.html",
        context,
    )

def logout_user(request):
    logout(request)

    response = redirect(
        "main:show_main"
    )

    response.delete_cookie(
        "last_login"
    )

    return response

def show_main(request):
    last_login = request.COOKIES.get(
        "last_login",
        "Belum ada sesi login / Cookie tidak ditemukan",
    )

    context = {
        "name": "Jeudi Augusto Asadullah",
        "npm": "2506656822",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Halo! Saya Jeudi Augusto Asadullah, mahasiswa Sistem Informasi "
            "Universitas Indonesia yang sedang mempelajari pengembangan web "
            "menggunakan Django."
        ),
        "last_login": last_login,
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

    return render(
        request,
        "index.html",
        context,
    )

def is_editor(user):
    return (
        user.is_authenticated
        and user.groups.filter(
            name="Editor"
        ).exists()
    )


# =========================================================
# EXPERIENCE
# =========================================================

def get_experiences_json(request):
    experiences = Experience.objects.all().order_by(
        "-started_at"
    )

    experiences_json = serializers.serialize(
        "json",
        experiences,
        use_natural_foreign_keys=True,
    )

    return HttpResponse(
        experiences_json,
        content_type="application/json",
    )


def show_experience(request):
    json_response = get_experiences_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    experiences = [
        experience.object
        for experience in experiences
    ]

    context = {
        "name": "Jeudi Augusto Asadullah",
        "experience_list": experiences,
        "is_editor": is_editor(request.user),
    }

    return render(
        request,
        "experience.html",
        context,
    )


@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ExperienceForm(
        request.POST or None
    )

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(
            request,
            "Experience berhasil ditambahkan!",
        )

        return redirect(
            "main:show_experience"
        )

    context = {
        "name": "Jeudi Augusto Asadullah",
        "form": form,
    }

    return render(
        request,
        "create_experience.html",
        context,
    )


@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if (
        not request.user.is_superuser
        and not is_editor(request.user)
    ):
        raise PermissionDenied

    experience = get_object_or_404(
        Experience,
        pk=experience_id,
    )

    form = ExperienceForm(
        request.POST or None,
        instance=experience,
    )

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(
            request,
            "Experience berhasil diperbarui!",
        )

        return redirect(
            "main:show_experience"
        )

    context = {
        "name": "Jeudi Augusto Asadullah",
        "form": form,
        "experience": experience,
    }

    return render(
        request,
        "update_experience.html",
        context,
    )


@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(
        Experience,
        pk=experience_id,
    )

    if request.method == "POST":
        experience.delete()

        messages.success(
            request,
            "Experience berhasil dihapus!",
        )

        return redirect(
            "main:show_experience"
        )

    return redirect(
        "main:show_experience"
    )

@login_required(login_url="/login/")
def toggle_experience_star(request, experience_id):
    experience = get_object_or_404(
        Experience,
        pk=experience_id,
    )

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(
                request.user
            )
        else:
            experience.starred_by.add(
                request.user
            )

    return redirect(
        "main:show_experience"
    )


# =========================================================
# PROJECT
# =========================================================

def get_projects_json(request):
    title_query = request.GET.get(
        "title",
        "",
    ).strip()

    projects = Project.objects.prefetch_related(
        "starred_by"
    ).all().order_by(
        "-year",
        "title",
    )

    if title_query:
        projects = projects.filter(
            title__icontains=title_query
        )

    data = []

    for project in projects:
        starred_users = project.starred_by.all()

        is_starred = (
            request.user in starred_users
            if request.user.is_authenticated
            else False
        )

        starred_by_names = ", ".join(
            user.username
            for user in starred_users
        )

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "year": project.year,
                "role": project.role,
                "focus": project.focus,
                "technologies": project.technologies,
                "repository_url": project.repository_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            },
        })

    return JsonResponse(
        data,
        safe=False,
    )
def show_projects(request):
    title_query = request.GET.get(
        "title",
        "",
    ).strip()

    context = {
        "name": "Jeudi Augusto Asadullah",
        "title_query": title_query,
        "form": ProjectForm(),
    }

    return render(
        request,
        "projects.html",
        context,
    )
@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {
                "message": (
                    "Hanya pemilik portofolio yang dapat "
                    "menambahkan proyek."
                )
            },
            status=403,
        )

    form = ProjectForm(request.POST)

    if form.is_valid():
        project = form.save()

        return JsonResponse(
            {
                "message": "Proyek berhasil ditambahkan.",
                "project_id": str(project.id),
            },
            status=201,
        )

    return JsonResponse(
        {
            "message": "Data proyek tidak valid.",
            "errors": form.errors.get_json_data(),
        },
        status=400,
    )

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ProjectForm(request.POST or None)

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

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied

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

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(
        Project,
        pk=project_id,
    )

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(
                request.user
            )
        else:
            project.starred_by.add(
                request.user
            )

    return redirect(
        "main:show_projects"
    )
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

# Pastikan import ada, tidak akan error jika sudah ter-import di atas
try:
    from .models import Experience
except ImportError:
    pass
try:
    from .forms import ExperienceForm
except ImportError:
    pass

def experience_json(request):
    query = request.GET.get('q', '')
    if query:
        experiences = Experience.objects.filter(title__icontains=query)
    else:
        experiences = Experience.objects.all()

    data = []
    for exp in experiences:
        is_starred = False
        star_count = 0
        if hasattr(exp, 'starred_by'):
            star_count = exp.starred_by.count()
            if request.user.is_authenticated:
                is_starred = exp.starred_by.filter(id=request.user.id).exists()

        data.append({
            'id': exp.id,
            'title': getattr(exp, 'title', ''),
            'description': getattr(exp, 'description', ''),
            'year': getattr(exp, 'year', ''),
            'role': getattr(exp, 'role', ''),
            'is_starred': is_starred,
            'star_count': star_count,
        })
    return JsonResponse({'experiences': data})

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse({'status': 'error', 'message': 'Forbidden'}, status=403)

    form = ExperienceForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': 'success', 'message': 'Experience added successfully'}, status=201)
    else:
        errors = json.loads(form.errors.as_json())
        return JsonResponse({'status': 'error', 'message': 'Validation failed', 'errors': errors}, status=400)
