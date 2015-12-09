# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_auto_20150730_2143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menutitle',
            options={'ordering': ['number']},
        ),
    ]
