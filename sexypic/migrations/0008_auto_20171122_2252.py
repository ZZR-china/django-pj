# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sexypic', '0007_auto_20171122_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pictrue',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
