# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-27 16:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('esocial', '0024_auto_20190427_1615'),
        ('s2306', '0009_auto_20190204_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='s2306infoComplementares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2306infocomplementares_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2306infocomplementares_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('s2306_evttsvaltcontr', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2306infocomplementares_s2306_evttsvaltcontr', to='esocial.s2306evtTSVAltContr')),
            ],
            options={
                'managed': True,
                'ordering': ['s2306_evttsvaltcontr'],
                'db_table': 's2306_infocomplementares',
                'permissions': (('can_view_s2306_infocomplementares', 'Can view s2306_infocomplementares'),),
            },
        ),
        migrations.AlterModelOptions(
            name='s2306cargofuncao',
            options={'managed': True, 'ordering': ['s2306_infocomplementares', 'codcargo'], 'permissions': (('can_view_s2306_cargofuncao', 'Can view s2306_cargofuncao'),)},
        ),
        migrations.AlterModelOptions(
            name='s2306infoestagiario',
            options={'managed': True, 'ordering': ['s2306_infocomplementares', 'natestagio', 'nivestagio', 'dtprevterm', 'nmrazao'], 'permissions': (('can_view_s2306_infoestagiario', 'Can view s2306_infoestagiario'),)},
        ),
        migrations.AlterModelOptions(
            name='s2306infotrabcedido',
            options={'managed': True, 'ordering': ['s2306_infocomplementares', 'indremuncargo'], 'permissions': (('can_view_s2306_infotrabcedido', 'Can view s2306_infotrabcedido'),)},
        ),
        migrations.AlterModelOptions(
            name='s2306remuneracao',
            options={'managed': True, 'ordering': ['s2306_infocomplementares', 'vrsalfx', 'undsalfixo'], 'permissions': (('can_view_s2306_remuneracao', 'Can view s2306_remuneracao'),)},
        ),
        migrations.RemoveField(
            model_name='s2306cargofuncao',
            name='s2306_evttsvaltcontr',
        ),
        migrations.RemoveField(
            model_name='s2306infoestagiario',
            name='s2306_evttsvaltcontr',
        ),
        migrations.RemoveField(
            model_name='s2306infotrabcedido',
            name='s2306_evttsvaltcontr',
        ),
        migrations.RemoveField(
            model_name='s2306remuneracao',
            name='s2306_evttsvaltcontr',
        ),
        migrations.AlterField(
            model_name='s2306ageintegracao',
            name='cep',
            field=models.CharField(default=b'A', max_length=8),
        ),
        migrations.AlterField(
            model_name='s2306ageintegracao',
            name='cnpjagntinteg',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s2306ageintegracao',
            name='dsclograd',
            field=models.CharField(default=b'A', max_length=100),
        ),
        migrations.AlterField(
            model_name='s2306ageintegracao',
            name='nmrazao',
            field=models.CharField(default=b'A', max_length=100),
        ),
        migrations.AlterField(
            model_name='s2306ageintegracao',
            name='nrlograd',
            field=models.CharField(default=b'A', max_length=10),
        ),
        migrations.AlterField(
            model_name='s2306ageintegracao',
            name='s2306_infoestagiario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2306ageintegracao_s2306_infoestagiario', to='s2306.s2306infoEstagiario'),
        ),
        migrations.AlterField(
            model_name='s2306ageintegracao',
            name='uf',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='s2306cargofuncao',
            name='codcargo',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s2306infoestagiario',
            name='dtprevterm',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2306infoestagiario',
            name='natestagio',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o Obrigat\xf3rio'), (b'O', 'O - Obrigat\xf3rio')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2306infoestagiario',
            name='nivestagio',
            field=models.IntegerField(choices=[(1, '1 - Fundamental'), (2, '2 - M\xe9dio'), (3, '3 - Forma\xe7\xe3o Profissional'), (4, '4 - Superior'), (8, '8 - Especial'), (9, '9 - M\xe3e social (Lei 7644, de 1987)')], default=0),
        ),
        migrations.AlterField(
            model_name='s2306infoestagiario',
            name='nmrazao',
            field=models.CharField(default=b'A', max_length=100),
        ),
        migrations.AlterField(
            model_name='s2306infotrabcedido',
            name='indremuncargo',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2306remuneracao',
            name='undsalfixo',
            field=models.IntegerField(choices=[(1, '1 - Por Hora'), (2, '2 - Por Dia'), (3, '3 - Por Semana'), (4, '4 - Por Quinzena'), (5, '5 - Por M\xeas'), (6, '6 - Por Tarefa'), (7, '7 - N\xe3o aplic\xe1vel - sal\xe1rio exclusivamente vari\xe1vel')], default=0),
        ),
        migrations.AlterField(
            model_name='s2306remuneracao',
            name='vrsalfx',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s2306supervisorestagio',
            name='cpfsupervisor',
            field=models.CharField(default=b'A', max_length=11),
        ),
        migrations.AlterField(
            model_name='s2306supervisorestagio',
            name='nmsuperv',
            field=models.CharField(default=b'A', max_length=70),
        ),
        migrations.AlterField(
            model_name='s2306supervisorestagio',
            name='s2306_infoestagiario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2306supervisorestagio_s2306_infoestagiario', to='s2306.s2306infoEstagiario'),
        ),
        migrations.AddField(
            model_name='s2306cargofuncao',
            name='s2306_infocomplementares',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2306cargofuncao_s2306_infocomplementares', to='s2306.s2306infoComplementares'),
        ),
        migrations.AddField(
            model_name='s2306infoestagiario',
            name='s2306_infocomplementares',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2306infoestagiario_s2306_infocomplementares', to='s2306.s2306infoComplementares'),
        ),
        migrations.AddField(
            model_name='s2306infotrabcedido',
            name='s2306_infocomplementares',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2306infotrabcedido_s2306_infocomplementares', to='s2306.s2306infoComplementares'),
        ),
        migrations.AddField(
            model_name='s2306remuneracao',
            name='s2306_infocomplementares',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2306remuneracao_s2306_infocomplementares', to='s2306.s2306infoComplementares'),
        ),
    ]
