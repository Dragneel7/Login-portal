# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0014_remove_userstats_userdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstats',
            name='userdetails',
            field=models.ForeignKey(default=0, to='login_app.UserDetails'),
            preserve_default=False,
        ),
    ]
