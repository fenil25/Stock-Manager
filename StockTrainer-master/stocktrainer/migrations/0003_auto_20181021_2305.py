# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocktrainer', '0002_crypto_current_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='current_price',
            field=models.BigIntegerField(default=0),
        ),
    ]
