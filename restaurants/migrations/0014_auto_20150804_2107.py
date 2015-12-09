# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0013_auto_20150803_1412'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menutitle',
            options={'ordering': ['mealtype', 'number']},
        ),
        migrations.AddField(
            model_name='menuitem',
            name='header',
            field=models.TextField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='menutitle',
            name='mealtype',
            field=models.CharField(max_length=120, choices=[(b'1Entrees', b'Entrees'), (b'2Sides', b'Sides'), (b'3Mains', b'Mains'), (b'4Drinks', b'Drinks'), (b'5Desserts', b'Desserts'), (b'6Specials', b'Specials'), (b'7Others', b'Others')]),
            preserve_default=True,
        ),
    ]
