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

- [ ] 论坛添加版块管理员、普通会员两个角色

- [ ] 普通会员只能修改自己的帖子和评论

- [ ] 使用 rest_framework的Throttling特性来控制client的访问频率。

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

# 8. 一些反思

## 1) rest_framework与django自身帐号权限系统的混用

rest_framework与django都有一套控制权限的套路，看你希望实现的功能来各取所需。首先django的admin后台很强大，我们希望系统管理者和项目app的管理者都能登录其中对数据进行直接的管理。而项目app的使用者也就是普通用户不能登录后台，只能使用前台产品进行产品的操作，进行数据的产生和自身数据的操作。

User的话使用django自身的auth_user这张表，同时使用django对user附带的permission和group等一套用户系统。项目app在需要在user表中添加时使用

```
user = models.OneToOneField(User, on_delete=models.CASCADE)
```

的方式创建自身的user表，进行字段的添加关联，group表也是。

权限方面django自带的permission功能已经很强大充分，可以直接使用，需要扩充的话django和rest_framework官网也有详细的说明。

## 2) 纯api输出后台需要考虑的地方

几经思索，最新的论坛项目还是采用了后台纯api输出，前端使用react搭建页面的模式进行开发。虽然会增加一些工作量，但是考虑到系统的可拓展性、架构的可读性、后期人员的协调与分工等，这样的搭配我个人还是很满意的，不满意的话。you can say a fuck to me and I'll accept with a smile face and my middle finger。

目前后台已经初步完成，从安全性、可拓展性、可维护性、可读性、性能五个方面来总结下。

#### 安全性

使用jwt对每一个需要权限认证的api进行了安全认证，而且目前只允许.mingz-tech.com下的请求进去controller层，其他的在中间件中就已经过滤掉。

（系统安全性还需更多防护）

#### 可拓展性

django的可拓展性在所有框架中是我见过最好的。（我用过的框架有express、hapi、koa、flask、thinkphp）虽然轻量性不够，但是框架在系统层面就定制好了许多可拓展的模块与方法。从他本身的startapp这个命令将所有小项目当做一个可打包发布的app来看待就可以看出。django的设计者是希望使用者们进行模块化的开发的。

我遵从rest_framework的教程创建 serializers.py来序列化需要api展示的参数， controllers.py中定义每个api的viewset，urls.py中使用rf（rest_framework的简写，下同）的DefaultRouter()封装viewset并使用path定义成url。最后在项目级的urls中引入app的url，是他可以访问。

#### 可维护性

代码使用pep8规则，功能尽量模块化。

#### 可读性

python的可读性在各个语言中是顶尖的，往往只是看单词的本意就能推测出代码的意思。django中更是如此。

#### 性能

python的性能一直为人诟病，后期可以使用Cpython来进行优化。

rf使用他的Throttling特性来控制client的访问频率。
