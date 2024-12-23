from django.urls import path
from .views import CommentListCreateView, CommentDetailView

urlpatterns = [
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('posts/<int:post_id>/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
] 