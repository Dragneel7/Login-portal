# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0012_auto_20170701_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstats',
            name='userdetails',
            field=models.ForeignKey(to='login_app.UserDetails'),
        ),
    ]
