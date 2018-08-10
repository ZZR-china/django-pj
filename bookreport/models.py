from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    '''
    帖子表
    '''
    # 标题最大长度255,不能重名
    title = models.CharField("文章标题", max_length=150, unique=True)
    '''
    这里在admin中,title默认是显示英文的,我们可以在他的最前面加要给字段,在admin中就可以显示中文,
    他和verbose_name一样,什么时候必须使用verbose_name呢?比如上面的
    {category = models.ForeignKey("Category",verbose_name='板块名称')}
    这个字段第一个字段是关联的类,这里就必须使用verbose_name
    '''
    # 文章内容(文章内容可能有很多,所以我们就不用"CharField"来写了,我们用TextField,不用规定他多长了,为可扩展长度)
    content = models.TextField(default="内容")
    # 文章作者
    author = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    # 发布日期
    publish_date = models.DateTimeField(auto_now=True, verbose_name="发布日期")
    # 是否隐藏
    hidden = models.BooleanField(default=False, verbose_name="是否隐藏")
    # 帖子的优先级
    priority = models.IntegerField(default=1000, verbose_name="优先级")

    def __str__(self):
        return "<%s,author:%s>" % (self.title, self.author)

    class Meta:
        ordering = ('-publish_date',)
