# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_auto_20170629_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstats',
            name='userdetails',
            field=models.ForeignKey(default='null', to='login_app.UserDetails'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userstats',
            name='user_stat',
            field=models.CharField(max_length=200),
        ),
    ]
