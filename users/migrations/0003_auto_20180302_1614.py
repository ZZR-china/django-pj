# Generated by Django 2.0 on 2018-03-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180302_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usergroup',
            name='group',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='nickname',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='groups',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sex',
            field=models.IntegerField(default=1, verbose_name='性别'),
        ),
        migrations.DeleteModel(
            name='UserGroup',
        ),
    ]
