#coding: utf-8
# © 2018 Marcelo Medeiros de Vasconcellos
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

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

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__credits__ = ["Marcelo Medeiros de Vasconcellos"]
__version__ = "1.0.0"
__maintainer__ = "Marcelo Medeiros de Vasconcellos"
__email__ = "marcelomdevasconcellos@gmail.com"


import os
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from emensageriapro.padrao import *
from emensageriapro.esocial.models import *
from emensageriapro.s1000.forms import *
from emensageriapro.functions import get_xmlns


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO


def gerar_xml_s1000_func(pk, versao=None):

    from emensageriapro.settings import BASE_DIR

    s1000_evtinfoempregador = get_object_or_404(
        s1000evtInfoEmpregador,
        id=pk)

    if not versao or versao == '|':
        versao = s1000_evtinfoempregador.versao

    evento = 's1000evtInfoEmpregador'[5:]
    arquivo = '/xsd/esocial/%s/%s.xsd' % (versao, evento)

    import os.path

    if os.path.isfile(BASE_DIR + arquivo):

        xmlns = get_xmlns(arquivo)

    else:

        xmlns = ''

    s1000_evtinfoempregador_lista = s1000evtInfoEmpregador.objects. \
        filter(id=pk).all()


    s1000_inclusao_lista = s1000inclusao.objects. \
        filter(s1000_evtinfoempregador_id__in=listar_ids(s1000_evtinfoempregador_lista)).all()

    s1000_inclusao_dadosisencao_lista = s1000inclusaodadosIsencao.objects. \
        filter(s1000_inclusao_id__in=listar_ids(s1000_inclusao_lista)).all()

    s1000_inclusao_infoop_lista = s1000inclusaoinfoOP.objects. \
        filter(s1000_inclusao_id__in=listar_ids(s1000_inclusao_lista)).all()

    s1000_inclusao_infoefr_lista = s1000inclusaoinfoEFR.objects. \
        filter(s1000_inclusao_infoop_id__in=listar_ids(s1000_inclusao_infoop_lista)).all()

    s1000_inclusao_infoente_lista = s1000inclusaoinfoEnte.objects. \
        filter(s1000_inclusao_infoop_id__in=listar_ids(s1000_inclusao_infoop_lista)).all()

    s1000_inclusao_infoorginternacional_lista = s1000inclusaoinfoOrgInternacional.objects. \
        filter(s1000_inclusao_id__in=listar_ids(s1000_inclusao_lista)).all()

    s1000_inclusao_softwarehouse_lista = s1000inclusaosoftwareHouse.objects. \
        filter(s1000_inclusao_id__in=listar_ids(s1000_inclusao_lista)).all()

    s1000_inclusao_situacaopj_lista = s1000inclusaosituacaoPJ.objects. \
        filter(s1000_inclusao_id__in=listar_ids(s1000_inclusao_lista)).all()

    s1000_inclusao_situacaopf_lista = s1000inclusaosituacaoPF.objects. \
        filter(s1000_inclusao_id__in=listar_ids(s1000_inclusao_lista)).all()

    s1000_alteracao_lista = s1000alteracao.objects. \
        filter(s1000_evtinfoempregador_id__in=listar_ids(s1000_evtinfoempregador_lista)).all()

    s1000_alteracao_dadosisencao_lista = s1000alteracaodadosIsencao.objects. \
        filter(s1000_alteracao_id__in=listar_ids(s1000_alteracao_lista)).all()

    s1000_alteracao_infoop_lista = s1000alteracaoinfoOP.objects. \
        filter(s1000_alteracao_id__in=listar_ids(s1000_alteracao_lista)).all()

    s1000_alteracao_infoefr_lista = s1000alteracaoinfoEFR.objects. \
        filter(s1000_alteracao_infoop_id__in=listar_ids(s1000_alteracao_infoop_lista)).all()

    s1000_alteracao_infoente_lista = s1000alteracaoinfoEnte.objects. \
        filter(s1000_alteracao_infoop_id__in=listar_ids(s1000_alteracao_infoop_lista)).all()

    s1000_alteracao_infoorginternacional_lista = s1000alteracaoinfoOrgInternacional.objects. \
        filter(s1000_alteracao_id__in=listar_ids(s1000_alteracao_lista)).all()

    s1000_alteracao_softwarehouse_lista = s1000alteracaosoftwareHouse.objects. \
        filter(s1000_alteracao_id__in=listar_ids(s1000_alteracao_lista)).all()

    s1000_alteracao_situacaopj_lista = s1000alteracaosituacaoPJ.objects. \
        filter(s1000_alteracao_id__in=listar_ids(s1000_alteracao_lista)).all()

    s1000_alteracao_situacaopf_lista = s1000alteracaosituacaoPF.objects. \
        filter(s1000_alteracao_id__in=listar_ids(s1000_alteracao_lista)).all()

    s1000_alteracao_novavalidade_lista = s1000alteracaonovaValidade.objects. \
        filter(s1000_alteracao_id__in=listar_ids(s1000_alteracao_lista)).all()

    s1000_exclusao_lista = s1000exclusao.objects. \
        filter(s1000_evtinfoempregador_id__in=listar_ids(s1000_evtinfoempregador_lista)).all()


    context = {
        'xmlns': xmlns,
        'versao': versao,
        'base': s1000_evtinfoempregador,
        's1000_evtinfoempregador_lista': s1000_evtinfoempregador_lista,
        'pk': int(pk),
        's1000_evtinfoempregador': s1000_evtinfoempregador,
        's1000_inclusao_lista': s1000_inclusao_lista,
        's1000_inclusao_dadosisencao_lista': s1000_inclusao_dadosisencao_lista,
        's1000_inclusao_infoop_lista': s1000_inclusao_infoop_lista,
        's1000_inclusao_infoefr_lista': s1000_inclusao_infoefr_lista,
        's1000_inclusao_infoente_lista': s1000_inclusao_infoente_lista,
        's1000_inclusao_infoorginternacional_lista': s1000_inclusao_infoorginternacional_lista,
        's1000_inclusao_softwarehouse_lista': s1000_inclusao_softwarehouse_lista,
        's1000_inclusao_situacaopj_lista': s1000_inclusao_situacaopj_lista,
        's1000_inclusao_situacaopf_lista': s1000_inclusao_situacaopf_lista,
        's1000_alteracao_lista': s1000_alteracao_lista,
        's1000_alteracao_dadosisencao_lista': s1000_alteracao_dadosisencao_lista,
        's1000_alteracao_infoop_lista': s1000_alteracao_infoop_lista,
        's1000_alteracao_infoefr_lista': s1000_alteracao_infoefr_lista,
        's1000_alteracao_infoente_lista': s1000_alteracao_infoente_lista,
        's1000_alteracao_infoorginternacional_lista': s1000_alteracao_infoorginternacional_lista,
        's1000_alteracao_softwarehouse_lista': s1000_alteracao_softwarehouse_lista,
        's1000_alteracao_situacaopj_lista': s1000_alteracao_situacaopj_lista,
        's1000_alteracao_situacaopf_lista': s1000_alteracao_situacaopf_lista,
        's1000_alteracao_novavalidade_lista': s1000_alteracao_novavalidade_lista,
        's1000_exclusao_lista': s1000_exclusao_lista,
    }

    t = get_template('s1000_evtinfoempregador.xml')
    xml = t.render(context)
    return xml



def gerar_xml_s1000(request, pk, versao=None):

    s1000_evtinfoempregador = get_object_or_404(
        s1000evtInfoEmpregador,
        id=pk)

    return gerar_xml_s1000_func(pk, versao)


def gerar_xml_assinado(request, pk):

    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes import salvar_arquivo_esocial
    from emensageriapro.mensageiro.functions.funcoes_esocial import assinar_esocial

    s1000_evtinfoempregador = get_object_or_404(
        s1000evtInfoEmpregador, id=pk)

    if not s1000_evtinfoempregador.identidade:
        from emensageriapro.functions import identidade_evento
        ident = identidade_evento(s1000_evtinfoempregador, 'esocial')
        s1000_evtinfoempregador = get_object_or_404(s1000evtInfoEmpregador, id=pk)

    if s1000_evtinfoempregador.arquivo_original:
        xml = ler_arquivo(s1000_evtinfoempregador.arquivo)

    else:
        xml = gerar_xml_s1000(request, pk)

    STATUS_ANT = [
            STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO,
            STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO
    ]

    if 'Signature' in xml and s1000_evtinfoempregador.status in STATUS_ANT:

        xml_assinado = xml
        s1000evtInfoEmpregador.objects.\
            filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)

    else:

        if not s1000_evtinfoempregador.transmissor_lote_esocial:

            from emensageriapro.mapa_processamento.views.funcoes_automaticas_esocial \
                import vincular_transmissor_esocial, criar_transmissor_esocial, get_grupo

            grupo = get_grupo(s1000evtInfoEmpregador)

            criar_transmissor_esocial(request,
                grupo,
                s1000_evtinfoempregador.nrinsc,
                s1000_evtinfoempregador.tpinsc)

            vincular_transmissor_esocial(request,
                grupo,
                s1000evtInfoEmpregador,
                s1000_evtinfoempregador)

        s1000_evtinfoempregador = get_object_or_404(
            s1000evtInfoEmpregador,
            id=pk)

        xml_assinado = assinar_esocial(
            request,
            xml,
            s1000_evtinfoempregador.transmissor_lote_esocial_id)


        if 'Signature' in xml_assinado and s1000_evtinfoempregador.status in STATUS_ANT:

            s1000evtInfoEmpregador.objects.\
                filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)

        elif s1000evtInfoEmpregador.status in STATUS_ANT:

            s1000evtInfoEmpregador.objects.\
                filter(id=pk).update(status=STATUS_EVENTO_GERADO)

    arquivo = '/arquivos/Eventos/s1000_evtinfoempregador/%s.xml' % (s1000_evtinfoempregador.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/s1000_evtinfoempregador/' % BASE_DIR)

    if not os.path.exists(BASE_DIR+arquivo):

        salvar_arquivo_esocial(arquivo, xml_assinado, 1)

    xml_assinado = ler_arquivo(arquivo)

    return xml_assinado


@login_required
def gerar_xml(request, pk):

    if pk:

        xml_assinado = gerar_xml_assinado(request, pk)
        return HttpResponse(xml_assinado, content_type='text/xml')

    context = {'data': datetime.now(),}

    return render(request, 'permissao_negada.html', context)