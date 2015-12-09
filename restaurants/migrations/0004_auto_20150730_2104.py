# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20150730_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_state',
            field=models.CharField(max_length=120, choices=[(b'VIC', b'victoria'), (b'NSW', b'new south wales'), (b'SA', b'south australia'), (b'QLD', b'queensland'), (b'WA', b'western australia'), (b'ACT', b'australian capital territory'), (b'NT', b'northern territory'), (b'TAS', b'tasmania')]),
            preserve_default=True,
        ),
    ]
