from django.contrib import admin

# Register your models here.
from .models import Article
from .models import Category
from .models import Comment
from .models import ThumbUp
from .models import UserProfile
from .models import UserGroup


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'hidden', 'publish_date')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'comment', 'parent_comment', 'user', 'date')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ThumbUp)
admin.site.register(UserProfile)
admin.site.register(UserGroup)
