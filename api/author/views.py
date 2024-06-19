from rest_framework import viewsets
from rest_framework.response import Response
from api.author.serializers import TeacherCreateSerializers, CategoryCreateSerializers
from common.author.models import Teacher, Category
import re


class TeacherAPIView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializers

    def perform_create(self, serializer):
        phone = self.request.data.get('phone')
        if not re.match(r'^\+\d{1,3}-\d{3,}$', phone):
            respoonse_data = {"phone": ["The phone number is in the wrong format"]}
            return Response(respoonse_data, status=400)
        serializer.save()


class CategoryAPIViews(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializers
