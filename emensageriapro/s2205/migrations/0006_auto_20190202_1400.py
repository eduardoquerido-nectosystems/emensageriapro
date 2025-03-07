# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-02 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2205', '0005_auto_20181213_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2205aposentadoria',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2205brasil',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2205cnh',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2205contato',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2205ctps',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2205dependente',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2205exterior',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2205infodeficiencia',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2205oc',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2205rg',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2205ric',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2205rne',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2205trabestrangeiro',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
    ]
