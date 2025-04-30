from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib import messages
def index(request):
    return render(request, 'index.html')





def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def courses(request):
    return render(request, 'courses.html')


def instructor(request):
    return render(request, 'instructor.html')


def team(request):
    return render(request, 'team.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def single(request):
    return render(request, 'single.html')

# ✅ Регистрация
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


# ✅ Вход
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Қате email немесе пароль')
    return render(request, 'login.html')


# ✅ Выход
def logout_view(request):
    logout(request)
    return redirect('login')


















# from django.http import HttpResponse
# from django.core.management import call_command


# def migrate_now(request):
#     call_command("migrate")
#     return HttpResponse("✅ Миграции выполнены на сервере.")
