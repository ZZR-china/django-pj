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
    # 服务器存储地址, 路径 like: /imgs/meizi/2017/06/10/01.jpg
    local_path = models.CharField(max_length=200)
    # 图片在七牛CDN上的路径
    qiniu_url = models.CharField(max_length=200, default='')
    # 图片分类 为text  (etc. 日韩,欧美)
    tags = models.TextField(default='')
    # 浏览量
    picview = models.IntegerField(default=0)
    # 排序
    order = models.IntegerField(default=0)
    # 发布时间
    pub_date = models.DateTimeField('date published')
    # 图片创建时间
    create_date = models.DateTimeField(auto_now_add=True)
    pictag = models.ManyToManyField('Tag')

    def __path__(self):
        path = self.local_path
        path = path.replace('\\', '/')
        return 'sexypic/images' + path

    static_path = __path__

class Tag(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)

# 图册
class Album(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # 图册分类 为text  (etc. 日韩,欧美)
    tags = models.TextField(default='')
    # 浏览量
    picview = models.IntegerField(default=0)
    # 排序
    order = models.IntegerField(default=0)
    # 发布时间
    pub_date = models.DateTimeField('date published')
    # 图册创建时间
    create_date = models.DateTimeField(auto_now_add=True)
    albumtag = models.ManyToManyField('Tag')
    pic = models.ManyToManyField('Pictrue')
