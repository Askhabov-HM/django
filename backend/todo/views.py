from django.shortcuts import render
from rest_framework import generics
from .models import Todo, Category
from .serializers import TodoSerializer, CategorySerializer

# Create your views here.

class TodoAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoCategoriesAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer