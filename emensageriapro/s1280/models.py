#coding:utf-8
from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.utils import timezone
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from emensageriapro.soft_delete import SoftDeletionModel
from emensageriapro.s1280.choices import *
get_model = apps.get_model


"""

    eMensageria - Sistema Open-Source de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""


STATUS_EVENTO_CADASTRADO = 0
STATUS_EVENTO_IMPORTADO = 1
STATUS_EVENTO_DUPLICADO = 2
STATUS_EVENTO_GERADO = 3
STATUS_EVENTO_GERADO_ERRO = 4
STATUS_EVENTO_ASSINADO = 5
STATUS_EVENTO_ASSINADO_ERRO = 6
STATUS_EVENTO_VALIDADO = 7
STATUS_EVENTO_VALIDADO_ERRO = 8
STATUS_EVENTO_AGUARD_PRECEDENCIA = 9
STATUS_EVENTO_AGUARD_ENVIO = 10
STATUS_EVENTO_ENVIADO = 11
STATUS_EVENTO_ENVIADO_ERRO = 12
STATUS_EVENTO_PROCESSADO = 13





class s1280infoAtivConcom(SoftDeletionModel):

    s1280_evtinfocomplper = models.ForeignKey('esocial.s1280evtInfoComplPer',
        related_name='%(class)s_s1280_evtinfocomplper', )

    def evento(self):
        return self.s1280_evtinfocomplper.evento()
    fatormes = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    fator13 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1280_evtinfocomplper) + ' - ' + unicode(self.fatormes) + ' - ' + unicode(self.fator13)

    class Meta:

        # verbose_name = u'Registro preenchido por empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída e não substituída.'
        db_table = r's1280_infoativconcom'
        managed = True # s1280_infoativconcom #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1280infoAtivConcom", u"Pode ver listagem do modelo S1280INFOATIVCONCOM"),
            ("can_see_data_s1280infoAtivConcom", u"Pode visualizar o conteúdo do modelo S1280INFOATIVCONCOM"),
            ("can_see_menu_s1280infoAtivConcom", u"Pode visualizar no menu o modelo S1280INFOATIVCONCOM"),
            ("can_print_list_s1280infoAtivConcom", u"Pode imprimir listagem do modelo S1280INFOATIVCONCOM"),
            ("can_print_data_s1280infoAtivConcom", u"Pode imprimir o conteúdo do modelo S1280INFOATIVCONCOM"), )

        ordering = [
            's1280_evtinfocomplper',
            'fatormes',
            'fator13',]



class s1280infoAtivConcomSerializer(ModelSerializer):

    class Meta:

        model = s1280infoAtivConcom
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1280infoSubstPatr(SoftDeletionModel):

    s1280_evtinfocomplper = models.ForeignKey('esocial.s1280evtInfoComplPer',
        related_name='%(class)s_s1280_evtinfocomplper', )

    def evento(self):
        return self.s1280_evtinfocomplper.evento()
    indsubstpatr = models.IntegerField(choices=CHOICES_S1280_INDSUBSTPATR, null=True, )
    percredcontrib = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1280_evtinfocomplper) + ' - ' + unicode(self.indsubstpatr) + ' - ' + unicode(self.percredcontrib)

    class Meta:

        # verbose_name = u'Registro preenchido exclusivamente por empresa enquadrada nos artigos 7 a 9 da Lei 12.546/2011, conforme classificação tributária indicada no evento de Informações Cadastrais do Empregador.'
        db_table = r's1280_infosubstpatr'
        managed = True # s1280_infosubstpatr #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1280infoSubstPatr", u"Pode ver listagem do modelo S1280INFOSUBSTPATR"),
            ("can_see_data_s1280infoSubstPatr", u"Pode visualizar o conteúdo do modelo S1280INFOSUBSTPATR"),
            ("can_see_menu_s1280infoSubstPatr", u"Pode visualizar no menu o modelo S1280INFOSUBSTPATR"),
            ("can_print_list_s1280infoSubstPatr", u"Pode imprimir listagem do modelo S1280INFOSUBSTPATR"),
            ("can_print_data_s1280infoSubstPatr", u"Pode imprimir o conteúdo do modelo S1280INFOSUBSTPATR"), )

        ordering = [
            's1280_evtinfocomplper',
            'indsubstpatr',
            'percredcontrib',]



class s1280infoSubstPatrSerializer(ModelSerializer):

    class Meta:

        model = s1280infoSubstPatr
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1280infoSubstPatrOpPort(SoftDeletionModel):

    s1280_evtinfocomplper = models.ForeignKey('esocial.s1280evtInfoComplPer',
        related_name='%(class)s_s1280_evtinfocomplper', )

    def evento(self):
        return self.s1280_evtinfocomplper.evento()
    cnpjopportuario = models.CharField(max_length=14, null=True, )

    def __unicode__(self):
        return unicode(self.s1280_evtinfocomplper) + ' - ' + unicode(self.cnpjopportuario)

    class Meta:

        # verbose_name = u'Registro preenchido exclusivamente pelo OGMO ({classTrib}=[09]) listando apenas seus Operadores Portuários enquadrados nos artigos 7 a 9 da Lei 12.546/2011.'
        db_table = r's1280_infosubstpatropport'
        managed = True # s1280_infosubstpatropport #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1280infoSubstPatrOpPort", u"Pode ver listagem do modelo S1280INFOSUBSTPATROPPORT"),
            ("can_see_data_s1280infoSubstPatrOpPort", u"Pode visualizar o conteúdo do modelo S1280INFOSUBSTPATROPPORT"),
            ("can_see_menu_s1280infoSubstPatrOpPort", u"Pode visualizar no menu o modelo S1280INFOSUBSTPATROPPORT"),
            ("can_print_list_s1280infoSubstPatrOpPort", u"Pode imprimir listagem do modelo S1280INFOSUBSTPATROPPORT"),
            ("can_print_data_s1280infoSubstPatrOpPort", u"Pode imprimir o conteúdo do modelo S1280INFOSUBSTPATROPPORT"), )

        ordering = [
            's1280_evtinfocomplper',
            'cnpjopportuario',]



class s1280infoSubstPatrOpPortSerializer(ModelSerializer):

    class Meta:

        model = s1280infoSubstPatrOpPort
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')