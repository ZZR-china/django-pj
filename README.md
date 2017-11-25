# 1. Intro

## How to use

/spiders/meizitu scrapy crawl meizi -o meizi.json

python manage.py

# 2. Study && Libs

## Python

[liaoxuefeng](https://www.liaoxuefeng.com/)

## Write Python with sublime

[知乎:怎么用sublime text 3搭建python 的ide？](https://www.zhihu.com/question/22904994)

[伯乐在线:Sublime Text 3设置为Python全栈开发环境](http://python.jobbole.com/81312/)

[我的有道云: py in sublime ](http://note.youdao.com/noteshare?id=87af95e3330bf39f87980ab4d1b4fba1&sub=8EAA53CA1F444886A4ACB088C961B312)

### Sublime detail

pip install pep8

安装 sublimelinter

安装 sublimelinter-pep8

[sublimelinter-pep8 - Github](https://github.com/SublimeLinter/SublimeLinter-pep8)

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

[Simple blog](http://zmrenwu.com/post/2/)

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

## 修改admin密码

Django shell：python manage.py shell

```

from django.contrib.auth.models import User

user =User.objects.get(username='admin')


user.set_password('new_password')
```

# 4. 已经完成的功能

- [x] init project

- [x] 数据库建表

- [x] 图册中图片的排序问题

- [x] scrapy解析妹子图网并生成json

- [x] django解析meizi.json将数据存储到mysql中

- [x] urllib3下载meizi图片并存储到本地

# 5. 待完成与优化

- [ ] 识别图片，找出肤色较黑的妹子
