from django.contrib import admin

# Register your models here.
from .models import Article
from .models import Category
from .models import Comment
from .models import ThumbUp
from .models import UserProfile
from .models import UserGroup


# 给某个表专门的定制的类
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'hidden', 'publish_date')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(ThumbUp)
admin.site.register(UserProfile)
admin.site.register(UserGroup)
