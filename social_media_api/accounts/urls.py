from django.urls import path
from .views import RegisterView, LoginView
from .views import follow_user, unfollow_user
#from . import views
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
    #path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    #path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
]

# In the main app's urls.py

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
