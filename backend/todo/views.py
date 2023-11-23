from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Todo, Category
from .serializers import *

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Todo.objects.all()[:2]

        return Todo.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)
    def category(self, request):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})

# class TodoAPIList(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

# class TodoAPIView(APIView):
#     def get(self, request):
#         lst = Todo.objects.all()
#         return Response({'data': TodoSerializer(lst, many=True).data})

#     def post(self, request):
#         serializer = TodoSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'data': serializer.data})
    
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
        
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
        
#         try:
#             instance = Todo.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object doesnt exists"})
        
#         serializer = TodoSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({"data": serializer.data})
    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)

#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
        
#         try:
#             instance = Todo.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"error": "Object doesnt exists"})
        
#         return Response({"data": "delete post" + str(pk)})

# class TodoAPIView(generics.ListAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

class TodoCategoriesAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer