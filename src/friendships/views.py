from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db import models
from .models import FriendRequest
from .serializers import FriendRequestSerializer

class SendFriendRequestView(generics.CreateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, user_id):
        receiver = get_object_or_404(User, id=user_id)
        if request.user == receiver:
            return Response(
                {"error": "You cannot send friend request to yourself"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        friend_request, created = FriendRequest.objects.get_or_create(
            sender=request.user,
            receiver=receiver
        )
        
        if not created:
            return Response(
                {"error": "Friend request already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        serializer = self.get_serializer(friend_request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RespondToFriendRequestView(generics.UpdateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        return FriendRequest.objects.filter(receiver=self.request.user, status='pending')

    def update(self, request, *args, **kwargs):
        friend_request = self.get_object()
        action = request.data.get('action')
        
        if action not in ['accept', 'reject']:
            return Response(
                {"error": "Invalid action"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        friend_request.status = 'accepted' if action == 'accept' else 'rejected'
        friend_request.save()
        
        serializer = self.get_serializer(friend_request)
        return Response(serializer.data)

class ListFriendsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return FriendRequest.objects.filter(
            status='accepted'
        ).filter(
            models.Q(sender=self.request.user) | models.Q(receiver=self.request.user)
        )
