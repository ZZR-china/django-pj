from .models import UserProfile

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework import serializers


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    # view_name 中参数是model的名字！
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')
        extra_kwargs = {
            'url': {'view_name': 'users:user-detail', 'lookup_field': 'pk'},
            'groups': {'view_name': 'users:group-detail', 'lookup_field': 'pk'},
        }


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'url', 'name')
        extra_kwargs = {
            'url': {'view_name': 'users:group-detail', 'lookup_field': 'pk'},
        }


class AppProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'url', 'user', 'user_email', 'union_id', 'nickname', 'mobile')
        extra_kwargs = {
            'url': {'view_name': 'users:userprofile-detail', 'lookup_field': 'pk'},
            'user': {'view_name': 'users:user-detail', 'lookup_field': 'pk'},
        }
