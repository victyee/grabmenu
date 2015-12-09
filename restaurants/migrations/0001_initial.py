# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000, null=True, blank=True)),
                ('price', models.CharField(max_length=20, null=True, blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=250)),
                ('restaurant_name', models.CharField(max_length=250)),
                ('restaurant_address1', models.CharField(max_length=250)),
                ('restaurant_address2', models.CharField(max_length=250)),
                ('restaurant_state', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='menutitle',
            name='restaurant',
            field=models.ForeignKey(to='restaurants.Restaurant'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='title',
            field=models.ForeignKey(to='restaurants.MenuTitle'),
            preserve_default=True,
        ),
    ]
