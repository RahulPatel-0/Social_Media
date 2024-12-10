from django.urls import path
from .views import FetchSocialMediaData, CreatePost, Analytics,RegisterView, FetchPostsView,CustomTokenObtainPairView, UserProfileView, UserProfileView,UserDashboardView

urlpatterns = [
    path('fetch/<str:platform>/', FetchSocialMediaData.as_view(), name='fetch'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('analytics/', Analytics.as_view(), name='analytics'),
    path('register/', RegisterView.as_view(), name='register'),
    path('fetch_posts/<str:platform>/', FetchPostsView.as_view(), name='fetch_posts'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('dashboard/', UserDashboardView.as_view(), name='user_dashboard'),
    
]
