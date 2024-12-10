from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Profile, Post,UserProfile
from rest_framework.permissions import IsAuthenticated
from .serializers import UserRegistrationSerializer
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



class FetchSocialMediaData(APIView):
    def get(self, request, platform):
        # Fetch data from APIs (Facebook/Twitter integration logic here)
        return Response({"message": "Data fetched successfully."})

class CreatePost(APIView):
    def post(self, request):
        # Handle creating and sharing posts across platforms
        return Response({"message": "Post created successfully."})

class Analytics(APIView):
    def get(self, request):
        # Calculate and return user activity analytics
        return Response({"analytics": {}})
      

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class FetchPostsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, platform):
        posts = Post.objects.filter(user=request.user.profile, platform=platform)
        return Response({"posts": [post.content for post in posts]})
    
    
    
class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom Token view to issue JWT tokens along with user information.
    """
    def post(self, request, *args, **kwargs):
        print(f"Request data: {request.data}")  # Debugging line
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            username = request.data.get('username', '')
            try:
                user = User.objects.get(username=username)
                response.data['username'] = user.username
                response.data['email'] = user.email
            except User.DoesNotExist:
                return Response({"detail": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        return response



    
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "username": request.user.username,
            "email": request.user.email,
        })
        
class UserDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  # This will fetch the authenticated user
        user_data = {
            'username': user.username,
            'email': user.email,
            'bio': user.profile.bio if hasattr(user, 'profile') else '',
            'avatar': user.profile.avatar.url if hasattr(user, 'profile') and user.profile.avatar else None
        }
        return Response(user_data)
    


