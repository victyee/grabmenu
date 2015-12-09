# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0014_auto_20150804_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menutitle',
            name='mealtype',
            field=models.CharField(max_length=120, choices=[(b'1Entrees', b'Entrees'), (b'2Sides', b'Sides'), (b'3Mains', b'Mains'), (b'4Drinks', b'Drinks'), (b'5Desserts', b'Desserts'), (b'6Specials', b'Specials'), (b'7Others', b'Others'), (b'8Lunch', b'Lunch')]),
            preserve_default=True,
        ),
    ]
