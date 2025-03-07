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
from emensageriapro.s2240.choices import *
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





class s2240altExpRisco(SoftDeletionModel):

    s2240_evtexprisco = models.ForeignKey('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco', )

    def evento(self):
        return self.s2240_evtexprisco.evento()
    dtaltcondicao = models.DateField(null=True, )

    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.dtaltcondicao)

    class Meta:

        # verbose_name = u'Condições ambientais do trabalho - Alteração'
        db_table = r's2240_altexprisco'
        managed = True # s2240_altexprisco #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2240altExpRisco", u"Pode ver listagem do modelo S2240ALTEXPRISCO"),
            ("can_see_data_s2240altExpRisco", u"Pode visualizar o conteúdo do modelo S2240ALTEXPRISCO"),
            ("can_see_menu_s2240altExpRisco", u"Pode visualizar no menu o modelo S2240ALTEXPRISCO"),
            ("can_print_list_s2240altExpRisco", u"Pode imprimir listagem do modelo S2240ALTEXPRISCO"),
            ("can_print_data_s2240altExpRisco", u"Pode imprimir o conteúdo do modelo S2240ALTEXPRISCO"), )

        ordering = [
            's2240_evtexprisco',
            'dtaltcondicao',]



class s2240altExpRiscoSerializer(ModelSerializer):

    class Meta:

        model = s2240altExpRisco
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2240altExpRiscoepc(SoftDeletionModel):

    s2240_altexprisco_fatrisco = models.ForeignKey('s2240.s2240altExpRiscofatRisco',
        related_name='%(class)s_s2240_altexprisco_fatrisco', )

    def evento(self):
        return self.s2240_altexprisco_fatrisco.evento()
    dscepc = models.CharField(max_length=70, null=True, )
    eficepc = models.CharField(choices=CHOICES_S2240_EFICEPC_ALTEXPRISCO, max_length=1, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s2240_altexprisco_fatrisco) + ' - ' + unicode(self.dscepc)

    class Meta:

        # verbose_name = u'Equipamentos de Proteção Coletiva - EPC'
        db_table = r's2240_altexprisco_epc'
        managed = True # s2240_altexprisco_epc #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2240altExpRiscoepc", u"Pode ver listagem do modelo S2240ALTEXPRISCOEPC"),
            ("can_see_data_s2240altExpRiscoepc", u"Pode visualizar o conteúdo do modelo S2240ALTEXPRISCOEPC"),
            ("can_see_menu_s2240altExpRiscoepc", u"Pode visualizar no menu o modelo S2240ALTEXPRISCOEPC"),
            ("can_print_list_s2240altExpRiscoepc", u"Pode imprimir listagem do modelo S2240ALTEXPRISCOEPC"),
            ("can_print_data_s2240altExpRiscoepc", u"Pode imprimir o conteúdo do modelo S2240ALTEXPRISCOEPC"), )

        ordering = [
            's2240_altexprisco_fatrisco',
            'dscepc',]



class s2240altExpRiscoepcSerializer(ModelSerializer):

    class Meta:

        model = s2240altExpRiscoepc
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2240altExpRiscoepi(SoftDeletionModel):

    s2240_altexprisco_fatrisco = models.ForeignKey('s2240.s2240altExpRiscofatRisco',
        related_name='%(class)s_s2240_altexprisco_fatrisco', )

    def evento(self):
        return self.s2240_altexprisco_fatrisco.evento()
    caepi = models.CharField(max_length=20, blank=True, null=True, )
    eficepi = models.CharField(choices=CHOICES_S2240_EFICEPI_ALTEXPRISCO, max_length=1, null=True, )
    medprotecao = models.CharField(choices=CHOICES_S2240_MEDPROTECAO_ALTEXPRISCO, max_length=1, null=True, )
    condfuncto = models.CharField(choices=CHOICES_S2240_CONDFUNCTO_ALTEXPRISCO, max_length=1, null=True, )
    przvalid = models.CharField(choices=CHOICES_S2240_PRZVALID_ALTEXPRISCO, max_length=1, null=True, )
    periodictroca = models.CharField(choices=CHOICES_S2240_PERIODICTROCA_ALTEXPRISCO, max_length=1, null=True, )
    higienizacao = models.CharField(choices=CHOICES_S2240_HIGIENIZACAO_ALTEXPRISCO, max_length=1, null=True, )

    def __unicode__(self):
        return unicode(self.s2240_altexprisco_fatrisco) + ' - ' + unicode(self.eficepi) + ' - ' + unicode(self.medprotecao) + ' - ' + unicode(self.condfuncto) + ' - ' + unicode(self.przvalid) + ' - ' + unicode(self.periodictroca) + ' - ' + unicode(self.higienizacao)

    class Meta:

        # verbose_name = u'Equipamentos de Proteção Individual - EPI'
        db_table = r's2240_altexprisco_epi'
        managed = True # s2240_altexprisco_epi #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2240altExpRiscoepi", u"Pode ver listagem do modelo S2240ALTEXPRISCOEPI"),
            ("can_see_data_s2240altExpRiscoepi", u"Pode visualizar o conteúdo do modelo S2240ALTEXPRISCOEPI"),
            ("can_see_menu_s2240altExpRiscoepi", u"Pode visualizar no menu o modelo S2240ALTEXPRISCOEPI"),
            ("can_print_list_s2240altExpRiscoepi", u"Pode imprimir listagem do modelo S2240ALTEXPRISCOEPI"),
            ("can_print_data_s2240altExpRiscoepi", u"Pode imprimir o conteúdo do modelo S2240ALTEXPRISCOEPI"), )

        ordering = [
            's2240_altexprisco_fatrisco',
            'eficepi',
            'medprotecao',
            'condfuncto',
            'przvalid',
            'periodictroca',
            'higienizacao',]



class s2240altExpRiscoepiSerializer(ModelSerializer):

    class Meta:

        model = s2240altExpRiscoepi
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2240altExpRiscofatRisco(SoftDeletionModel):

    s2240_altexprisco_infoamb = models.ForeignKey('s2240.s2240altExpRiscoinfoAmb',
        related_name='%(class)s_s2240_altexprisco_infoamb', )

    def evento(self):
        return self.s2240_altexprisco_infoamb.evento()
    codfatris = models.TextField(null=True, )
    intconc = models.CharField(max_length=15, blank=True, null=True, )
    tecmedicao = models.CharField(max_length=40, blank=True, null=True, )
    utilizepc = models.IntegerField(choices=CHOICES_S2240_UTILIZEPC_ALTEXPRISCO, null=True, )
    utilizepi = models.IntegerField(choices=CHOICES_S2240_UTILIZEPI_ALTEXPRISCO, null=True, )

    def __unicode__(self):
        return unicode(self.s2240_altexprisco_infoamb) + ' - ' + unicode(self.codfatris) + ' - ' + unicode(self.utilizepc) + ' - ' + unicode(self.utilizepi)

    class Meta:

        # verbose_name = u'Fator de risco ao qual o trabalhador está exposto na atividade exercida no ambiente'
        db_table = r's2240_altexprisco_fatrisco'
        managed = True # s2240_altexprisco_fatrisco #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2240altExpRiscofatRisco", u"Pode ver listagem do modelo S2240ALTEXPRISCOFATRISCO"),
            ("can_see_data_s2240altExpRiscofatRisco", u"Pode visualizar o conteúdo do modelo S2240ALTEXPRISCOFATRISCO"),
            ("can_see_menu_s2240altExpRiscofatRisco", u"Pode visualizar no menu o modelo S2240ALTEXPRISCOFATRISCO"),
            ("can_print_list_s2240altExpRiscofatRisco", u"Pode imprimir listagem do modelo S2240ALTEXPRISCOFATRISCO"),
            ("can_print_data_s2240altExpRiscofatRisco", u"Pode imprimir o conteúdo do modelo S2240ALTEXPRISCOFATRISCO"), )

        ordering = [
            's2240_altexprisco_infoamb',
            'codfatris',
            'utilizepc',
            'utilizepi',]



class s2240altExpRiscofatRiscoSerializer(ModelSerializer):

    class Meta:

        model = s2240altExpRiscofatRisco
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2240altExpRiscoinfoAmb(SoftDeletionModel):

    s2240_altexprisco = models.ForeignKey('s2240.s2240altExpRisco',
        related_name='%(class)s_s2240_altexprisco', )

    def evento(self):
        return self.s2240_altexprisco.evento()
    codamb = models.CharField(max_length=30, null=True, )
    dscativdes = models.CharField(max_length=999, null=True, )

    def __unicode__(self):
        return unicode(self.s2240_altexprisco) + ' - ' + unicode(self.codamb) + ' - ' + unicode(self.dscativdes)

    class Meta:

        # verbose_name = u'Informações relativas ao ambiente de trabalho'
        db_table = r's2240_altexprisco_infoamb'
        managed = True # s2240_altexprisco_infoamb #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2240altExpRiscoinfoAmb", u"Pode ver listagem do modelo S2240ALTEXPRISCOINFOAMB"),
            ("can_see_data_s2240altExpRiscoinfoAmb", u"Pode visualizar o conteúdo do modelo S2240ALTEXPRISCOINFOAMB"),
            ("can_see_menu_s2240altExpRiscoinfoAmb", u"Pode visualizar no menu o modelo S2240ALTEXPRISCOINFOAMB"),
            ("can_print_list_s2240altExpRiscoinfoAmb", u"Pode imprimir listagem do modelo S2240ALTEXPRISCOINFOAMB"),
            ("can_print_data_s2240altExpRiscoinfoAmb", u"Pode imprimir o conteúdo do modelo S2240ALTEXPRISCOINFOAMB"), )

        ordering = [
            's2240_altexprisco',
            'codamb',
            'dscativdes',]



class s2240altExpRiscoinfoAmbSerializer(ModelSerializer):

    class Meta:

        model = s2240altExpRiscoinfoAmb
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2240fimExpRisco(SoftDeletionModel):

    s2240_evtexprisco = models.ForeignKey('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco', )

    def evento(self):
        return self.s2240_evtexprisco.evento()
    dtfimcondicao = models.DateField(null=True, )

    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.dtfimcondicao)

    class Meta:

        # verbose_name = u'Condições ambientais do trabalho - Fim'
        db_table = r's2240_fimexprisco'
        managed = True # s2240_fimexprisco #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2240fimExpRisco", u"Pode ver listagem do modelo S2240FIMEXPRISCO"),
            ("can_see_data_s2240fimExpRisco", u"Pode visualizar o conteúdo do modelo S2240FIMEXPRISCO"),
            ("can_see_menu_s2240fimExpRisco", u"Pode visualizar no menu o modelo S2240FIMEXPRISCO"),
            ("can_print_list_s2240fimExpRisco", u"Pode imprimir listagem do modelo S2240FIMEXPRISCO"),
            ("can_print_data_s2240fimExpRisco", u"Pode imprimir o conteúdo do modelo S2240FIMEXPRISCO"), )

        ordering = [
            's2240_evtexprisco',
            'dtfimcondicao',]



class s2240fimExpRiscoSerializer(ModelSerializer):

    class Meta:

        model = s2240fimExpRisco
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2240fimExpRiscoinfoAmb(SoftDeletionModel):

    s2240_fimexprisco = models.ForeignKey('s2240.s2240fimExpRisco',
        related_name='%(class)s_s2240_fimexprisco', )

    def evento(self):
        return self.s2240_fimexprisco.evento()
    codamb = models.CharField(max_length=30, null=True, )

    def __unicode__(self):
        return unicode(self.s2240_fimexprisco) + ' - ' + unicode(self.codamb)

    class Meta:

        # verbose_name = u'Informações relativas ao ambiente de trabalho'
        db_table = r's2240_fimexprisco_infoamb'
        managed = True # s2240_fimexprisco_infoamb #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2240fimExpRiscoinfoAmb", u"Pode ver listagem do modelo S2240FIMEXPRISCOINFOAMB"),
            ("can_see_data_s2240fimExpRiscoinfoAmb", u"Pode visualizar o conteúdo do modelo S2240FIMEXPRISCOINFOAMB"),
            ("can_see_menu_s2240fimExpRiscoinfoAmb", u"Pode visualizar no menu o modelo S2240FIMEXPRISCOINFOAMB"),
            ("can_print_list_s2240fimExpRiscoinfoAmb", u"Pode imprimir listagem do modelo S2240FIMEXPRISCOINFOAMB"),
            ("can_print_data_s2240fimExpRiscoinfoAmb", u"Pode imprimir o conteúdo do modelo S2240FIMEXPRISCOINFOAMB"), )

        ordering = [
            's2240_fimexprisco',
            'codamb',]



class s2240fimExpRiscoinfoAmbSerializer(ModelSerializer):

    class Meta:

        model = s2240fimExpRiscoinfoAmb
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2240fimExpRiscorespReg(SoftDeletionModel):

    s2240_evtexprisco = models.ForeignKey('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco', )

    def evento(self):
        return self.s2240_evtexprisco.evento()
    dtini = models.DateField(null=True, )
    dtfim = models.DateField(blank=True, null=True, )
    nisresp = models.CharField(max_length=11, null=True, )
    nroc = models.CharField(max_length=14, null=True, )
    ufoc = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.dtini) + ' - ' + unicode(self.nisresp) + ' - ' + unicode(self.nroc)

    class Meta:

        # verbose_name = u'Informações relativas ao responsável pelos registros ambientais'
        db_table = r's2240_fimexprisco_respreg'
        managed = True # s2240_fimexprisco_respreg #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2240fimExpRiscorespReg", u"Pode ver listagem do modelo S2240FIMEXPRISCORESPREG"),
            ("can_see_data_s2240fimExpRiscorespReg", u"Pode visualizar o conteúdo do modelo S2240FIMEXPRISCORESPREG"),
            ("can_see_menu_s2240fimExpRiscorespReg", u"Pode visualizar no menu o modelo S2240FIMEXPRISCORESPREG"),
            ("can_print_list_s2240fimExpRiscorespReg", u"Pode imprimir listagem do modelo S2240FIMEXPRISCORESPREG"),
            ("can_print_data_s2240fimExpRiscorespReg", u"Pode imprimir o conteúdo do modelo S2240FIMEXPRISCORESPREG"), )

        ordering = [
            's2240_evtexprisco',
            'dtini',
            'nisresp',
            'nroc',]



class s2240fimExpRiscorespRegSerializer(ModelSerializer):

    class Meta:

        model = s2240fimExpRiscorespReg
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2240iniExpRiscoativPericInsal(SoftDeletionModel):

    s2240_evtexprisco = models.ForeignKey('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco', )

    def evento(self):
        return self.s2240_evtexprisco.evento()
    codativ = models.TextField(null=True, )

    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.codativ)

    class Meta:

        # verbose_name = u'Informação da(s) atividade(s) periculosa(s), insalubre(s) ou especial(is) desempenhada(s)'
        db_table = r's2240_iniexprisco_ativpericinsal'
        managed = True # s2240_iniexprisco_ativpericinsal #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2240iniExpRiscoativPericInsal", u"Pode ver listagem do modelo S2240INIEXPRISCOATIVPERICINSAL"),
            ("can_see_data_s2240iniExpRiscoativPericInsal", u"Pode visualizar o conteúdo do modelo S2240INIEXPRISCOATIVPERICINSAL"),
            ("can_see_menu_s2240iniExpRiscoativPericInsal", u"Pode visualizar no menu o modelo S2240INIEXPRISCOATIVPERICINSAL"),
            ("can_print_list_s2240iniExpRiscoativPericInsal", u"Pode imprimir listagem do modelo S2240INIEXPRISCOATIVPERICINSAL"),
            ("can_print_data_s2240iniExpRiscoativPericInsal", u"Pode imprimir o conteúdo do modelo S2240INIEXPRISCOATIVPERICINSAL"), )

        ordering = [
            's2240_evtexprisco',
            'codativ',]



class s2240iniExpRiscoativPericInsalSerializer(ModelSerializer):

    class Meta:

        model = s2240iniExpRiscoativPericInsal
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2240iniExpRiscoepc(SoftDeletionModel):

    s2240_iniexprisco_fatrisco = models.ForeignKey('s2240.s2240iniExpRiscofatRisco',
        related_name='%(class)s_s2240_iniexprisco_fatrisco', )

    def evento(self):
        return self.s2240_iniexprisco_fatrisco.evento()
    codep = models.CharField(max_length=30, null=True, )
    dscepc = models.CharField(max_length=70, null=True, )
    eficepc = models.CharField(choices=CHOICES_S2240_EFICEPC_INIEXPRISCO, max_length=1, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s2240_iniexprisco_fatrisco) + ' - ' + unicode(self.codep) + ' - ' + unicode(self.dscepc)

    class Meta:

        # verbose_name = u'Equipamentos de Proteção Coletiva - EPC'
        db_table = r's2240_iniexprisco_epc'
        managed = True # s2240_iniexprisco_epc #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2240iniExpRiscoepc", u"Pode ver listagem do modelo S2240INIEXPRISCOEPC"),
            ("can_see_data_s2240iniExpRiscoepc", u"Pode visualizar o conteúdo do modelo S2240INIEXPRISCOEPC"),
            ("can_see_menu_s2240iniExpRiscoepc", u"Pode visualizar no menu o modelo S2240INIEXPRISCOEPC"),
            ("can_print_list_s2240iniExpRiscoepc", u"Pode imprimir listagem do modelo S2240INIEXPRISCOEPC"),
            ("can_print_data_s2240iniExpRiscoepc", u"Pode imprimir o conteúdo do modelo S2240INIEXPRISCOEPC"), )

        ordering = [
            's2240_iniexprisco_fatrisco',
            'codep',
            'dscepc',]



class s2240iniExpRiscoepcSerializer(ModelSerializer):

    class Meta:

        model = s2240iniExpRiscoepc
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2240iniExpRiscoepi(SoftDeletionModel):

    s2240_iniexprisco_fatrisco = models.ForeignKey('s2240.s2240iniExpRiscofatRisco',
        related_name='%(class)s_s2240_iniexprisco_fatrisco', )

    def evento(self):
        return self.s2240_iniexprisco_fatrisco.evento()
    caepi = models.CharField(max_length=20, blank=True, null=True, )
    dscepi = models.CharField(max_length=999, blank=True, null=True, )
    eficepi = models.CharField(choices=CHOICES_S2240_EFICEPI_INIEXPRISCO, max_length=1, null=True, )
    medprotecao = models.CharField(choices=CHOICES_S2240_MEDPROTECAO_INIEXPRISCO, max_length=1, null=True, )
    condfuncto = models.CharField(choices=CHOICES_S2240_CONDFUNCTO_INIEXPRISCO, max_length=1, null=True, )
    usoinint = models.CharField(choices=CHOICES_S2240_USOININT_INIEXPRISCO, max_length=1, null=True, )
    przvalid = models.CharField(choices=CHOICES_S2240_PRZVALID_INIEXPRISCO, max_length=1, null=True, )
    periodictroca = models.CharField(choices=CHOICES_S2240_PERIODICTROCA_INIEXPRISCO, max_length=1, null=True, )
    higienizacao = models.CharField(choices=CHOICES_S2240_HIGIENIZACAO_INIEXPRISCO, max_length=1, null=True, )

    def __unicode__(self):
        return unicode(self.s2240_iniexprisco_fatrisco) + ' - ' + unicode(self.eficepi) + ' - ' + unicode(self.medprotecao) + ' - ' + unicode(self.condfuncto) + ' - ' + unicode(self.usoinint) + ' - ' + unicode(self.przvalid) + ' - ' + unicode(self.periodictroca) + ' - ' + unicode(self.higienizacao)

    class Meta:

        # verbose_name = u'Equipamentos de Proteção Individual - EPI'
        db_table = r's2240_iniexprisco_epi'
        managed = True # s2240_iniexprisco_epi #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2240iniExpRiscoepi", u"Pode ver listagem do modelo S2240INIEXPRISCOEPI"),
            ("can_see_data_s2240iniExpRiscoepi", u"Pode visualizar o conteúdo do modelo S2240INIEXPRISCOEPI"),
            ("can_see_menu_s2240iniExpRiscoepi", u"Pode visualizar no menu o modelo S2240INIEXPRISCOEPI"),
            ("can_print_list_s2240iniExpRiscoepi", u"Pode imprimir listagem do modelo S2240INIEXPRISCOEPI"),
            ("can_print_data_s2240iniExpRiscoepi", u"Pode imprimir o conteúdo do modelo S2240INIEXPRISCOEPI"), )

        ordering = [
            's2240_iniexprisco_fatrisco',
            'eficepi',
            'medprotecao',
            'condfuncto',
            'usoinint',
            'przvalid',
            'periodictroca',
            'higienizacao',]



class s2240iniExpRiscoepiSerializer(ModelSerializer):

    class Meta:

        model = s2240iniExpRiscoepi
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2240iniExpRiscofatRisco(SoftDeletionModel):

    s2240_evtexprisco = models.ForeignKey('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco', )

    def evento(self):
        return self.s2240_evtexprisco.evento()
    codfatris = models.TextField(null=True, )
    dscfatrisc = models.CharField(max_length=999, blank=True, null=True, )
    tpaval = models.IntegerField(choices=CHOICES_S2240_TPAVAL_INIEXPRISCO, null=True, )
    intconc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    limtol = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    unmed = models.IntegerField(blank=True, null=True, )
    tecmedicao = models.CharField(max_length=40, blank=True, null=True, )
    insalubridade = models.CharField(choices=CHOICES_S2240_INSALUBRIDADE_INIEXPRISCO, max_length=1, blank=True, null=True, )
    periculosidade = models.CharField(choices=CHOICES_S2240_PERICULOSIDADE_INIEXPRISCO, max_length=1, blank=True, null=True, )
    aposentesp = models.CharField(choices=CHOICES_S2240_APOSENTESP_INIEXPRISCO, max_length=1, blank=True, null=True, )
    utilizepc = models.IntegerField(choices=CHOICES_S2240_UTILIZEPC_INIEXPRISCO, null=True, )
    eficepc = models.CharField(choices=CHOICES_S2240_EFICEPC_INIEXPRISCO, max_length=1, blank=True, null=True, )
    utilizepi = models.IntegerField(choices=CHOICES_S2240_UTILIZEPI_INIEXPRISCO, null=True, )

    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.codfatris) + ' - ' + unicode(self.tpaval) + ' - ' + unicode(self.utilizepc) + ' - ' + unicode(self.utilizepi)

    class Meta:

        # verbose_name = u'Fator de risco ao qual o trabalhador está exposto na atividade exercida no ambiente'
        db_table = r's2240_iniexprisco_fatrisco'
        managed = True # s2240_iniexprisco_fatrisco #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2240iniExpRiscofatRisco", u"Pode ver listagem do modelo S2240INIEXPRISCOFATRISCO"),
            ("can_see_data_s2240iniExpRiscofatRisco", u"Pode visualizar o conteúdo do modelo S2240INIEXPRISCOFATRISCO"),
            ("can_see_menu_s2240iniExpRiscofatRisco", u"Pode visualizar no menu o modelo S2240INIEXPRISCOFATRISCO"),
            ("can_print_list_s2240iniExpRiscofatRisco", u"Pode imprimir listagem do modelo S2240INIEXPRISCOFATRISCO"),
            ("can_print_data_s2240iniExpRiscofatRisco", u"Pode imprimir o conteúdo do modelo S2240INIEXPRISCOFATRISCO"), )

        ordering = [
            's2240_evtexprisco',
            'codfatris',
            'tpaval',
            'utilizepc',
            'utilizepi',]



class s2240iniExpRiscofatRiscoSerializer(ModelSerializer):

    class Meta:

        model = s2240iniExpRiscofatRisco
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2240iniExpRiscoinfoAmb(SoftDeletionModel):

    s2240_evtexprisco = models.ForeignKey('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco', )

    def evento(self):
        return self.s2240_evtexprisco.evento()
    codamb = models.CharField(max_length=30, null=True, )

    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.codamb)

    class Meta:

        # verbose_name = u'Informações relativas ao ambiente de trabalho'
        db_table = r's2240_iniexprisco_infoamb'
        managed = True # s2240_iniexprisco_infoamb #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2240iniExpRiscoinfoAmb", u"Pode ver listagem do modelo S2240INIEXPRISCOINFOAMB"),
            ("can_see_data_s2240iniExpRiscoinfoAmb", u"Pode visualizar o conteúdo do modelo S2240INIEXPRISCOINFOAMB"),
            ("can_see_menu_s2240iniExpRiscoinfoAmb", u"Pode visualizar no menu o modelo S2240INIEXPRISCOINFOAMB"),
            ("can_print_list_s2240iniExpRiscoinfoAmb", u"Pode imprimir listagem do modelo S2240INIEXPRISCOINFOAMB"),
            ("can_print_data_s2240iniExpRiscoinfoAmb", u"Pode imprimir o conteúdo do modelo S2240INIEXPRISCOINFOAMB"), )

        ordering = [
            's2240_evtexprisco',
            'codamb',]



class s2240iniExpRiscoinfoAmbSerializer(ModelSerializer):

    class Meta:

        model = s2240iniExpRiscoinfoAmb
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2240iniExpRiscoobs(SoftDeletionModel):

    s2240_evtexprisco = models.ForeignKey('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco', )

    def evento(self):
        return self.s2240_evtexprisco.evento()
    meterg = models.CharField(max_length=999, blank=True, null=True, )
    obscompl = models.CharField(max_length=999, blank=True, null=True, )
    observacao = models.CharField(max_length=999, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s2240_evtexprisco)

    class Meta:

        # verbose_name = u'Observações relativas a registros ambientais'
        db_table = r's2240_iniexprisco_obs'
        managed = True # s2240_iniexprisco_obs #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2240iniExpRiscoobs", u"Pode ver listagem do modelo S2240INIEXPRISCOOBS"),
            ("can_see_data_s2240iniExpRiscoobs", u"Pode visualizar o conteúdo do modelo S2240INIEXPRISCOOBS"),
            ("can_see_menu_s2240iniExpRiscoobs", u"Pode visualizar no menu o modelo S2240INIEXPRISCOOBS"),
            ("can_print_list_s2240iniExpRiscoobs", u"Pode imprimir listagem do modelo S2240INIEXPRISCOOBS"),
            ("can_print_data_s2240iniExpRiscoobs", u"Pode imprimir o conteúdo do modelo S2240INIEXPRISCOOBS"), )

        ordering = [
            's2240_evtexprisco',]



class s2240iniExpRiscoobsSerializer(ModelSerializer):

    class Meta:

        model = s2240iniExpRiscoobs
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2240iniExpRiscorespReg(SoftDeletionModel):

    s2240_evtexprisco = models.ForeignKey('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco', )

    def evento(self):
        return self.s2240_evtexprisco.evento()
    cpfresp = models.CharField(max_length=11, null=True, )
    nisresp = models.CharField(max_length=11, null=True, )
    nmresp = models.CharField(max_length=70, null=True, )
    ideoc = models.IntegerField(choices=CHOICES_S2240_IDEOC_INIEXPRISCO, null=True, )
    dscoc = models.CharField(max_length=20, blank=True, null=True, )
    nroc = models.CharField(max_length=14, null=True, )
    ufoc = models.CharField(choices=ESTADOS, max_length=2, null=True, )

    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.cpfresp) + ' - ' + unicode(self.nisresp) + ' - ' + unicode(self.nmresp) + ' - ' + unicode(self.ideoc) + ' - ' + unicode(self.nroc) + ' - ' + unicode(self.ufoc)

    class Meta:

        # verbose_name = u'Informações relativas ao responsável pelos registros ambientais'
        db_table = r's2240_iniexprisco_respreg'
        managed = True # s2240_iniexprisco_respreg #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2240iniExpRiscorespReg", u"Pode ver listagem do modelo S2240INIEXPRISCORESPREG"),
            ("can_see_data_s2240iniExpRiscorespReg", u"Pode visualizar o conteúdo do modelo S2240INIEXPRISCORESPREG"),
            ("can_see_menu_s2240iniExpRiscorespReg", u"Pode visualizar no menu o modelo S2240INIEXPRISCORESPREG"),
            ("can_print_list_s2240iniExpRiscorespReg", u"Pode imprimir listagem do modelo S2240INIEXPRISCORESPREG"),
            ("can_print_data_s2240iniExpRiscorespReg", u"Pode imprimir o conteúdo do modelo S2240INIEXPRISCORESPREG"), )

        ordering = [
            's2240_evtexprisco',
            'cpfresp',
            'nisresp',
            'nmresp',
            'ideoc',
            'nroc',
            'ufoc',]



class s2240iniExpRiscorespRegSerializer(ModelSerializer):

    class Meta:

        model = s2240iniExpRiscorespReg
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')