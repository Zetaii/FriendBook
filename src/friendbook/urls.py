from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request, format=None):
    return Response({
        'register': reverse('register', request=request, format=format),
        'login': reverse('token_obtain_pair', request=request, format=format),
        'profile': reverse('profile', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format),
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    path('api/auth/', include('users.urls')),
    path('api/friends/', include('friendships.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/', include('comments.urls')),
] 