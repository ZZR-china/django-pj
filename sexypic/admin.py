from django.contrib import admin

# Register your models here.
from .models import Picture
from .models import Album

admin.site.register(Album)

admin.site.register(Picture)