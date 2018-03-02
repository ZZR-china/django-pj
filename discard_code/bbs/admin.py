from django.contrib import admin

# Register your models here.
from .models import Article
from .models import Category
from .models import Comment
from .models import ThumbUp


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'hidden', 'publish_date')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'comment', 'parent_comment', 'user', 'date')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ThumbUp)
