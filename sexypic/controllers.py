from .models import Album
from .models import Picture
from .models import Snippet
from .models import Tag
from .permissions import IsOwnerOrReadOnly
from .serializers import AlbumSerializer
from .serializers import PictureSerializer
from .serializers import SnippetSerializer
from .serializers import TagSerializer
from .serializers import UserSerializer

from django.contrib.auth.models import User
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import detail_route
from rest_framework.response import Response


class AlbumViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    @detail_route()
    def tags(self, request, pk=None):
        """
        Returns a list of all the picture that the given
        tag belongs to.
        """
        album = self.get_object()
        tags = album.albumtag.all()
        return Response([tag.title for tag in tags])


class PictureViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    @detail_route()
    def tags(self, request, pk=None):
        """
        Returns a list of all the picture that the given
        tag belongs to.
        """
        picture = self.get_object()
        tags = picture.pictag.all()
        return Response([tag.title for tag in tags])


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @detail_route()
    def picture(self, request, pk=None):
        """
        Returns a list of all the picture that the given
        tag belongs to.
        """
        tag = self.get_object()
        pictures = tag.picture_set.all()
        return Response([{
            'id': picture.pk,
            'title': picture.title,
            'create_date': picture.create_date,
            'picview': picture.picview,
            'tags': picture.tags,
            'description': picture.description,
            'static_path': picture.__path__(),
        } for picture in pictures])


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
