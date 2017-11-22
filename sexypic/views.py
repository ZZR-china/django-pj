from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

import os
import json
import time, datetime
import random

from .models import Pictrue, Album, Tag

class IndexView(generic.ListView):
    template_name = 'sexypic/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return ''

def meizi(request):
		def getPreview():
			return int(random.randint(9999,99999))

		def handleSingleLine(record):

			def dateDeal(str):
				t = time.strptime(str, "%Y-%m-%d")
				y,m,d = t[0:3]
				return datetime.datetime(y,m,d)

			def tagsDeal(tags):
				tags = tags.split('Tags:')[-1].replace(' ', '')
				return tags[:tags.rfind(',')]

			
			print('---- in handleSingleLine ------')
			print(type(record))
			# 2017-10-01
			pub_date = dateDeal(record['time'])
			print(pub_date)
			# 性感美女11
			title = record['title']
			print('title---' + title)
			# "Tags:\u5199\u771f , \u6c14\u8d28 , \u7f8e\u5973 , \u8f66\u6a21 , \u6a21\u7279 "
			tags = record['tags']
			tags = tagsDeal(tags)
			print('tags---' + tags)
			print('------ album save ------')
			album = handleAlbum(title, tags, pub_date)
			print(type(album))
			print(album)
			imgslist = record['imgslist']
			print('------ pictrues save ------')
			pictrues = handlePictrues(imgslist, tags, title, pub_date, album)
			print(type(pictrues))
			print(pictrues)
			print('------ tags save ------')
			tags = handleTags(tags, album, pictrues)
			print(type(tags))
			print(tags)

		def handleAlbum(title, tags, pub_date):
			album,created = Album.objects.get_or_create(
				title=title,
				description=title,
				tags=tags,
				pub_date=pub_date
			)
			album.picview = getPreview()
			album.save()
			return album.id

		def handlePictrues(imgslist, tags, description, pub_date, album_id):
			pictrues_id = []
			for img in imgslist:
				pictrue,created = Pictrue.objects.get_or_create(
					title=img.get('title', ''),
					origin_url=img.get('src', ''),
					description=description,
					tags=tags,
					pub_date=pub_date
				)
				pictrue.picview = getPreview()
				pictrue.save()
				album = Album.objects.get(id=album_id)
				album.pic.add(pictrue)
				pictrues_id.append(pictrue.id)
			return pictrues_id

		def handleTags(tags, album_id, pictrues_id):
			def manyToAlbum(tag, album_id):
				album = Album.objects.get(id=album_id)
				album.albumtag.add(tag)

			def manyToPictrue(tag, pictrues_id):
				for pictrue_id in pictrues_id:
					pictrue = Pictrue.objects.get(id=pictrue_id)
					pictrue.pictag.add(tag)

			tags = tags.split(',')
			tag_ids = []
			for tag in tags:
				obj, created = Tag.objects.get_or_create(title=tag)
				manyToAlbum(obj, album_id)
				manyToPictrue(obj, pictrues_id)
				tag_ids.append(obj.id)
			return tag_ids

		dirPath = os.path.dirname(os.path.realpath(__file__))
		meiziJsonPath = str(dirPath) + '\datas\meizi.json'
		meiziData = open(meiziJsonPath, encoding='utf-8')
		dicList= []
		for line in meiziData:
				if line != ']' and line != '[':
					line = line.strip()
					if line.endswith(','):
						pointCount =  line.rfind(',')
						line = line[:pointCount]
						line = json.loads(line)
						dicList.append(line)
					else:
						pass
				else:
					pass
		# print(dicList[0])
		for item in dicList:
			print(item)
			handleSingleLine(item)
		return HttpResponse(u'start')
