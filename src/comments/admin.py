"""Admin configuration for the comments app."""
from django.contrib import admin
from .models import Comment

admin.site.register(Comment)
