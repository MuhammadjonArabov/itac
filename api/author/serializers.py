from rest_framework import serializers
from common.author.models import Category, Teacher


class CategoryCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'guid', 'title']


class TeacherCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'guid', 'first_name', 'last_name', 'country', 'email', 'phone', 'category']


