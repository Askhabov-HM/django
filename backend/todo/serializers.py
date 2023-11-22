from rest_framework import serializers
from .models import Todo, Category

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
    # pk = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # content = serializers.CharField()
    # category_id = serializers.IntegerField()

    # def create(self, validated_data):
    #     return Todo.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.category_id = validated_data.get('category_id', instance.category_id)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'name')