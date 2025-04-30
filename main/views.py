def index(request):
    return render(request, 'index.html')


from django.shortcuts import render


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def courses(request):
    return render(request, 'courses.html')


def instructor(request):
    return render(request, 'instructor.html')


def login_view(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def team(request):
    return render(request, 'team.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def single(request):
    return render(request, 'single.html')


from django.http import HttpResponse
from django.core.management import call_command


def migrate_now(request):
    call_command("migrate")
    return HttpResponse("✅ Миграции выполнены на сервере.")
