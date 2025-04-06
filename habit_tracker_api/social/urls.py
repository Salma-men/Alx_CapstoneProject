from django.urls import path
from .views import FollowUserView, UnfollowUserView, FollowersView, FollowingView

urlpatterns = [
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('followers/', FollowersView.as_view(), name='followers-list'),
    path('following/', FollowingView.as_view(), name='following-list'),
]
