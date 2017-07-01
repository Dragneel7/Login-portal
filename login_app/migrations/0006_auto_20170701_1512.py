# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0005_auto_20170701_0631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstats',
            name='user',
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='user_name',
            field=models.CharField(max_length=100, verbose_name=b'UserName'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='user_password',
            field=models.CharField(max_length=50, verbose_name=b'PassWord'),
        ),
        migrations.DeleteModel(
            name='UserStats',
        ),
    ]
