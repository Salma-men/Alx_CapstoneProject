from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Friendship
from django.contrib.auth.models import User

class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if already following
        if Friendship.objects.filter(user=request.user, friend=user_to_follow).exists():
            return Response({"message": "You are already following this user."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new friendship (follow)
        Friendship.objects.create(user=request.user, friend=user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}."}, status=status.HTTP_201_CREATED)

class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user is following
        friendship = Friendship.objects.filter(user=request.user, friend=user_to_unfollow).first()
        if not friendship:
            return Response({"message": "You are not following this user."}, status=status.HTTP_400_BAD_REQUEST)

        # Unfollow
        friendship.delete()
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)

class FollowersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        followers = Friendship.objects.filter(friend=request.user)
        followers_list = [follower.user.username for follower in followers]
        return Response({"followers": followers_list}, status=status.HTTP_200_OK)

class FollowingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following = Friendship.objects.filter(user=request.user)
        following_list = [friend.friend.username for friend in following]
        return Response({"following": following_list}, status=status.HTTP_200_OK)
