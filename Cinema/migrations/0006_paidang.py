# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-13 11:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Common', '0003_movie_m_price'),
        ('Cinema', '0005_hall'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaiDang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_time', models.DateTimeField(default='2018-12-13 00:00:00')),
                ('p_price', models.FloatField(default=35)),
                ('p_cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cinema.Cinema')),
                ('p_hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cinema.Hall')),
                ('p_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Common.Movie')),
            ],
        ),
    ]