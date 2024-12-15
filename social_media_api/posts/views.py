from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework import filters

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from .serializers import LikeSerializer
from notifications.models import Notification  # Import Notification model
from django.contrib.auth import get_user_model

User = get_user_model()

# View to like a post
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can like posts

    def post(self, request, pk):
        # Fetch the post using generics.get_object_or_404
        post = generics.get_object_or_404(Post, pk=pk)  
        user = request.user

        # Use Like.objects.get_or_create to ensure a single like per user
        like, created = Like.objects.get_or_create(user=user, post=post)  

        if not created:
            return Response({"error": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Generate a notification for the post owner
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb="liked your post",
            target=post
        )

        return Response({"message": "Post liked successfully."}, status=status.HTTP_201_CREATED)

# View to unlike a post
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can unlike posts

    def post(self, request, pk):
        # Fetch the post using generics.get_object_or_404
        post = generics.get_object_or_404(Post, pk=pk)  
        user = request.user

        # Check if the user has liked the post
        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({"error": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Remove the Like entry
        like.delete()

        return Response({"message": "Post unliked successfully."}, status=status.HTTP_200_OK)
