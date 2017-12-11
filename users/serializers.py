from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
        extra_kwargs = {
            'url': {'view_name': 'users:user-detail', 'lookup_field': 'pk'},
            'groups': {'view_name': 'users:group-detail', 'lookup_field': 'pk'},
        }


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')
        extra_kwargs = {
            'url': {'view_name': 'users:group-detail', 'lookup_field': 'pk'},
        }
