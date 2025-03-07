# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r2010', '0015_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r2010infoprocretad',
            options={'managed': True, 'ordering': ['r2010_evtservtom', 'tpprocretadic', 'nrprocretadic', 'valoradic'], 'permissions': (('can_see_list_r2010infoProcRetAd', 'Pode ver listagem do modelo R2010INFOPROCRETAD'), ('can_see_data_r2010infoProcRetAd', 'Pode visualizar o conte\xfado do modelo R2010INFOPROCRETAD'), ('can_see_menu_r2010infoProcRetAd', 'Pode visualizar no menu o modelo R2010INFOPROCRETAD'), ('can_print_list_r2010infoProcRetAd', 'Pode imprimir listagem do modelo R2010INFOPROCRETAD'), ('can_print_data_r2010infoProcRetAd', 'Pode imprimir o conte\xfado do modelo R2010INFOPROCRETAD'))},
        ),
        migrations.AlterModelOptions(
            name='r2010infoprocretpr',
            options={'managed': True, 'ordering': ['r2010_evtservtom', 'tpprocretprinc', 'nrprocretprinc', 'valorprinc'], 'permissions': (('can_see_list_r2010infoProcRetPr', 'Pode ver listagem do modelo R2010INFOPROCRETPR'), ('can_see_data_r2010infoProcRetPr', 'Pode visualizar o conte\xfado do modelo R2010INFOPROCRETPR'), ('can_see_menu_r2010infoProcRetPr', 'Pode visualizar no menu o modelo R2010INFOPROCRETPR'), ('can_print_list_r2010infoProcRetPr', 'Pode imprimir listagem do modelo R2010INFOPROCRETPR'), ('can_print_data_r2010infoProcRetPr', 'Pode imprimir o conte\xfado do modelo R2010INFOPROCRETPR'))},
        ),
        migrations.AlterModelOptions(
            name='r2010infotpserv',
            options={'managed': True, 'ordering': ['r2010_nfs', 'tpservico', 'vlrbaseret', 'vlrretencao'], 'permissions': (('can_see_list_r2010infoTpServ', 'Pode ver listagem do modelo R2010INFOTPSERV'), ('can_see_data_r2010infoTpServ', 'Pode visualizar o conte\xfado do modelo R2010INFOTPSERV'), ('can_see_menu_r2010infoTpServ', 'Pode visualizar no menu o modelo R2010INFOTPSERV'), ('can_print_list_r2010infoTpServ', 'Pode imprimir listagem do modelo R2010INFOTPSERV'), ('can_print_data_r2010infoTpServ', 'Pode imprimir o conte\xfado do modelo R2010INFOTPSERV'))},
        ),
        migrations.AlterModelOptions(
            name='r2010nfs',
            options={'managed': True, 'ordering': ['r2010_evtservtom', 'serie', 'numdocto', 'dtemissaonf', 'vlrbruto'], 'permissions': (('can_see_list_r2010nfs', 'Pode ver listagem do modelo R2010NFS'), ('can_see_data_r2010nfs', 'Pode visualizar o conte\xfado do modelo R2010NFS'), ('can_see_menu_r2010nfs', 'Pode visualizar no menu o modelo R2010NFS'), ('can_print_list_r2010nfs', 'Pode imprimir listagem do modelo R2010NFS'), ('can_print_data_r2010nfs', 'Pode imprimir o conte\xfado do modelo R2010NFS'))},
        ),
    ]
