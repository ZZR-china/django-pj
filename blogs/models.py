import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
