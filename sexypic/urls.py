from django.urls import path
from django.urls import include

from rest_framework.routers import DefaultRouter

from . import views
from . import controllers

app_name = 'sexypic'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'albums', controllers.AlbumViewSet)
router.register(r'pictures', controllers.PictureViewSet)
router.register(r'snippets', controllers.SnippetViewSet)
router.register(r'tags', controllers.TagViewSet)
router.register(r'users', controllers.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('meizi/', views.meizi, name='meizi'),
    path('picturedownload/', views.picturedownload, name='picturedownload'),
]
