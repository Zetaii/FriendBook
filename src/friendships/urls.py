from django.urls import path
from .views import SendFriendRequestView, RespondToFriendRequestView, ListFriendsView

urlpatterns = [
    path('request/<int:user_id>/', SendFriendRequestView.as_view(), name='send_friend_request'),
    path('respond/<int:pk>/', RespondToFriendRequestView.as_view(), name='respond_to_friend_request'),
    path('list/', ListFriendsView.as_view(), name='list_friends'),
] 