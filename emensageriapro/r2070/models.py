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
from emensageriapro.r2070.choices import *
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





class r2070compJud(SoftDeletionModel):

    r2070_pgtopf = models.ForeignKey('r2070.r2070pgtoPF',
        related_name='%(class)s_r2070_pgtopf', )

    def evento(self):
        return self.r2070_pgtopf.evento()
    vlrcompanocalend = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrcompanoant = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_pgtopf)

    class Meta:

        # verbose_name = u'Compensação Judicial'
        db_table = r'r2070_compjud'
        managed = True # r2070_compjud #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070compJud", u"Pode ver listagem do modelo R2070COMPJUD"),
            ("can_see_data_r2070compJud", u"Pode visualizar o conteúdo do modelo R2070COMPJUD"),
            ("can_see_menu_r2070compJud", u"Pode visualizar no menu o modelo R2070COMPJUD"),
            ("can_print_list_r2070compJud", u"Pode imprimir listagem do modelo R2070COMPJUD"),
            ("can_print_data_r2070compJud", u"Pode imprimir o conteúdo do modelo R2070COMPJUD"), )

        ordering = [
            'r2070_pgtopf',]



class r2070compJudSerializer(ModelSerializer):

    class Meta:

        model = r2070compJud
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070depJudicial(SoftDeletionModel):

    r2070_pgtopf = models.ForeignKey('r2070.r2070pgtoPF',
        related_name='%(class)s_r2070_pgtopf', )

    def evento(self):
        return self.r2070_pgtopf.evento()
    vlrdepjudicial = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_pgtopf)

    class Meta:

        # verbose_name = u'Depósito Judicial'
        db_table = r'r2070_depjudicial'
        managed = True # r2070_depjudicial #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070depJudicial", u"Pode ver listagem do modelo R2070DEPJUDICIAL"),
            ("can_see_data_r2070depJudicial", u"Pode visualizar o conteúdo do modelo R2070DEPJUDICIAL"),
            ("can_see_menu_r2070depJudicial", u"Pode visualizar no menu o modelo R2070DEPJUDICIAL"),
            ("can_print_list_r2070depJudicial", u"Pode imprimir listagem do modelo R2070DEPJUDICIAL"),
            ("can_print_data_r2070depJudicial", u"Pode imprimir o conteúdo do modelo R2070DEPJUDICIAL"), )

        ordering = [
            'r2070_pgtopf',]



class r2070depJudicialSerializer(ModelSerializer):

    class Meta:

        model = r2070depJudicial
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070detCompet(SoftDeletionModel):

    r2070_pgtopf = models.ForeignKey('r2070.r2070pgtoPF',
        related_name='%(class)s_r2070_pgtopf', )

    def evento(self):
        return self.r2070_pgtopf.evento()
    indperreferencia = models.IntegerField(choices=CHOICES_R2070_INDPERREFERENCIA, null=True, )
    perrefpagto = models.CharField(max_length=7, null=True, )
    vlrrendtributavel = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_pgtopf) + ' - ' + unicode(self.indperreferencia) + ' - ' + unicode(self.perrefpagto) + ' - ' + unicode(self.vlrrendtributavel)

    class Meta:

        # verbose_name = u'Detalhamento das Competências'
        db_table = r'r2070_detcompet'
        managed = True # r2070_detcompet #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070detCompet", u"Pode ver listagem do modelo R2070DETCOMPET"),
            ("can_see_data_r2070detCompet", u"Pode visualizar o conteúdo do modelo R2070DETCOMPET"),
            ("can_see_menu_r2070detCompet", u"Pode visualizar no menu o modelo R2070DETCOMPET"),
            ("can_print_list_r2070detCompet", u"Pode imprimir listagem do modelo R2070DETCOMPET"),
            ("can_print_data_r2070detCompet", u"Pode imprimir o conteúdo do modelo R2070DETCOMPET"), )

        ordering = [
            'r2070_pgtopf',
            'indperreferencia',
            'perrefpagto',
            'vlrrendtributavel',]



class r2070detCompetSerializer(ModelSerializer):

    class Meta:

        model = r2070detCompet
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070detDeducao(SoftDeletionModel):

    r2070_pgtopf = models.ForeignKey('r2070.r2070pgtoPF',
        related_name='%(class)s_r2070_pgtopf', )

    def evento(self):
        return self.r2070_pgtopf.evento()
    indtpdeducao = models.IntegerField(choices=CHOICES_R2070_INDTPDEDUCAO, null=True, )
    vlrdeducao = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_pgtopf) + ' - ' + unicode(self.indtpdeducao) + ' - ' + unicode(self.vlrdeducao)

    class Meta:

        # verbose_name = u'Detalhamento das Deduções'
        db_table = r'r2070_detdeducao'
        managed = True # r2070_detdeducao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070detDeducao", u"Pode ver listagem do modelo R2070DETDEDUCAO"),
            ("can_see_data_r2070detDeducao", u"Pode visualizar o conteúdo do modelo R2070DETDEDUCAO"),
            ("can_see_menu_r2070detDeducao", u"Pode visualizar no menu o modelo R2070DETDEDUCAO"),
            ("can_print_list_r2070detDeducao", u"Pode imprimir listagem do modelo R2070DETDEDUCAO"),
            ("can_print_data_r2070detDeducao", u"Pode imprimir o conteúdo do modelo R2070DETDEDUCAO"), )

        ordering = [
            'r2070_pgtopf',
            'indtpdeducao',
            'vlrdeducao',]



class r2070detDeducaoSerializer(ModelSerializer):

    class Meta:

        model = r2070detDeducao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070ideEstab(SoftDeletionModel):

    r2070_evtpgtosdivs = models.ForeignKey('efdreinf.r2070evtPgtosDivs',
        related_name='%(class)s_r2070_evtpgtosdivs', )

    def evento(self):
        return self.r2070_evtpgtosdivs.evento()
    tpinsc = models.IntegerField(choices=CHOICES_R2070_TPINSC, null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_evtpgtosdivs) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)

    class Meta:

        # verbose_name = u'Identificação dos estabelecimentos da associação desportiva que receberam os recursos'
        db_table = r'r2070_ideestab'
        managed = True # r2070_ideestab #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070ideEstab", u"Pode ver listagem do modelo R2070IDEESTAB"),
            ("can_see_data_r2070ideEstab", u"Pode visualizar o conteúdo do modelo R2070IDEESTAB"),
            ("can_see_menu_r2070ideEstab", u"Pode visualizar no menu o modelo R2070IDEESTAB"),
            ("can_print_list_r2070ideEstab", u"Pode imprimir listagem do modelo R2070IDEESTAB"),
            ("can_print_data_r2070ideEstab", u"Pode imprimir o conteúdo do modelo R2070IDEESTAB"), )

        ordering = [
            'r2070_evtpgtosdivs',
            'tpinsc',
            'nrinsc',]



class r2070ideEstabSerializer(ModelSerializer):

    class Meta:

        model = r2070ideEstab
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070infoMolestia(SoftDeletionModel):

    r2070_evtpgtosdivs = models.ForeignKey('efdreinf.r2070evtPgtosDivs',
        related_name='%(class)s_r2070_evtpgtosdivs', )

    def evento(self):
        return self.r2070_evtpgtosdivs.evento()
    dtlaudo = models.DateField(null=True, )

    def __unicode__(self):
        return unicode(self.r2070_evtpgtosdivs) + ' - ' + unicode(self.dtlaudo)

    class Meta:

        # verbose_name = u'Informações de Beneficiário portador de moléstia grave'
        db_table = r'r2070_infomolestia'
        managed = True # r2070_infomolestia #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070infoMolestia", u"Pode ver listagem do modelo R2070INFOMOLESTIA"),
            ("can_see_data_r2070infoMolestia", u"Pode visualizar o conteúdo do modelo R2070INFOMOLESTIA"),
            ("can_see_menu_r2070infoMolestia", u"Pode visualizar no menu o modelo R2070INFOMOLESTIA"),
            ("can_print_list_r2070infoMolestia", u"Pode imprimir listagem do modelo R2070INFOMOLESTIA"),
            ("can_print_data_r2070infoMolestia", u"Pode imprimir o conteúdo do modelo R2070INFOMOLESTIA"), )

        ordering = [
            'r2070_evtpgtosdivs',
            'dtlaudo',]



class r2070infoMolestiaSerializer(ModelSerializer):

    class Meta:

        model = r2070infoMolestia
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070infoProcJud(SoftDeletionModel):

    r2070_pgtopf = models.ForeignKey('r2070.r2070pgtoPF',
        related_name='%(class)s_r2070_pgtopf', )

    def evento(self):
        return self.r2070_pgtopf.evento()
    nrprocjud = models.CharField(max_length=21, null=True, )
    codsusp = models.IntegerField(blank=True, null=True, )
    indorigemrecursos = models.IntegerField(choices=CHOICES_R2070_INDORIGEMRECURSOS_INFOPROCJUD, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_pgtopf) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.indorigemrecursos)

    class Meta:

        # verbose_name = u'Informações Complementares - Demais rendimentos decorrentes de Decisão Judicial'
        db_table = r'r2070_infoprocjud'
        managed = True # r2070_infoprocjud #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070infoProcJud", u"Pode ver listagem do modelo R2070INFOPROCJUD"),
            ("can_see_data_r2070infoProcJud", u"Pode visualizar o conteúdo do modelo R2070INFOPROCJUD"),
            ("can_see_menu_r2070infoProcJud", u"Pode visualizar no menu o modelo R2070INFOPROCJUD"),
            ("can_print_list_r2070infoProcJud", u"Pode imprimir listagem do modelo R2070INFOPROCJUD"),
            ("can_print_data_r2070infoProcJud", u"Pode imprimir o conteúdo do modelo R2070INFOPROCJUD"), )

        ordering = [
            'r2070_pgtopf',
            'nrprocjud',
            'indorigemrecursos',]



class r2070infoProcJudSerializer(ModelSerializer):

    class Meta:

        model = r2070infoProcJud
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070infoProcJuddespProcJud(SoftDeletionModel):

    r2070_infoprocjud = models.ForeignKey('r2070.r2070infoProcJud',
        related_name='%(class)s_r2070_infoprocjud', )

    def evento(self):
        return self.r2070_infoprocjud.evento()
    vlrdespcustas = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrdespadvogados = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_infoprocjud) + ' - ' + unicode(self.vlrdespcustas) + ' - ' + unicode(self.vlrdespadvogados)

    class Meta:

        # verbose_name = u'Detalhamento das despesas de processo judicial'
        db_table = r'r2070_infoprocjud_despprocjud'
        managed = True # r2070_infoprocjud_despprocjud #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070infoProcJuddespProcJud", u"Pode ver listagem do modelo R2070INFOPROCJUDDESPPROCJUD"),
            ("can_see_data_r2070infoProcJuddespProcJud", u"Pode visualizar o conteúdo do modelo R2070INFOPROCJUDDESPPROCJUD"),
            ("can_see_menu_r2070infoProcJuddespProcJud", u"Pode visualizar no menu o modelo R2070INFOPROCJUDDESPPROCJUD"),
            ("can_print_list_r2070infoProcJuddespProcJud", u"Pode imprimir listagem do modelo R2070INFOPROCJUDDESPPROCJUD"),
            ("can_print_data_r2070infoProcJuddespProcJud", u"Pode imprimir o conteúdo do modelo R2070INFOPROCJUDDESPPROCJUD"), )

        ordering = [
            'r2070_infoprocjud',
            'vlrdespcustas',
            'vlrdespadvogados',]



class r2070infoProcJuddespProcJudSerializer(ModelSerializer):

    class Meta:

        model = r2070infoProcJuddespProcJud
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070infoProcJudideAdvogado(SoftDeletionModel):

    r2070_infoprocjud_despprocjud = models.ForeignKey('r2070.r2070infoProcJuddespProcJud',
        related_name='%(class)s_r2070_infoprocjud_despprocjud', )

    def evento(self):
        return self.r2070_infoprocjud_despprocjud.evento()
    tpinscadvogado = models.IntegerField(choices=CHOICES_R2070_TPINSCADVOGADO_INFOPROCJUD, null=True, )
    nrinscadvogado = models.CharField(max_length=14, null=True, )
    vlradvogado = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_infoprocjud_despprocjud) + ' - ' + unicode(self.tpinscadvogado) + ' - ' + unicode(self.nrinscadvogado) + ' - ' + unicode(self.vlradvogado)

    class Meta:

        # verbose_name = u'Identificação do Advogado'
        db_table = r'r2070_infoprocjud_ideadvogado'
        managed = True # r2070_infoprocjud_ideadvogado #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070infoProcJudideAdvogado", u"Pode ver listagem do modelo R2070INFOPROCJUDIDEADVOGADO"),
            ("can_see_data_r2070infoProcJudideAdvogado", u"Pode visualizar o conteúdo do modelo R2070INFOPROCJUDIDEADVOGADO"),
            ("can_see_menu_r2070infoProcJudideAdvogado", u"Pode visualizar no menu o modelo R2070INFOPROCJUDIDEADVOGADO"),
            ("can_print_list_r2070infoProcJudideAdvogado", u"Pode imprimir listagem do modelo R2070INFOPROCJUDIDEADVOGADO"),
            ("can_print_data_r2070infoProcJudideAdvogado", u"Pode imprimir o conteúdo do modelo R2070INFOPROCJUDIDEADVOGADO"), )

        ordering = [
            'r2070_infoprocjud_despprocjud',
            'tpinscadvogado',
            'nrinscadvogado',
            'vlradvogado',]



class r2070infoProcJudideAdvogadoSerializer(ModelSerializer):

    class Meta:

        model = r2070infoProcJudideAdvogado
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070infoProcJudorigemRecursos(SoftDeletionModel):

    r2070_infoprocjud = models.ForeignKey('r2070.r2070infoProcJud',
        related_name='%(class)s_r2070_infoprocjud', )

    def evento(self):
        return self.r2070_infoprocjud.evento()
    cnpjorigemrecursos = models.CharField(max_length=14, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_infoprocjud) + ' - ' + unicode(self.cnpjorigemrecursos)

    class Meta:

        # verbose_name = u'Identificação da origem dos recursos'
        db_table = r'r2070_infoprocjud_origemrecursos'
        managed = True # r2070_infoprocjud_origemrecursos #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070infoProcJudorigemRecursos", u"Pode ver listagem do modelo R2070INFOPROCJUDORIGEMRECURSOS"),
            ("can_see_data_r2070infoProcJudorigemRecursos", u"Pode visualizar o conteúdo do modelo R2070INFOPROCJUDORIGEMRECURSOS"),
            ("can_see_menu_r2070infoProcJudorigemRecursos", u"Pode visualizar no menu o modelo R2070INFOPROCJUDORIGEMRECURSOS"),
            ("can_print_list_r2070infoProcJudorigemRecursos", u"Pode imprimir listagem do modelo R2070INFOPROCJUDORIGEMRECURSOS"),
            ("can_print_data_r2070infoProcJudorigemRecursos", u"Pode imprimir o conteúdo do modelo R2070INFOPROCJUDORIGEMRECURSOS"), )

        ordering = [
            'r2070_infoprocjud',
            'cnpjorigemrecursos',]



class r2070infoProcJudorigemRecursosSerializer(ModelSerializer):

    class Meta:

        model = r2070infoProcJudorigemRecursos
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070infoRRA(SoftDeletionModel):

    r2070_pgtopf = models.ForeignKey('r2070.r2070pgtoPF',
        related_name='%(class)s_r2070_pgtopf', )

    def evento(self):
        return self.r2070_pgtopf.evento()
    tpprocrra = models.IntegerField(choices=CHOICES_R2070_TPPROCRRA_INFORRA, blank=True, null=True, )
    nrprocrra = models.CharField(max_length=21, blank=True, null=True, )
    codsusp = models.IntegerField(blank=True, null=True, )
    natrra = models.CharField(max_length=50, blank=True, null=True, )
    qtdmesesrra = models.IntegerField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_pgtopf)

    class Meta:

        # verbose_name = u'Informações Complementares - Rendimentos Recebidos Acumuladamente'
        db_table = r'r2070_inforra'
        managed = True # r2070_inforra #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070infoRRA", u"Pode ver listagem do modelo R2070INFORRA"),
            ("can_see_data_r2070infoRRA", u"Pode visualizar o conteúdo do modelo R2070INFORRA"),
            ("can_see_menu_r2070infoRRA", u"Pode visualizar no menu o modelo R2070INFORRA"),
            ("can_print_list_r2070infoRRA", u"Pode imprimir listagem do modelo R2070INFORRA"),
            ("can_print_data_r2070infoRRA", u"Pode imprimir o conteúdo do modelo R2070INFORRA"), )

        ordering = [
            'r2070_pgtopf',]



class r2070infoRRASerializer(ModelSerializer):

    class Meta:

        model = r2070infoRRA
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070infoRRAdespProcJud(SoftDeletionModel):

    r2070_inforra = models.ForeignKey('r2070.r2070infoRRA',
        related_name='%(class)s_r2070_inforra', )

    def evento(self):
        return self.r2070_inforra.evento()
    vlrdespcustas = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrdespadvogados = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_inforra) + ' - ' + unicode(self.vlrdespcustas) + ' - ' + unicode(self.vlrdespadvogados)

    class Meta:

        # verbose_name = u'Detalhamento das despesas de processo judicial'
        db_table = r'r2070_inforra_despprocjud'
        managed = True # r2070_inforra_despprocjud #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070infoRRAdespProcJud", u"Pode ver listagem do modelo R2070INFORRADESPPROCJUD"),
            ("can_see_data_r2070infoRRAdespProcJud", u"Pode visualizar o conteúdo do modelo R2070INFORRADESPPROCJUD"),
            ("can_see_menu_r2070infoRRAdespProcJud", u"Pode visualizar no menu o modelo R2070INFORRADESPPROCJUD"),
            ("can_print_list_r2070infoRRAdespProcJud", u"Pode imprimir listagem do modelo R2070INFORRADESPPROCJUD"),
            ("can_print_data_r2070infoRRAdespProcJud", u"Pode imprimir o conteúdo do modelo R2070INFORRADESPPROCJUD"), )

        ordering = [
            'r2070_inforra',
            'vlrdespcustas',
            'vlrdespadvogados',]



class r2070infoRRAdespProcJudSerializer(ModelSerializer):

    class Meta:

        model = r2070infoRRAdespProcJud
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070infoRRAideAdvogado(SoftDeletionModel):

    r2070_inforra_despprocjud = models.ForeignKey('r2070.r2070infoRRAdespProcJud',
        related_name='%(class)s_r2070_inforra_despprocjud', )

    def evento(self):
        return self.r2070_inforra_despprocjud.evento()
    tpinscadvogado = models.IntegerField(choices=CHOICES_R2070_TPINSCADVOGADO_INFORRA, null=True, )
    nrinscadvogado = models.CharField(max_length=14, null=True, )
    vlradvogado = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_inforra_despprocjud) + ' - ' + unicode(self.tpinscadvogado) + ' - ' + unicode(self.nrinscadvogado) + ' - ' + unicode(self.vlradvogado)

    class Meta:

        # verbose_name = u'Identificação do Advogado'
        db_table = r'r2070_inforra_ideadvogado'
        managed = True # r2070_inforra_ideadvogado #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070infoRRAideAdvogado", u"Pode ver listagem do modelo R2070INFORRAIDEADVOGADO"),
            ("can_see_data_r2070infoRRAideAdvogado", u"Pode visualizar o conteúdo do modelo R2070INFORRAIDEADVOGADO"),
            ("can_see_menu_r2070infoRRAideAdvogado", u"Pode visualizar no menu o modelo R2070INFORRAIDEADVOGADO"),
            ("can_print_list_r2070infoRRAideAdvogado", u"Pode imprimir listagem do modelo R2070INFORRAIDEADVOGADO"),
            ("can_print_data_r2070infoRRAideAdvogado", u"Pode imprimir o conteúdo do modelo R2070INFORRAIDEADVOGADO"), )

        ordering = [
            'r2070_inforra_despprocjud',
            'tpinscadvogado',
            'nrinscadvogado',
            'vlradvogado',]



class r2070infoRRAideAdvogadoSerializer(ModelSerializer):

    class Meta:

        model = r2070infoRRAideAdvogado
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070infoResidExt(SoftDeletionModel):

    r2070_evtpgtosdivs = models.ForeignKey('efdreinf.r2070evtPgtosDivs',
        related_name='%(class)s_r2070_evtpgtosdivs', )

    def evento(self):
        return self.r2070_evtpgtosdivs.evento()
    paisresid = models.TextField(null=True, )
    dsclograd = models.CharField(max_length=80, null=True, )
    nrlograd = models.CharField(max_length=10, blank=True, null=True, )
    complem = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=60, blank=True, null=True, )
    cidade = models.CharField(max_length=30, blank=True, null=True, )
    codpostal = models.CharField(max_length=12, blank=True, null=True, )
    indnif = models.IntegerField(choices=CHOICES_R2070_INDNIF, null=True, )
    nifbenef = models.CharField(max_length=20, blank=True, null=True, )
    relfontepagad = models.CharField(choices=CHOICES_EFDREINFINFORMACOESBENEFICIARIOSEXTERIOR, max_length=3, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_evtpgtosdivs) + ' - ' + unicode(self.paisresid) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.indnif)

    class Meta:

        # verbose_name = u'Informações complementares de beneficiário residente ou domiciliado no exterior'
        db_table = r'r2070_inforesidext'
        managed = True # r2070_inforesidext #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070infoResidExt", u"Pode ver listagem do modelo R2070INFORESIDEXT"),
            ("can_see_data_r2070infoResidExt", u"Pode visualizar o conteúdo do modelo R2070INFORESIDEXT"),
            ("can_see_menu_r2070infoResidExt", u"Pode visualizar no menu o modelo R2070INFORESIDEXT"),
            ("can_print_list_r2070infoResidExt", u"Pode imprimir listagem do modelo R2070INFORESIDEXT"),
            ("can_print_data_r2070infoResidExt", u"Pode imprimir o conteúdo do modelo R2070INFORESIDEXT"), )

        ordering = [
            'r2070_evtpgtosdivs',
            'paisresid',
            'dsclograd',
            'indnif',]



class r2070infoResidExtSerializer(ModelSerializer):

    class Meta:

        model = r2070infoResidExt
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070pgtoPF(SoftDeletionModel):

    r2070_pgtoresidbr = models.ForeignKey('r2070.r2070pgtoResidBR',
        related_name='%(class)s_r2070_pgtoresidbr', )

    def evento(self):
        return self.r2070_pgtoresidbr.evento()
    dtpgto = models.DateField(null=True, )
    indsuspexig = models.CharField(choices=CHOICES_R2070_INDSUSPEXIG, max_length=1, null=True, )
    inddecterceiro = models.CharField(choices=CHOICES_R2070_INDDECTERCEIRO, max_length=1, null=True, )
    vlrrendtributavel = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrirrf = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_pgtoresidbr) + ' - ' + unicode(self.dtpgto) + ' - ' + unicode(self.indsuspexig) + ' - ' + unicode(self.inddecterceiro) + ' - ' + unicode(self.vlrrendtributavel) + ' - ' + unicode(self.vlrirrf)

    class Meta:

        # verbose_name = u'Beneficiário Pessoa Física - Residente no Brasil'
        db_table = r'r2070_pgtopf'
        managed = True # r2070_pgtopf #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070pgtoPF", u"Pode ver listagem do modelo R2070PGTOPF"),
            ("can_see_data_r2070pgtoPF", u"Pode visualizar o conteúdo do modelo R2070PGTOPF"),
            ("can_see_menu_r2070pgtoPF", u"Pode visualizar no menu o modelo R2070PGTOPF"),
            ("can_print_list_r2070pgtoPF", u"Pode imprimir listagem do modelo R2070PGTOPF"),
            ("can_print_data_r2070pgtoPF", u"Pode imprimir o conteúdo do modelo R2070PGTOPF"), )

        ordering = [
            'r2070_pgtoresidbr',
            'dtpgto',
            'indsuspexig',
            'inddecterceiro',
            'vlrrendtributavel',
            'vlrirrf',]



class r2070pgtoPFSerializer(ModelSerializer):

    class Meta:

        model = r2070pgtoPF
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070pgtoPJ(SoftDeletionModel):

    r2070_pgtoresidbr = models.ForeignKey('r2070.r2070pgtoResidBR',
        related_name='%(class)s_r2070_pgtoresidbr', )

    def evento(self):
        return self.r2070_pgtoresidbr.evento()
    dtpagto = models.DateField(null=True, )
    vlrrendtributavel = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_pgtoresidbr) + ' - ' + unicode(self.dtpagto) + ' - ' + unicode(self.vlrrendtributavel) + ' - ' + unicode(self.vlrret)

    class Meta:

        # verbose_name = u'Pagamento a Beneficiário Pessoa Jurídica - Domiciliado no Brasil'
        db_table = r'r2070_pgtopj'
        managed = True # r2070_pgtopj #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070pgtoPJ", u"Pode ver listagem do modelo R2070PGTOPJ"),
            ("can_see_data_r2070pgtoPJ", u"Pode visualizar o conteúdo do modelo R2070PGTOPJ"),
            ("can_see_menu_r2070pgtoPJ", u"Pode visualizar no menu o modelo R2070PGTOPJ"),
            ("can_print_list_r2070pgtoPJ", u"Pode imprimir listagem do modelo R2070PGTOPJ"),
            ("can_print_data_r2070pgtoPJ", u"Pode imprimir o conteúdo do modelo R2070PGTOPJ"), )

        ordering = [
            'r2070_pgtoresidbr',
            'dtpagto',
            'vlrrendtributavel',
            'vlrret',]



class r2070pgtoPJSerializer(ModelSerializer):

    class Meta:

        model = r2070pgtoPJ
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070pgtoPJdespProcJud(SoftDeletionModel):

    r2070_pgtopj_infoprocjud = models.ForeignKey('r2070.r2070pgtoPJinfoProcJud',
        related_name='%(class)s_r2070_pgtopj_infoprocjud', )

    def evento(self):
        return self.r2070_pgtopj_infoprocjud.evento()
    vlrdespcustas = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrdespadvogados = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_pgtopj_infoprocjud) + ' - ' + unicode(self.vlrdespcustas) + ' - ' + unicode(self.vlrdespadvogados)

    class Meta:

        # verbose_name = u'Detalhamento das despesas de processo judicial'
        db_table = r'r2070_pgtopj_despprocjud'
        managed = True # r2070_pgtopj_despprocjud #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070pgtoPJdespProcJud", u"Pode ver listagem do modelo R2070PGTOPJDESPPROCJUD"),
            ("can_see_data_r2070pgtoPJdespProcJud", u"Pode visualizar o conteúdo do modelo R2070PGTOPJDESPPROCJUD"),
            ("can_see_menu_r2070pgtoPJdespProcJud", u"Pode visualizar no menu o modelo R2070PGTOPJDESPPROCJUD"),
            ("can_print_list_r2070pgtoPJdespProcJud", u"Pode imprimir listagem do modelo R2070PGTOPJDESPPROCJUD"),
            ("can_print_data_r2070pgtoPJdespProcJud", u"Pode imprimir o conteúdo do modelo R2070PGTOPJDESPPROCJUD"), )

        ordering = [
            'r2070_pgtopj_infoprocjud',
            'vlrdespcustas',
            'vlrdespadvogados',]



class r2070pgtoPJdespProcJudSerializer(ModelSerializer):

    class Meta:

        model = r2070pgtoPJdespProcJud
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070pgtoPJideAdvogado(SoftDeletionModel):

    r2070_pgtopj_despprocjud = models.ForeignKey('r2070.r2070pgtoPJdespProcJud',
        related_name='%(class)s_r2070_pgtopj_despprocjud', )

    def evento(self):
        return self.r2070_pgtopj_despprocjud.evento()
    tpinscadvogado = models.IntegerField(choices=CHOICES_R2070_TPINSCADVOGADO_PGTOPJ, null=True, )
    nrinscadvogado = models.CharField(max_length=14, null=True, )
    vlradvogado = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_pgtopj_despprocjud) + ' - ' + unicode(self.tpinscadvogado) + ' - ' + unicode(self.nrinscadvogado) + ' - ' + unicode(self.vlradvogado)

    class Meta:

        # verbose_name = u'Identificação do Advogado'
        db_table = r'r2070_pgtopj_ideadvogado'
        managed = True # r2070_pgtopj_ideadvogado #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070pgtoPJideAdvogado", u"Pode ver listagem do modelo R2070PGTOPJIDEADVOGADO"),
            ("can_see_data_r2070pgtoPJideAdvogado", u"Pode visualizar o conteúdo do modelo R2070PGTOPJIDEADVOGADO"),
            ("can_see_menu_r2070pgtoPJideAdvogado", u"Pode visualizar no menu o modelo R2070PGTOPJIDEADVOGADO"),
            ("can_print_list_r2070pgtoPJideAdvogado", u"Pode imprimir listagem do modelo R2070PGTOPJIDEADVOGADO"),
            ("can_print_data_r2070pgtoPJideAdvogado", u"Pode imprimir o conteúdo do modelo R2070PGTOPJIDEADVOGADO"), )

        ordering = [
            'r2070_pgtopj_despprocjud',
            'tpinscadvogado',
            'nrinscadvogado',
            'vlradvogado',]



class r2070pgtoPJideAdvogadoSerializer(ModelSerializer):

    class Meta:

        model = r2070pgtoPJideAdvogado
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070pgtoPJinfoProcJud(SoftDeletionModel):

    r2070_pgtopj = models.ForeignKey('r2070.r2070pgtoPJ',
        related_name='%(class)s_r2070_pgtopj', )

    def evento(self):
        return self.r2070_pgtopj.evento()
    nrprocjud = models.CharField(max_length=21, null=True, )
    codsusp = models.IntegerField(blank=True, null=True, )
    indorigemrecursos = models.IntegerField(choices=CHOICES_R2070_INDORIGEMRECURSOS_PGTOPJ, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_pgtopj) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.indorigemrecursos)

    class Meta:

        # verbose_name = u'Informações Complementares - Demais rendimentos decorrentes de Decisão Judicial'
        db_table = r'r2070_pgtopj_infoprocjud'
        managed = True # r2070_pgtopj_infoprocjud #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070pgtoPJinfoProcJud", u"Pode ver listagem do modelo R2070PGTOPJINFOPROCJUD"),
            ("can_see_data_r2070pgtoPJinfoProcJud", u"Pode visualizar o conteúdo do modelo R2070PGTOPJINFOPROCJUD"),
            ("can_see_menu_r2070pgtoPJinfoProcJud", u"Pode visualizar no menu o modelo R2070PGTOPJINFOPROCJUD"),
            ("can_print_list_r2070pgtoPJinfoProcJud", u"Pode imprimir listagem do modelo R2070PGTOPJINFOPROCJUD"),
            ("can_print_data_r2070pgtoPJinfoProcJud", u"Pode imprimir o conteúdo do modelo R2070PGTOPJINFOPROCJUD"), )

        ordering = [
            'r2070_pgtopj',
            'nrprocjud',
            'indorigemrecursos',]



class r2070pgtoPJinfoProcJudSerializer(ModelSerializer):

    class Meta:

        model = r2070pgtoPJinfoProcJud
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070pgtoPJorigemRecursos(SoftDeletionModel):

    r2070_pgtopj_infoprocjud = models.ForeignKey('r2070.r2070pgtoPJinfoProcJud',
        related_name='%(class)s_r2070_pgtopj_infoprocjud', )

    def evento(self):
        return self.r2070_pgtopj_infoprocjud.evento()
    cnpjorigemrecursos = models.CharField(max_length=14, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_pgtopj_infoprocjud) + ' - ' + unicode(self.cnpjorigemrecursos)

    class Meta:

        # verbose_name = u'Identificação da origem dos recursos'
        db_table = r'r2070_pgtopj_origemrecursos'
        managed = True # r2070_pgtopj_origemrecursos #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070pgtoPJorigemRecursos", u"Pode ver listagem do modelo R2070PGTOPJORIGEMRECURSOS"),
            ("can_see_data_r2070pgtoPJorigemRecursos", u"Pode visualizar o conteúdo do modelo R2070PGTOPJORIGEMRECURSOS"),
            ("can_see_menu_r2070pgtoPJorigemRecursos", u"Pode visualizar no menu o modelo R2070PGTOPJORIGEMRECURSOS"),
            ("can_print_list_r2070pgtoPJorigemRecursos", u"Pode imprimir listagem do modelo R2070PGTOPJORIGEMRECURSOS"),
            ("can_print_data_r2070pgtoPJorigemRecursos", u"Pode imprimir o conteúdo do modelo R2070PGTOPJORIGEMRECURSOS"), )

        ordering = [
            'r2070_pgtopj_infoprocjud',
            'cnpjorigemrecursos',]



class r2070pgtoPJorigemRecursosSerializer(ModelSerializer):

    class Meta:

        model = r2070pgtoPJorigemRecursos
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070pgtoResidBR(SoftDeletionModel):

    r2070_ideestab = models.ForeignKey('r2070.r2070ideEstab',
        related_name='%(class)s_r2070_ideestab', )

    def evento(self):
        return self.r2070_ideestab.evento()

    def __unicode__(self):
        return unicode(self.r2070_ideestab)

    class Meta:

        # verbose_name = u'Pagamento a Pessoa Física ou Jurídica residente ou domiciliada no Brasil'
        db_table = r'r2070_pgtoresidbr'
        managed = True # r2070_pgtoresidbr #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070pgtoResidBR", u"Pode ver listagem do modelo R2070PGTORESIDBR"),
            ("can_see_data_r2070pgtoResidBR", u"Pode visualizar o conteúdo do modelo R2070PGTORESIDBR"),
            ("can_see_menu_r2070pgtoResidBR", u"Pode visualizar no menu o modelo R2070PGTORESIDBR"),
            ("can_print_list_r2070pgtoResidBR", u"Pode imprimir listagem do modelo R2070PGTORESIDBR"),
            ("can_print_data_r2070pgtoResidBR", u"Pode imprimir o conteúdo do modelo R2070PGTORESIDBR"), )

        ordering = [
            'r2070_ideestab',]



class r2070pgtoResidBRSerializer(ModelSerializer):

    class Meta:

        model = r2070pgtoResidBR
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070pgtoResidExt(SoftDeletionModel):

    r2070_ideestab = models.ForeignKey('r2070.r2070ideEstab',
        related_name='%(class)s_r2070_ideestab', )

    def evento(self):
        return self.r2070_ideestab.evento()
    dtpagto = models.DateField(null=True, )
    tprendimento = models.IntegerField(choices=CHOICES_EFDREINFRENDIMENTOSBENEFICIARIOSEXTERIOR, null=True, )
    formatributacao = models.CharField(choices=CHOICES_EFDREINFRENDIMENTOSBENEFICIARIOSEXTERIORTRIBUTACAO, max_length=2, null=True, )
    vlrpgto = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_ideestab) + ' - ' + unicode(self.dtpagto) + ' - ' + unicode(self.tprendimento) + ' - ' + unicode(self.formatributacao) + ' - ' + unicode(self.vlrpgto) + ' - ' + unicode(self.vlrret)

    class Meta:

        # verbose_name = u'Pagamento a não residente ou domiciliado no exterior'
        db_table = r'r2070_pgtoresidext'
        managed = True # r2070_pgtoresidext #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070pgtoResidExt", u"Pode ver listagem do modelo R2070PGTORESIDEXT"),
            ("can_see_data_r2070pgtoResidExt", u"Pode visualizar o conteúdo do modelo R2070PGTORESIDEXT"),
            ("can_see_menu_r2070pgtoResidExt", u"Pode visualizar no menu o modelo R2070PGTORESIDEXT"),
            ("can_print_list_r2070pgtoResidExt", u"Pode imprimir listagem do modelo R2070PGTORESIDEXT"),
            ("can_print_data_r2070pgtoResidExt", u"Pode imprimir o conteúdo do modelo R2070PGTORESIDEXT"), )

        ordering = [
            'r2070_ideestab',
            'dtpagto',
            'tprendimento',
            'formatributacao',
            'vlrpgto',
            'vlrret',]



class r2070pgtoResidExtSerializer(ModelSerializer):

    class Meta:

        model = r2070pgtoResidExt
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2070rendIsento(SoftDeletionModel):

    r2070_pgtopf = models.ForeignKey('r2070.r2070pgtoPF',
        related_name='%(class)s_r2070_pgtopf', )

    def evento(self):
        return self.r2070_pgtopf.evento()
    tpisencao = models.IntegerField(choices=CHOICES_R2070_TPISENCAO, null=True, )
    vlrisento = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    descrendimento = models.CharField(max_length=100, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.r2070_pgtopf) + ' - ' + unicode(self.tpisencao) + ' - ' + unicode(self.vlrisento)

    class Meta:

        # verbose_name = u'Rendimentos Isentos/Não Tributáveis'
        db_table = r'r2070_rendisento'
        managed = True # r2070_rendisento #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2070rendIsento", u"Pode ver listagem do modelo R2070RENDISENTO"),
            ("can_see_data_r2070rendIsento", u"Pode visualizar o conteúdo do modelo R2070RENDISENTO"),
            ("can_see_menu_r2070rendIsento", u"Pode visualizar no menu o modelo R2070RENDISENTO"),
            ("can_print_list_r2070rendIsento", u"Pode imprimir listagem do modelo R2070RENDISENTO"),
            ("can_print_data_r2070rendIsento", u"Pode imprimir o conteúdo do modelo R2070RENDISENTO"), )

        ordering = [
            'r2070_pgtopf',
            'tpisencao',
            'vlrisento',]



class r2070rendIsentoSerializer(ModelSerializer):

    class Meta:

        model = r2070rendIsento
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')