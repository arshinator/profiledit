# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 03:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_thing_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thing',
            old_name='description',
            new_name='pan',
        ),
    ]
