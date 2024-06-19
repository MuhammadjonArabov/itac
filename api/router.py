from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from api.author.views import TeacherAPIView, CategoryAPIViews

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register(r'teacher', TeacherAPIView, basename='teacher')
router.register(r'category', CategoryAPIViews, basename='category')

urlpatterns = router.urls
