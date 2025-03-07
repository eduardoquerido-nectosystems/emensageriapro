#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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

import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.mensageiro.functions.funcoes_esocial import *
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import Usuarios


#IMPORTACOES



@login_required
def enviar(request, pk):

    transmissor_lote_esocial = get_object_or_404(TransmissorLoteEsocial, id=pk)
    a = send_xml(request, pk, 'WsEnviarLoteEventos')

    return redirect('transmissor_lote_esocial')


@login_required
def consultar(request, pk):

    transmissor_lote_esocial = get_object_or_404(TransmissorLoteEsocial, id=pk)
    a = send_xml(request, pk, 'WsConsultarLoteEventos')

    return redirect('transmissor_lote_esocial')


@login_required
def recibo(request, pk):
    from django.db.models import Q

    transmissor_lote_esocial = get_object_or_404(TransmissorLoteEsocial, id=pk)

    ocorrencias_lista = TransmissorLoteEsocialOcorrencias.objects.\
        filter(transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()

    eventos_lista = TransmissorEventosEsocial.objects.\
        filter(Q(transmissor_lote_esocial_id=transmissor_lote_esocial.id) | Q(transmissor_lote_esocial_error_id=transmissor_lote_esocial.id)).all()

    context = {
        'eventos_lista': eventos_lista,
        'ocorrencias_lista': ocorrencias_lista,
        'transmissor_lote_esocial': transmissor_lote_esocial,
        'data': datetime.datetime.now(),
    }

    return render(request, 'transmissor_lote_esocial_recibo.html', context)
