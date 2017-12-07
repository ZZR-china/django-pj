from django.contrib import admin

# Register your models here.
from .models import Picture
from .models import Album
from .models import Tag


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'picview')


class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'local_path', 'pub_date', 'picview')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'create_date')

admin.site.register(Album, AlbumAdmin)

admin.site.register(Picture, PictureAdmin)

admin.site.register(Tag, TagAdmin)
