# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-12 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Common', '0002_auto_20181211_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='m_price',
            field=models.IntegerField(default=0),
        ),
    ]
