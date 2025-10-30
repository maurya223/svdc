from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),
    path('appointment/success/', views.appointment_success, name='appointment_success'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),
]
