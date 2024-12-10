from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_token = models.CharField(max_length=255, blank=True, null=True)
    twitter_token = models.CharField(max_length=255, blank=True, null=True)

class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)  # 'Facebook', 'Twitter'
    content = models.TextField()
    likes = models.IntegerField(default=0)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username