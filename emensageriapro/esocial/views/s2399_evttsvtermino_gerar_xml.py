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
from emensageriapro.s2399.forms import *
from emensageriapro.functions import get_xmlns


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO


def gerar_xml_s2399_func(pk, versao=None):

    from emensageriapro.settings import BASE_DIR

    s2399_evttsvtermino = get_object_or_404(
        s2399evtTSVTermino,
        id=pk)

    if not versao or versao == '|':
        versao = s2399_evttsvtermino.versao

    evento = 's2399evtTSVTermino'[5:]
    arquivo = '/xsd/esocial/%s/%s.xsd' % (versao, evento)

    import os.path

    if os.path.isfile(BASE_DIR + arquivo):

        xmlns = get_xmlns(arquivo)

    else:

        xmlns = ''

    s2399_evttsvtermino_lista = s2399evtTSVTermino.objects. \
        filter(id=pk).all()


    s2399_mudancacpf_lista = s2399mudancaCPF.objects. \
        filter(s2399_evttsvtermino_id__in=listar_ids(s2399_evttsvtermino_lista)).all()

    s2399_verbasresc_lista = s2399verbasResc.objects. \
        filter(s2399_evttsvtermino_id__in=listar_ids(s2399_evttsvtermino_lista)).all()

    s2399_dmdev_lista = s2399dmDev.objects. \
        filter(s2399_verbasresc_id__in=listar_ids(s2399_verbasresc_lista)).all()

    s2399_ideestablot_lista = s2399ideEstabLot.objects. \
        filter(s2399_dmdev_id__in=listar_ids(s2399_dmdev_lista)).all()

    s2399_detverbas_lista = s2399detVerbas.objects. \
        filter(s2399_ideestablot_id__in=listar_ids(s2399_ideestablot_lista)).all()

    s2399_infosaudecolet_lista = s2399infoSaudeColet.objects. \
        filter(s2399_ideestablot_id__in=listar_ids(s2399_ideestablot_lista)).all()

    s2399_detoper_lista = s2399detOper.objects. \
        filter(s2399_infosaudecolet_id__in=listar_ids(s2399_infosaudecolet_lista)).all()

    s2399_detplano_lista = s2399detPlano.objects. \
        filter(s2399_detoper_id__in=listar_ids(s2399_detoper_lista)).all()

    s2399_infoagnocivo_lista = s2399infoAgNocivo.objects. \
        filter(s2399_ideestablot_id__in=listar_ids(s2399_ideestablot_lista)).all()

    s2399_infosimples_lista = s2399infoSimples.objects. \
        filter(s2399_ideestablot_id__in=listar_ids(s2399_ideestablot_lista)).all()

    s2399_procjudtrab_lista = s2399procJudTrab.objects. \
        filter(s2399_verbasresc_id__in=listar_ids(s2399_verbasresc_lista)).all()

    s2399_infomv_lista = s2399infoMV.objects. \
        filter(s2399_verbasresc_id__in=listar_ids(s2399_verbasresc_lista)).all()

    s2399_remunoutrempr_lista = s2399remunOutrEmpr.objects. \
        filter(s2399_infomv_id__in=listar_ids(s2399_infomv_lista)).all()

    s2399_quarentena_lista = s2399quarentena.objects. \
        filter(s2399_evttsvtermino_id__in=listar_ids(s2399_evttsvtermino_lista)).all()


    context = {
        'xmlns': xmlns,
        'versao': versao,
        'base': s2399_evttsvtermino,
        's2399_evttsvtermino_lista': s2399_evttsvtermino_lista,
        'pk': int(pk),
        's2399_evttsvtermino': s2399_evttsvtermino,
        's2399_mudancacpf_lista': s2399_mudancacpf_lista,
        's2399_verbasresc_lista': s2399_verbasresc_lista,
        's2399_dmdev_lista': s2399_dmdev_lista,
        's2399_ideestablot_lista': s2399_ideestablot_lista,
        's2399_detverbas_lista': s2399_detverbas_lista,
        's2399_infosaudecolet_lista': s2399_infosaudecolet_lista,
        's2399_detoper_lista': s2399_detoper_lista,
        's2399_detplano_lista': s2399_detplano_lista,
        's2399_infoagnocivo_lista': s2399_infoagnocivo_lista,
        's2399_infosimples_lista': s2399_infosimples_lista,
        's2399_procjudtrab_lista': s2399_procjudtrab_lista,
        's2399_infomv_lista': s2399_infomv_lista,
        's2399_remunoutrempr_lista': s2399_remunoutrempr_lista,
        's2399_quarentena_lista': s2399_quarentena_lista,
    }

    t = get_template('s2399_evttsvtermino.xml')
    xml = t.render(context)
    return xml



def gerar_xml_s2399(request, pk, versao=None):

    s2399_evttsvtermino = get_object_or_404(
        s2399evtTSVTermino,
        id=pk)

    return gerar_xml_s2399_func(pk, versao)


def gerar_xml_assinado(request, pk):

    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes import salvar_arquivo_esocial
    from emensageriapro.mensageiro.functions.funcoes_esocial import assinar_esocial

    s2399_evttsvtermino = get_object_or_404(
        s2399evtTSVTermino, id=pk)

    if not s2399_evttsvtermino.identidade:
        from emensageriapro.functions import identidade_evento
        ident = identidade_evento(s2399_evttsvtermino, 'esocial')
        s2399_evttsvtermino = get_object_or_404(s2399evtTSVTermino, id=pk)

    if s2399_evttsvtermino.arquivo_original:
        xml = ler_arquivo(s2399_evttsvtermino.arquivo)

    else:
        xml = gerar_xml_s2399(request, pk)

    STATUS_ANT = [
            STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO,
            STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO
    ]

    if 'Signature' in xml and s2399_evttsvtermino.status in STATUS_ANT:

        xml_assinado = xml
        s2399evtTSVTermino.objects.\
            filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)

    else:

        if not s2399_evttsvtermino.transmissor_lote_esocial:

            from emensageriapro.mapa_processamento.views.funcoes_automaticas_esocial \
                import vincular_transmissor_esocial, criar_transmissor_esocial, get_grupo

            grupo = get_grupo(s2399evtTSVTermino)

            criar_transmissor_esocial(request,
                grupo,
                s2399_evttsvtermino.nrinsc,
                s2399_evttsvtermino.tpinsc)

            vincular_transmissor_esocial(request,
                grupo,
                s2399evtTSVTermino,
                s2399_evttsvtermino)

        s2399_evttsvtermino = get_object_or_404(
            s2399evtTSVTermino,
            id=pk)

        xml_assinado = assinar_esocial(
            request,
            xml,
            s2399_evttsvtermino.transmissor_lote_esocial_id)


        if 'Signature' in xml_assinado and s2399_evttsvtermino.status in STATUS_ANT:

            s2399evtTSVTermino.objects.\
                filter(id=pk).update(status=STATUS_EVENTO_ASSINADO)

        elif s1000evtInfoEmpregador.status in STATUS_ANT:

            s2399evtTSVTermino.objects.\
                filter(id=pk).update(status=STATUS_EVENTO_GERADO)

    arquivo = '/arquivos/Eventos/s2399_evttsvtermino/%s.xml' % (s2399_evttsvtermino.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/s2399_evttsvtermino/' % BASE_DIR)

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