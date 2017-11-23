# -*-coding:utf-8 -*-

from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

import datetime
import json
import os
import random
import time
import urllib3

from .models import Pictrue, Album, Tag

__dirPath__ = os.path.dirname(os.path.realpath(__file__))


class IndexView(generic.ListView):
    template_name = 'sexypic/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        print(self)
        return ''

# 解析meizi.json


def meizi(request):
    def getPreview():
        return int(random.randint(9999, 99999))

    def handleSingleLine(record):

        def dateDeal(str):
            t = time.strptime(str, "%Y-%m-%d")
            y, m, d = t[0:3]
            return datetime.datetime(y, m, d)

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
        album, created = Album.objects.get_or_create(
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
        for index, img in enumerate(imgslist):
            pictrue, created = Pictrue.objects.get_or_create(
                title=img.get('title', ''),
                origin_url=img.get('src', ''),
                description=description,
                order=index,
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

    requestData = request.GET.copy()
    isDone = requestData['done']
    if isDone != '1':
        return HttpResponse(u'need done params')

    dirPath = os.path.dirname(os.path.realpath(__file__))
    meiziJsonPath = str(dirPath) + '\datas\meizi_small.json'
    # meiziJsonPath = str(dirPath) + '\datas\meizi.json'
    meiziData = open(meiziJsonPath, encoding='utf-8')
    dicList = []
    for line in meiziData:
        if line != ']' and line != '[':
            line = line.strip()
            if line.endswith(','):
                pointCount = line.rfind(',')
                line = line[:pointCount]
                line = json.loads(line)
                dicList.append(line)
            else:
                pass
        else:
            pass
    for item in dicList:
        print(item)
        handleSingleLine(item)
    return HttpResponse(u'start')


class PicView(generic.ListView):
    template_name = 'sexypic/pic.html'
    context_object_name = 'pictrues'

    def get_queryset(self):
        pictrues = Pictrue.objects.filter(
            pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        return pictrues


def pictruedownload(request):

    def mkdir(path):
        path = path.strip()
        path = path.rstrip("\\")
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            print(path+' 创建成功')
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(path+' 目录已存在')
            return False

    def requestPic(url, paths):
        try:
            http = urllib3.PoolManager()
            pic = http.request('GET', url)
        except http.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
        mkdir(paths['dirpath'])
        # resolve the problem of encode, make sure that chinese name could be
        # store
        fp = open(paths['imgpath'], 'wb')
        fp.write(pic.data)
        fp.close()

    def getPath(pic_id, url, timestr):
        year = str(timestr.year)
        month = str(timestr.month)
        day = str(timestr.day)
        dirpath = str(__dirPath__) + '\static\sexypic\images\meizi\\' + year + \
            '\\' + month + '\\' + day + '\\'
        imgpath = dirpath + str(pic_id) + '.' + getImgType(url)
        return {
            u'dirpath': dirpath,
            u'imgpath': imgpath
        }

    def getImgType(url):
        imgType = url.split('.')[-1]
        return imgType

    def downloadPic(pic_id, url, timestr):
        paths = getPath(pic_id, url, timestr)
        print(url)
        requestPic(url, paths)

    pictrues = Pictrue.objects.filter(
        pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

    for pictrue in pictrues:
        pic_id = pictrue.id
        url = pictrue.origin_url
        timestr = pictrue.pub_date
        downloadPic(pic_id, url, timestr)

    return HttpResponse(u'start download pic')
