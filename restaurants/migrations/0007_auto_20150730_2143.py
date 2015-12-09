# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_auto_20150730_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='number',
            field=models.IntegerField(default=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='menutitle',
            name='number',
            field=models.IntegerField(default=1, null=True, blank=True),
            preserve_default=True,
        ),
    ]
