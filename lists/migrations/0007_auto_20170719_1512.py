# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-19 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_auto_20170719_1508'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([]),
        ),
    ]