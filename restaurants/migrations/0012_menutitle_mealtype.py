# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0011_auto_20150731_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='menutitle',
            name='mealtype',
            field=models.CharField(blank=True, max_length=120, null=True, choices=[(b'Breakfast', b'breakfast'), (b'Lunch', b'lunch'), (b'Dinner', b'dinner'), (b'Supper', b'supper')]),
            preserve_default=True,
        ),
    ]
