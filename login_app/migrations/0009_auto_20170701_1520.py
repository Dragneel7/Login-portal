# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0008_auto_20170701_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='user_name',
            field=models.CharField(default=0, max_length=100, verbose_name=b'UserName'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='user_password',
            field=models.CharField(default=0, max_length=50, verbose_name=b'PassWord'),
        ),
    ]