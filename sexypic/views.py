from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

import os
import json

from .models import Pictrue, Album, Tag, PictrueTag, AlbumPictrue, AlbumTag

class IndexView(generic.ListView):
    template_name = 'sexypic/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return ''

def meizi(request):
	  dirPath = os.path.dirname(os.path.realpath(__file__))
	  meiziJsonPath = str(dirPath) + '\datas\meizi.json'
	  print(meiziJsonPath)
	  meiziData = open(meiziJsonPath, encoding='utf-8')
	  # print(meiziData)
	  dicList= []
	  for line in meiziData:
	  	try:
	  		line = json.load(line)
	  	except Exception as e:
	  		print(e)
	  	else:
	  	  dicList.append(line)
	  # dicList = [json.loads(line) for line in meiziData]
	  # print(type(dicList))
	  # print(dicList[0])
	  return HttpResponse(u'type(dicList)')
