from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo, Category
from .serializers import TodoSerializer, CategorySerializer

# Create your views here.

class TodoAPIView(APIView):
    def get(self, request):
        lst = Todo.objects.all().values()
        return Response({'todos': list(lst)})

    def post(self, request):
        todo_new = Todo.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            category_id = request.data['category_id']
        )

        return Response({'post': model_to_dict(todo_new)})

# class TodoAPIView(generics.ListAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

class TodoCategoriesAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer