from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'blogs/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return ''

def pdf(request):
      return HttpResponse('1234dfsdf')

def add(request):
			a = request.GET['a']
			b = request.GET['b']
			c = int(a) + int(b)
			return HttpResponse(str(c))