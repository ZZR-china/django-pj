from .models import Article
from .models import Category
from .models import Comment
from .models import ThumbUp
from .models import UserProfile
from .models import UserGroup

from rest_framework import serializers


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Article
        fields = ('id', 'url', 'title', 'category', 'category_name', 'content', 'head_img_url', 'hidden', 'publish_date')
        extra_kwargs = {
            'url': {'view_name': 'bbs:article-detail', 'lookup_field': 'pk'},
            'category': {'view_name': 'bbs:category-detail', 'lookup_field': 'pk'},
        }


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'url', 'name', 'admin', 'article_set')
        extra_kwargs = {
            'url': {'view_name': 'bbs:category-detail', 'lookup_field': 'pk'},
            'admin': {'view_name': 'bbs:userprofile-detail', 'lookup_field': 'pk'},
            'article_set': {'view_name': 'bbs:article-detail', 'lookup_field': 'pk'},
        }


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'url', 'article', 'user', 'comment', 'parent_comment', 'date')
        extra_kwargs = {
            'url': {'view_name': 'bbs:comment-detail', 'lookup_field': 'pk'},
            'parent_comment': {'view_name': 'bbs:comment-detail', 'lookup_field': 'pk'},
            'article': {'view_name': 'bbs:article-detail', 'lookup_field': 'pk'},
            'user': {'view_name': 'bbs:userprofile-detail', 'lookup_field': 'pk'}
        }


class ThumbUpSerializer(serializers.HyperlinkedModelSerializer):
    article_title = serializers.ReadOnlyField(source='article.title')

    class Meta:
        model = ThumbUp
        fields = ('id', 'url', 'article_title', 'article', 'user', 'date')
        extra_kwargs = {
            'url': {'view_name': 'bbs:thumbup-detail', 'lookup_field': 'pk'},
            'article': {'view_name': 'bbs:article-detail', 'lookup_field': 'pk'},
            'user': {'view_name': 'bbs:userprofile-detail', 'lookup_field': 'pk'},
        }


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'url', 'union_id', 'name', 'groups')
        extra_kwargs = {
            'url': {'view_name': 'bbs:userprofile-detail', 'lookup_field': 'pk'},
            'groups': {'view_name': 'bbs:usergroup-detail', 'lookup_field': 'pk'},
        }


class UserGroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserGroup
        fields = ('id', 'url', 'name')
        extra_kwargs = {
            'url': {'view_name': 'bbs:usergroup-detail', 'lookup_field': 'pk'},
        }
