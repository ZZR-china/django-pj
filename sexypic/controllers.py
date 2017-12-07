from .serializers import SnippetSerializer
from .serializers import UserSerializer
from .models import Snippet

from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import generics
from rest_framework.decorators import permission_classes


@permission_classes((permissions.AllowAny,))
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


@permission_classes((permissions.AllowAny,))
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
