# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 21:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('s1300', '0007_auto_20190204_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='s1300contribsind',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s1300contribsind_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s1300contribsind',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s1300contribsind_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
    ]
