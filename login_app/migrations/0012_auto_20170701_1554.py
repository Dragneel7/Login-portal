# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 15:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0011_remove_userstats_userdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstats',
            name='userdetails',
            field=models.ForeignKey(default=b'north', on_delete=django.db.models.deletion.CASCADE, to='login_app.UserDetails'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='user_password',
            field=models.CharField(max_length=50, verbose_name=b'PassWord'),
        ),
        migrations.AlterField(
            model_name='userstats',
            name='user_stat',
            field=models.CharField(max_length=200),
        ),
    ]
