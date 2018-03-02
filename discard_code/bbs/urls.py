from django.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter

from . import controllers
from . import views

app_name = 'bbs'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'articles', controllers.ArticleViewSet)
router.register(r'categorys', controllers.CategoryViewSet)
router.register(r'comments', controllers.CommentViewSet)
router.register(r'thumbups', controllers.ThumbUpViewSet)

urlpatterns = [
    path('', include(router.urls))
]
