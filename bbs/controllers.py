from .models import Article
from .models import Category
from .models import Comment
from .models import ThumbUp
from .models import UserProfile
from .models import UserGroup

from .serializers import ArticleSerializer
from .serializers import CategorySerializer
from .serializers import CommentSerializer
from .serializers import ThumbUpSerializer
from .serializers import UserProfileSerializer
from .serializers import UserGroupSerializer

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from django_filters import rest_framework as filters


class ArticleViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filter_fields = ('title', 'content')
    search_fields = ('title', 'content')


class CategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @detail_route()
    def article(self, request, pk=None):
        category = self.get_object()
        articles = category.article_set.all()
        return Response([article.title for article in articles])


class CommentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ThumbUpViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = ThumbUp.objects.all()
    serializer_class = ThumbUpSerializer

@permission_classes((AllowAny, ))
class UserProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserGroupViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer
