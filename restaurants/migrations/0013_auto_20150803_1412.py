# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0012_menutitle_mealtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menutitle',
            name='mealtype',
            field=models.CharField(default=1, max_length=120, choices=[(b'Entrees', b'Entrees'), (b'Sides', b'Sides'), (b'Mains', b'Mains'), (b'Drinks', b'Drinks'), (b'Desserts', b'Desserts'), (b'Specials', b'Specials'), (b'Others', b'Others')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menutitle',
            name='title',
            field=models.CharField(max_length=120, null=True, blank=True),
            preserve_default=True,
        ),
    ]
