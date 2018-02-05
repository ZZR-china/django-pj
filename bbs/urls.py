from django.urls import path
from django.urls import include

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
router.register(r'userprofiles', controllers.UserProfileViewSet)
router.register(r'usergroups', controllers.UserGroupViewSet)


urlpatterns = [
    path('', include(router.urls))
]
