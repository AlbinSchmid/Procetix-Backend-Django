from django.contrib import admin
from django.urls import path
from .views import ContactEmailView, ProjectEmailView

urlpatterns = [
    path('contact-email', ContactEmailView.as_view(), name='contact_email'),
    path('project-email', ProjectEmailView.as_view(), name='project_email'),
]