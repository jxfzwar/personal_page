# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 06:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20170802_0654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='publish_date',
            new_name='publish_year',
        ),
    ]
