# Generated by Django 2.0 on 2017-12-08 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sexypic', '0004_tag_pictures'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='pictures',
        ),
    ]
