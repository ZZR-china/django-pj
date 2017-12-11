from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from . import controllers

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'users', controllers.UserViewSet)
router.register(r'groups', controllers.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
