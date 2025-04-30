from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404




# from django.core.management import call_command
# from django.http import HttpResponse
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





@login_required
def profile_view(request):
    return render(request, 'profile.html')

@login_required
def upgrade_view(request):
    if request.method == 'POST':
        status = request.POST.get('new_status')
        if status in ['regular', 'advanced']:
            request.user.status = status
            request.user.save()
            return redirect('profile')
    return render(request, 'upgrade.html')


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # Доступен либо если курс бесплатный, либо пользователь с подпиской
    if course.is_free or getattr(request.user, 'status', 'regular') == 'advanced':
        return render(request, 'course_detail.html', {'course': course})

    # Иначе перенаправим на шаблон блокировки
    return render(request, 'course_locked.html', {'course': course})


# views.py
from .models import Course

def courses_view(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})



# def collectstatic_now(request):
#     call_command("collectstatic", interactive=False)
#     return HttpResponse("✅ collectstatic выполнен")



from django.http import HttpResponse
from django.core.management import call_command


def migrate_now(request):
    call_command("migrate")
    return HttpResponse("✅ Миграции выполнены на сервере.")
