# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20171018_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='community',
            field=models.URLField(default='abc'),
            preserve_default=False,
        ),
    ]
