from django.contrib import admin

from common.author.models import Category, Teacher


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
