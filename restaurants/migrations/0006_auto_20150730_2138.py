# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20150730_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='number',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menutitle',
            name='number',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
