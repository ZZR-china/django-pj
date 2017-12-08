from .models import Album
from .models import Picture
from .models import Snippet
from .models import Tag

from django.contrib.auth.models import User
from rest_framework import serializers


class AlbumSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'url', 'title', 'description', 'pub_date', 'tags', 'picview', 'pub_date', 'albumtag', 'pic')
        extra_kwargs = {
            'url': {'view_name': 'sexypic:album-detail', 'lookup_field': 'pk'},
            'albumtag': {'view_name': 'sexypic:tag-detail', 'lookup_field': 'pk'},
            'pic': {'view_name': 'sexypic:picture-detail', 'lookup_field': 'pk'},
        }


class PictureSerializer(serializers.HyperlinkedModelSerializer):
    api_url = serializers.HyperlinkedIdentityField(
        view_name='sexypic:picture-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Picture
        fields = ('id', 'title', 'api_url', 'local_path', 'static_path', 'tags', 'picview', 'pub_date', 'pictag')
        extra_kwargs = {
            'pictag': {'view_name': 'sexypic:tag-picture', 'lookup_field': 'pk'}
        }


class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'url', 'title', 'order', 'create_date', 'album_set', 'picture_set')
        extra_kwargs = {
            'url': {'view_name': 'sexypic:tag-detail', 'lookup_field': 'pk'},
            'album_set': {'view_name': 'sexypic:album-detail', 'lookup_field': 'pk'},
            'picture_set': {'view_name': 'sexypic:picture-detail', 'lookup_field': 'pk'},
        }


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='sexypic:snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('id', 'url', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')
        extra_kwargs = {
            'url': {'view_name': 'sexypic:snippet-detail', 'lookup_field': 'pk'}
        }


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='sexypic:snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'snippets')
        extra_kwargs = {
            'url': {'view_name': 'sexypic:user-detail', 'lookup_field': 'pk'}
        }
