# -*-coding:utf-8 -*-

import datetime
import json
import os
import random
import time
import urllib3

from django.http import HttpResponse
from django.utils import timezone
from django.views import generic


from .models import Album
from .models import Picture
from .models import Tag

__dirPath__ = os.path.dirname(os.path.realpath(__file__))


class IndexView(generic.ListView):
    template_name = 'sexypic/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
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
        pub_date = dateDeal(record['time'])
        title = record['title']
        print('title---' + title)
        tags = record['tags']
        tags = tagsDeal(tags)
        print('tags---' + tags)
        print('------ album save ------')
        album = handleAlbum(title, tags, pub_date)
        print(type(album))
        print(album)
        imgslist = record['imgslist']
        print('------ pictrues save ------')
        pictrues = handlePictures(imgslist, tags, title, pub_date, album)
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

    def handlePictures(imgslist, tags, description, pub_date, album_id):
        pictures_id = []
        for index, img in enumerate(imgslist):
            picture, created = Picture.objects.get_or_create(
                title=img.get('title', ''),
                origin_url=img.get('src', ''),
                description=description,
                order=index,
                tags=tags,
                pub_date=pub_date
            )
            picture.picview = getPreview()
            picture.save()
            album = Album.objects.get(id=album_id)
            album.pic.add(picture)
            pictures_id.append(picture.id)
        return pictures_id

    def handleTags(tags, album_id, pictures_id):
        def manyToAlbum(tag, album_id):
            album = Album.objects.get(id=album_id)
            album.albumtag.add(tag)

        def manyToPicture(tag, pictures_id):
            for picture_id in pictures_id:
                picture = Picture.objects.get(id=picture_id)
                picture.pictag.add(tag)

        tags = tags.split(',')
        tag_ids = []
        for tag in tags:
            obj, created = Tag.objects.get_or_create(title=tag)
            manyToAlbum(obj, album_id)
            manyToPicture(obj, pictures_id)
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
    context_object_name = 'pictures'

    def get_queryset(self):
        pictures = Picture.objects.filter(
            pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        return pictures


def picturedownload(request):

    def mkdir(path):
        path = path.strip()
        path = path.rstrip("\\")
        # 判断路径是否存在
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
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
            print('[错误]当前图片无法下载')
        mkdir(paths['dirpath'])
        # resolve the problem of encode, make sure that chinese name could be
        # store
        fp = open(paths['imgpath'], 'wb')
        picData = pic.data
        if not picData:
            return False
        else:
            fp.write(picData)
            fp.close()
            return paths['imgpath']

    def getPath(pic_id, url, timestr):
        year = str(timestr.year)
        month = str(timestr.month)
        day = str(timestr.day)
        dirpath = (str(__dirPath__) + '\static\sexypic\images\meizi\\' + year +
                   '\\' + month + '\\' + day + '\\')
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
        return requestPic(url, paths)

    pictures = Picture.objects.all()

    for picture in pictures:
        pic_id = picture.id
        print('----- picture id is ' + str(pic_id) + '------')
        url = picture.origin_url
        timestr = picture.pub_date
        res = downloadPic(pic_id, url, timestr)
        passPart = str(__dirPath__) + '\static\sexypic\images'
        res = res.split(passPart)[-1]
        picture.local_path = res
        picture.save()

    return HttpResponse(u'start download pic')
