from django.urls import path
from . import views
from .views import profile_view, upgrade_view, logout_view, course_list, course_detail, migrate_now

# from .views import collectstatic_now
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('instructor/', views.instructor, name='instructor'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),  # ✅ правильно
    path('profile/', profile_view, name='profile'),
    path('upgrade/', upgrade_view, name='upgrade'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('single/', views.single, name='single'),
    path('logout/', logout_view, name='logout'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),

    path('courses/', course_list, name='courses'),
    path('courses/<int:course_id>/', course_detail, name='course_detail'),
    path('migrate-now/', migrate_now, name='migrate-now'),
    # path('collectstatic_now/', collectstatic_now, name='collectstatic'),
]
