# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2410', '0006_auto_20190204_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s2410homologtc',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2410homologtc',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2410infopenmorte',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2410infopenmorte',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2410instpenmorte',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2410instpenmorte',
            name='modificado_por',
        ),
        migrations.AlterField(
            model_name='s2410homologtc',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2410homologtc',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2410infopenmorte',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2410infopenmorte',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2410instpenmorte',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2410instpenmorte',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
