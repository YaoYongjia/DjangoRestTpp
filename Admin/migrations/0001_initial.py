# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-11 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_username', models.CharField(max_length=16, unique=True)),
                ('a_password', models.CharField(max_length=256)),
                ('is_delete', models.BooleanField(default=False)),
                ('is_super', models.BooleanField(default=False)),
            ],
        ),
    ]
