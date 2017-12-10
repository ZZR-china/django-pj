# 1. Intro

## How to use

/spiders/meizitu scrapy crawl meizi -o meizi.json

python manage.py

## 项目架构

cross-ai-
		ai-
		bbs-
		blog-
		comments-
		ENV-
		patchapps-
		polls-
		sexpic-
		shells-
		spiders-
		templates-
		uploads-
		xmind-

# 2. Study && Libs

## Python

[liaoxuefeng](https://www.liaoxuefeng.com/)

## Write Python with sublime

[知乎:怎么用sublime text 3搭建python 的ide？](https://www.zhihu.com/question/22904994)

[伯乐在线:Sublime Text 3设置为Python全栈开发环境](http://python.jobbole.com/81312/)

[我的有道云: py in sublime ](http://note.youdao.com/noteshare?id=87af95e3330bf39f87980ab4d1b4fba1&sub=8EAA53CA1F444886A4ACB088C961B312)

### Sublime detail

pip install pep8

sublime 安装 sublimelinter

sublime 安装 [sublimelinter-pep8](https://github.com/SublimeLinter/SublimeLinter-pep8)

sublime 安装 autopep8

## Tensorflow

[tensorflow - Github](https://github.com/tensorflow/tensorflow)

[tensorflow - 官方网站](http://www.tensorflow.org/)

[tensorflow - 中文社区](http://www.tensorfly.cn)

[TensorFlow - 官方文档中文版--极客学院](http://wiki.jikexueyuan.com/project/tensorflow-zh/)

## Django

[Django官网](https://docs.djangoproject.com/en/1.11/)

[django-rest-framework Github](https://github.com/encode/django-rest-framework)

[django-rest-framework Website](http://www.django-rest-framework.org)

[自强学堂](http://code.ziqiangxuetang.com/django/django-tutorial.html)

[Simple blog - Github](https://github.com/zmrenwu/django-blog-tutorial)

[Simple blog - Website](http://zmrenwu.com/post/2/)

## Django django-rest-framework

[django-rest-framework Github](https://github.com/encode/django-rest-framework)

[django-rest-framework Website](http://www.django-rest-framework.org)

easy and simple, powerful

## Scrapy

[scrapy - Github](https://github.com/scrapy/scrapy)

[scrapy - Website](https://scrapy.org/)

## Pillow

[Pillow - Github](https://github.com/python-pillow/Pillow)

## Celery

[Celery - Github](https://github.com/celery/celery)

[Celery - 分布式任务队列 Website](http://docs.jinkan.org/docs/celery/index.html)

# 3. 项目一些配置

## Mysql 链接库使用 pymysql

pip install pymysql

**django __init__.py中做如下配置**
```

import pymysql

pymysql.install_as_MySQLdb()

```

2.0后使用mysqlclient，pymysql版本太低

## 修改admin密码

Django shell：python manage.py shell

```

from django.contrib.auth.models import User

user =User.objects.get(username='admin')


user.set_password('new_password')
```

# 4. 前端配置


## bulma

[bulma - Github](https://github.com/jgthms/bulma)

[bulma - Website](https://bulma.io/)

# 5. 已经完成的功能

- [x] init project

- [x] 数据库建表

- [x] 图册中图片的排序问题

- [x] scrapy解析妹子图网并生成json

- [x] django解析meizi.json将数据存储到mysql中

- [x] urllib3下载meizi图片并存储到本地

- [x] django-rest-framework将数据以api形式输出

- [x] django-rest-framework添加模糊查询

- [x] django-rest-framework添加聚合查询

# 6. 待完成与优化

- [ ] 识别图片，找出肤色较黑的妹子

- [ ] django-rest-framework添加权限检查

# 7. BUGS&&ImportantThings

## 1). django-rest-framework创建hylink时错误  (耗时-1小时)

教程中直接在serializers.py class SnippetSerializer下添加url，并将继承类改为HyperlinkedModelSerializer，但是总是报错，然而UserSerializer类却不会。报的错误类型为ImproperlyConfigured--错误的配置类型。

后来在github上看到一个人回复在[guide](http://www.django-rest-framework.org/api-guide/serializers/#how-hyperlinked-views-are-determined)中看看，查看中发现class Meta中添加extra_kwargs 配置也可以添加hylink url。之后错误解决。

```

class Meta:
      model = Snippet
      fields = ('url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')
      extra_kwargs = {
          'url': {'view_name': 'sexypic:snippet-detail', 'lookup_field': 'pk'}
      }

```

总结: 有些事直接上github的issues中看，更能得到解决办法。

## 2) django-rest-framework添加模糊查询无法导入SearchFilter  （耗时-30分钟）

教程中直接引入了SearchFilter,但是django_filters中并没有，后来看[rest_framework_word_filter](https://github.com/trollknurr/django-rest-framework-word-search-filter)中，filter.py 源代码里写到

```
from django.db import models
from django.utils.six.moves import reduce
from rest_framework.filters import BaseFilterBackend
from rest_framework.settings import api_settings
```

得知，rest_framework中也是有filters子类的可以直接导入,添加

```
from rest_framework.filters import SearchFilter
```
成功。

总结：自己太蠢，应该想到既然是rest_framework的教程，django_filters中没有，当然是从rest_framework里导入。而且也应该多看看源码。起码知道框架中包含了哪些主要类、方法。
