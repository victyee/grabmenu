# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OwnersSubmit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('restaurant_name', models.CharField(max_length=200)),
                ('street_address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('menu', models.FileField(null=True, upload_to=b'restaurant/menu/', blank=True)),
                ('website', models.CharField(max_length=350, null=True, blank=True)),
                ('owner_name', models.CharField(max_length=150)),
                ('contact_number', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.EmailField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(max_length=1000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
