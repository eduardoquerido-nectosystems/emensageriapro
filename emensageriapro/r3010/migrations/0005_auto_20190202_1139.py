# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-02 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r3010', '0004_auto_20181213_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r3010boletim',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='r3010infoproc',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='r3010outrasreceitas',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='r3010receitaingressos',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
    ]
