# Generated by Django 2.0 on 2018-03-02 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookreport', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='user',
        ),
    ]
