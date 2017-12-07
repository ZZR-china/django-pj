import datetime

from django.db import models
from django.utils import timezone


from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers
from pygments.lexers import get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.

# 图片


class Picture(models.Model):
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

    def __str__(self):
        return self.title

    static_path = __path__


class Tag(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


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
    pic = models.ManyToManyField('Picture')

    def __str__(self):
        return self.title


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(
        choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)
