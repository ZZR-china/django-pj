import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# 图片
class Pictrue(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # 图片地址线上地址，可直接访问图片地址非本机
    url = models.CharField(max_length=200)
    # 来源网址 即解析的网址
    origin_url = models.CharField(max_length=200)
    # 本机存储地址, 路径
    local_path = models.CharField(max_length=200)
    # 图片分类 为text  (etc. 日韩,欧美)
    category_match = models.TextField()
    # 浏览量
    picview = models.IntegerField(default=0)
    # 排序
    order = models.IntegerField(default=0)
    # 发布时间
    pub_date = models.DateTimeField('date published')
    # 图片创建时间
    create_date = models.DateTimeField('date published')

class Tag(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField()
    create_date = models.DateTimeField('date published')

class PictrueTag(models.Model):
    pictrue = models.ForeignKey(Pictrue, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

# 图册
class Album(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # 图册分类 为text  (etc. 日韩,欧美)
    category_match = models.TextField()
    # 浏览量
    picview = models.IntegerField(default=0)
    # 排序
    order = models.IntegerField(default=0)
    # 发布时间
    pub_date = models.DateTimeField('date published')
    # 图册创建时间
    create_date = models.DateTimeField('date published')

class AlbumTag(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class AlbumPictrue(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    pictrue = models.ForeignKey(Pictrue, on_delete=models.CASCADE)