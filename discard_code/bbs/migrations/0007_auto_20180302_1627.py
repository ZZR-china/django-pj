# Generated by Django 2.0 on 2018-03-02 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0006_auto_20180302_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile', verbose_name='作者'),
        ),
    ]