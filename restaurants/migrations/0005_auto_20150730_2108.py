# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20150730_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_state',
            field=models.CharField(max_length=120, choices=[(b'VIC', b'Victoria'), (b'NSW', b'New South Wales'), (b'SA', b'South Australia'), (b'QLD', b'Queensland'), (b'WA', b'Western Australia'), (b'ACT', b'Australian Capital Territory'), (b'NT', b'Northern Territory'), (b'TAS', b'Tasmania')]),
            preserve_default=True,
        ),
    ]
