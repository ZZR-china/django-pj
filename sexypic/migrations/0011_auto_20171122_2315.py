# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sexypic', '0010_auto_20171122_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumpictrue',
            name='album',
        ),
        migrations.RemoveField(
            model_name='albumpictrue',
            name='pictrue',
        ),
        migrations.RemoveField(
            model_name='albumtag',
            name='album',
        ),
        migrations.RemoveField(
            model_name='albumtag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='pictruetag',
            name='pictrue',
        ),
        migrations.RemoveField(
            model_name='pictruetag',
            name='tag',
        ),
        migrations.AddField(
            model_name='album',
            name='albumtag',
            field=models.ManyToManyField(to='sexypic.Tag'),
        ),
        migrations.AddField(
            model_name='album',
            name='pic',
            field=models.ManyToManyField(to='sexypic.Pictrue'),
        ),
        migrations.AddField(
            model_name='pictrue',
            name='pictag',
            field=models.ManyToManyField(to='sexypic.Tag'),
        ),
        migrations.DeleteModel(
            name='AlbumPictrue',
        ),
        migrations.DeleteModel(
            name='AlbumTag',
        ),
        migrations.DeleteModel(
            name='PictrueTag',
        ),
    ]