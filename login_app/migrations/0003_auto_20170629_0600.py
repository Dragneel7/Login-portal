# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_userstats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstats',
            name='user_stat',
            field=models.ForeignKey(to='login_app.UserDetails'),
        ),
    ]
