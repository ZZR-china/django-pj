from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'sexypic/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return ''
