# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0013_auto_20170702_0738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstats',
            name='userdetails',
        ),
    ]
