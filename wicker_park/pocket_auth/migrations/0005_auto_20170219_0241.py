# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-19 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pocket_auth', '0004_auto_20170219_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pocketitem',
            name='given_url',
            field=models.URLField(max_length=4096),
        ),
        migrations.AlterField(
            model_name='pocketitem',
            name='resolved_url',
            field=models.URLField(max_length=4096),
        ),
    ]