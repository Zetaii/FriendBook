"""Admin configuration for the friendships app."""
from django.contrib import admin
from .models import FriendRequest

admin.site.register(FriendRequest)
