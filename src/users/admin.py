"""Admin configuration for the users app."""
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
