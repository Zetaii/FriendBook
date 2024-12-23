from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        # Get posts from user and their friends
        friend_requests = self.request.user.received_requests.filter(
            status='accepted'
        ).values_list('sender', flat=True)
        
        friend_requests_sent = self.request.user.sent_requests.filter(
            status='accepted'
        ).values_list('receiver', flat=True)
        
        friends = list(friend_requests) + list(friend_requests_sent)
        friends.append(self.request.user.id)
        
        return Post.objects.filter(user_id__in=friends)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)
