# coding: utf-8

from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Article


class IndexView(ListView):
    model = Article
    template_name = 'bbs/index.html'
    context_object_name = 'article_list'
