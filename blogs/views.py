from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'homedata'

    def get_queryset(self):
        """Return the last five published questions."""
        List = map(str, range(100))# 一个长度为100的 List
        return {
          'TutorialList': ["HTML", "CSS", "jQuery", "Python", "Django"],
          'site': u'自强学堂', 
          'content': u'各种IT技术教程',
          'List': List
        }

def pdf(request):
      return HttpResponse('1234dfsdf')

def add(request):
			a = request.GET['a']
			b = request.GET['b']
			c = int(a) + int(b)
			return HttpResponse(str(c))