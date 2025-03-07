# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-18 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0022_auto_20190531_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configperfis_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
            ],
            options={
                'db_table': 'config_perfis_grupos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='configperfis',
            options={'managed': True, 'ordering': ['titulo'], 'permissions': (('can_view_config_perfis', 'Can view config_perfis'),), 'verbose_name': 'Perfis', 'verbose_name_plural': 'Perfis'},
        ),
        migrations.AlterModelOptions(
            name='usuarios',
            options={'managed': True, 'permissions': (('can_view_usuarios', 'Can view usuarios'), ('can_create_token_usuarios', 'Pode criar Token')), 'verbose_name': 'Usu\xe1rios'},
        ),
    ]
