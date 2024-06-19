from django.db import models
from common.base import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Teacher(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=13)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.first_name
