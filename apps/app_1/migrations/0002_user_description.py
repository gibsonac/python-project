# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-24 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(default='Add a description about yourself'),
            preserve_default=False,
        ),
    ]
