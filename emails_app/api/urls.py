from django.contrib import admin
from django.urls import path
from .views import ContactEmailView
from django.views.decorators.cache import cache_page
from django.conf import settings
CACHE_TTL = getattr(settings, 'CACHE_TTL', 60 * 15)


urlpatterns = [
    path('contact-email/', cache_page(CACHE_TTL)(ContactEmailView.as_view()), name='contact_email'),
]