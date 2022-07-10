from django.shortcuts import render
from rest_framework import viewsets

from .serializers import HeroSerializer
from .serializers import PostSerializer
from .serializers import UserSerializer
from .models import Hero
from .models import Post
from .models import User

# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer