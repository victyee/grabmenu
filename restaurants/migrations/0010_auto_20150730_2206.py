# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_auto_20150730_2150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['number']},
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='number',
            field=models.IntegerField(default=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_state',
            field=models.CharField(max_length=120, choices=[(b'Victoria', b'Victoria'), (b'New South Wales', b'New South Wales'), (b'South Australia', b'South Australia'), (b'Queensland', b'Queensland'), (b'Western Australia', b'Western Australia'), (b'Australian Capital Territory', b'Australian Capital Territory'), (b'Northern Territory', b'Northern Territory'), (b'Tasmania', b'Tasmania')]),
            preserve_default=True,
        ),
    ]
