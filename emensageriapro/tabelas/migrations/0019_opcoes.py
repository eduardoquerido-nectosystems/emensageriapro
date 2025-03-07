# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-26 18:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tabelas', '0018_auto_20190513_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opcoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcao_slug', models.CharField(max_length=50)),
                ('opcao_id', models.IntegerField()),
                ('codigo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opcoes_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opcoes_modificado_por', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
                'ordering': ['opcao_slug', 'codigo'],
                'db_table': 'opcoes',
                'verbose_name': 'Op\xe7\xf5es',
                'permissions': (('can_view_opcoes', 'Can view opcoes'),),
            },
        ),
    ]
