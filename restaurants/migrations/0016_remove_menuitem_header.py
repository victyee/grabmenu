# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0015_auto_20150804_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='header',
        ),
    ]
