#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"


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


import datetime
import json
import base64
from django.contrib import messages
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from django.forms.models import model_to_dict
from wkhtmltopdf.views import PDFTemplateResponse
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from emensageriapro.padrao import *
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.mensageiro.models import TransmissorLoteEsocial
from emensageriapro.mensageiro.models import TransmissorLoteEsocial


@login_required
def listar(request, output=None):

    if request.user.has_perm('esocial.can_see_s5003evtBasesFGTS'):

        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_esocial': 0,
            'show_evtbasesfgts': 0,
            'show_identidade': 1,
            'show_ideevento': 0,
            'show_nrrecarqbase': 1,
            'show_perapur': 1,
            'show_ideempregador': 0,
            'show_tpinsc': 0,
            'show_nrinsc': 0,
            'show_idetrabalhador': 0,
            'show_cpftrab': 0,
            'show_nistrab': 0,
            'show_infofgts': 0,
            'show_dtvenc': 0,
            'show_versao': 0,
            'show_transmissor_lote_esocial': 0,
            'show_ocorrencias': 0,
            'show_validacao_precedencia': 0,
            'show_validacoes': 0,
            'show_arquivo_original': 0,
            'show_arquivo': 0,
            'show_status': 1,
            'show_transmissor_lote_esocial_error': 0, }

        post = False

        if request.method == 'POST':

            post = True
            dict_fields = {
                'esocial': 'esocial',
                'evtbasesfgts': 'evtbasesfgts',
                'identidade__icontains': 'identidade__icontains',
                'ideevento': 'ideevento',
                'nrrecarqbase__icontains': 'nrrecarqbase__icontains',
                'perapur__icontains': 'perapur__icontains',
                'ideempregador': 'ideempregador',
                'tpinsc__icontains': 'tpinsc__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'idetrabalhador': 'idetrabalhador',
                'cpftrab__icontains': 'cpftrab__icontains',
                'nistrab__icontains': 'nistrab__icontains',
                'infofgts': 'infofgts',
                'dtvenc__range': 'dtvenc__range',
                'versao__icontains': 'versao__icontains',
                'transmissor_lote_esocial__icontains': 'transmissor_lote_esocial__icontains',
                'status__icontains': 'status__icontains', }

            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)

            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)

            if request.method == 'POST':
                dict_fields = {
                    'esocial': 'esocial',
                    'evtbasesfgts': 'evtbasesfgts',
                    'identidade__icontains': 'identidade__icontains',
                    'ideevento': 'ideevento',
                    'nrrecarqbase__icontains': 'nrrecarqbase__icontains',
                    'perapur__icontains': 'perapur__icontains',
                    'ideempregador': 'ideempregador',
                    'tpinsc__icontains': 'tpinsc__icontains',
                    'nrinsc__icontains': 'nrinsc__icontains',
                    'idetrabalhador': 'idetrabalhador',
                    'cpftrab__icontains': 'cpftrab__icontains',
                    'nistrab__icontains': 'nistrab__icontains',
                    'infofgts': 'infofgts',
                    'dtvenc__range': 'dtvenc__range',
                    'versao__icontains': 'versao__icontains',
                    'transmissor_lote_esocial__icontains': 'transmissor_lote_esocial__icontains',
                    'status__icontains': 'status__icontains', }
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)

        dict_qs = clear_dict_fields(dict_fields)
        s5003_evtbasesfgts_lista = s5003evtBasesFGTS.objects.filter(**dict_qs).filter().exclude(id=0).all()

        if not post and len(s5003_evtbasesfgts_lista) > 100:
            filtrar = True
            s5003_evtbasesfgts_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lote_esocial_lista = TransmissorLoteEsocial.objects.all()
        transmissor_lote_esocial_error_lista = TransmissorLoteEsocial.objects.all()
        #s5003_evtbasesfgts_listar_custom

        request.session['return'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'output': output,
            's5003_evtbasesfgts_lista': s5003_evtbasesfgts_lista,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'modulos': ['esocial', ],
            'paginas': ['s5003_evtbasesfgts', ],
            'show_fields': show_fields,
            'filtrar': filtrar,
            'transmissor_lote_esocial_lista': transmissor_lote_esocial_lista,
            'transmissor_lote_esocial_error_lista': transmissor_lote_esocial_error_lista,
        }

        if output == 'pdf':

            from emensageriapro.functions import render_to_pdf
            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='s5003_evtbasesfgts_listar.html',
                filename="s5003_evtbasesfgts.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             'viewport-size': "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response

        elif output == 'xls':

            response = render_to_response('s5003_evtbasesfgts_listar.html', context)
            filename = "s5003_evtbasesfgts.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        elif output == 'csv':

            response = render_to_response('csv/s5003_evtbasesfgts.csv', context)
            filename = "s5003_evtbasesfgts.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'

            return response

        else:

            return render(request, 's5003_evtbasesfgts_listar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'data': datetime.datetime.now(),
            'modulos': ['esocial', ],
            'paginas': ['s5003_evtbasesfgts', ],
        }
        return render(request, 'permissao_negada.html', context)