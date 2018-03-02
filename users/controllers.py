from .models import UserProfile

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .serializers import ProfileSerializer
from .serializers import GroupSerializer
from .serializers import AppProfileSerializer

from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = ProfileSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@permission_classes((AllowAny, ))
class AppProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = UserProfile.objects.all()
    serializer_class = AppProfileSerializer
