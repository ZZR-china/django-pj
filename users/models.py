from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your models here.


class UserProfile(models.Model):
    '''
    用户信息表，是对系统 auth user表的补充
    '''
    # 使用Django提供的用户表,直接继承就可以了.在原生的User表里扩展!(原生的User表里就有用户名和密码)
    # 一定要使用OneToOne,如果是正常的ForeignKey的话就表示User中的记录可以对应UserProfile中的多条记录!
    # 并且OneToOne的实现不是在SQL级别实现的而是在代码基本实现的!
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 昵称
    nickname = models.CharField(max_length=32, blank=False, unique=True)
    # 性别 0 女性 1男性 2未知
    sex = models.IntegerField(default=1, verbose_name="性别")
    # 微信UnionID
    union_id = models.CharField(max_length=150, blank=False)
    # 手机号
    mobile = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.nickname

    def user_email(self):
        user = self.user
        return str(user.email)

    def user_name(self):
        user = self.user
        return str(user.name)
