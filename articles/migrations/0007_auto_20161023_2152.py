# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20161020_2056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['id'], 'verbose_name': 'client', 'verbose_name_plural': 'clients'},
        ),
        migrations.RenameField(
            model_name='client',
            old_name='debt',
            new_name='balance',
        ),
    ]
