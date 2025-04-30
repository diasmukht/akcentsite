from django.urls import path
from . import views
# from .views import migrate_now
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('instructor/', views.instructor, name='instructor'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),  # ✅ правильно

    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('single/', views.single, name='single'),
    # path('migrate-now/', migrate_now, name='migrate-now'),
]
