# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-07-30 10:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20200730_1013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='real_name',
            new_name='name',
        ),
    ]
