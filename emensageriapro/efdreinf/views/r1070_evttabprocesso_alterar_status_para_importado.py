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


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from emensageriapro.padrao import *
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import Usuarios
from emensageriapro.r1070.models import *
from emensageriapro.r1070.forms import *
from emensageriapro.functions import render_to_pdf, txt_xml
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from wkhtmltopdf.views import PDFTemplateResponse
from datetime import datetime
import base64
import os


from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO



@csrf_exempt
@api_view(["GET"])
def alterar_status_para_importado(request, pk):

    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes import gravar_nome_arquivo

    if request.user.has_perm('efdreinf.can_open_r1070evtTabProcesso'):

        r1070_evttabprocesso = get_object_or_404(r1070evtTabProcesso, id=pk)

        status_list = [
            STATUS_EVENTO_CADASTRADO
        ]

        if r1070_evttabprocesso.status in status_list:

            r1070evtTabProcesso.objects.filter(id=pk).update(
                status=STATUS_EVENTO_IMPORTADO)

            request.user.id = request.user.id

            gravar_auditoria(u'{}', u'{"funcao": "Status do evento alterado para Importado"}',
                'r1070_evttabprocesso', pk, request.user.id, 2)

            data = {'response': u'Status do evento alterado para "Importado"!'}
            return Response(data, status=HTTP_200_OK)

        else:

            data = {'response': u'Não foi possível alterar o status para importado, pois o mesmo não está com o status "Cadastrado"!'}
            return Response(data, status=HTTP_200_OK)

    else:

        data = {'response': u'Você não tem permissão para acessar esta página!'}
        return Response(data, status=HTTP_200_OK)
