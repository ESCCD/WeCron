# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-02-25 14:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remind', '0009_auto_20180225_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remind',
            name='repeat',
        ),
        migrations.RenameField(
            model_name='remind',
            old_name='repeat2',
            new_name='repeat',
        ),
    ]
