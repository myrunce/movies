# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-27 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0005_auto_20170727_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='showtime',
            field=models.DateField(),
        ),
    ]
