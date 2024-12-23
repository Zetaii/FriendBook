from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/friends/', include('friendships.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/', include('comments.urls')),
] 