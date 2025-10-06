from django.shortcuts import render
from .serializers import RegisterSerializer, BlogSerializer
from .models import BlogModel
from rest_framework import generics,permissions
from django.contrib.auth.models import User

# Create your views here.

class BlogView(generics.ListAPIView):

    serializer_class = BlogSerializer
    queryset = BlogModel.objects.all()

class CreateBlogView(generics.CreateAPIView):

    serializer_class = BlogSerializer
    queryset = BlogModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class DetailView(generics.RetrieveAPIView):

    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class DeleteView(generics.RetrieveUpdateDestroyAPIView):

    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

