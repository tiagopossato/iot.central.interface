# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0004_auto_20170618_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mqtt',
            name='status',
            field=models.IntegerField(choices=[(1, 'Small'), (2, 'Medium'), (3, 'Large')], verbose_name='Estado da comunicação'),
        ),
    ]