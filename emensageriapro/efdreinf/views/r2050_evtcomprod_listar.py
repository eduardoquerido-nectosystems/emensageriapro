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
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.mensageiro.models import TransmissorLoteEfdreinf
from emensageriapro.efdreinf.models import r5001evtTotal
from emensageriapro.efdreinf.models import r5011evtTotalContrib
from emensageriapro.efdreinf.models import r9001evtTotal
from emensageriapro.efdreinf.models import r9002evtRet
from emensageriapro.efdreinf.models import r9011evtTotalContrib
from emensageriapro.efdreinf.models import r9012evtRetCons
from emensageriapro.mensageiro.models import TransmissorLoteEfdreinf


@login_required
def listar(request, output=None):

    if request.user.has_perm('efdreinf.can_see_r2050evtComProd'):

        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_reinf': 0,
            'show_evtcomprod': 0,
            'show_identidade': 1,
            'show_ideevento': 0,
            'show_indretif': 1,
            'show_nrrecibo': 0,
            'show_perapur': 1,
            'show_tpamb': 0,
            'show_procemi': 0,
            'show_verproc': 0,
            'show_idecontri': 0,
            'show_tpinsc': 0,
            'show_nrinsc': 0,
            'show_infocomprod': 0,
            'show_ideestab': 0,
            'show_tpinscestab': 0,
            'show_nrinscestab': 0,
            'show_vlrrecbrutatotal': 0,
            'show_vlrcpapur': 0,
            'show_vlrratapur': 0,
            'show_vlrsenarapur': 0,
            'show_vlrcpsusptotal': 0,
            'show_vlrratsusptotal': 0,
            'show_vlrsenarsusptotal': 0,
            'show_versao': 0,
            'show_transmissor_lote_efdreinf': 0,
            'show_retornos_r5001': 0,
            'show_retornos_r5011': 0,
            'show_retornos_r9001': 0,
            'show_retornos_r9002': 0,
            'show_retornos_r9011': 0,
            'show_retornos_r9012': 0,
            'show_ocorrencias': 0,
            'show_validacao_precedencia': 0,
            'show_validacoes': 0,
            'show_arquivo_original': 0,
            'show_arquivo': 0,
            'show_status': 1,
            'show_cdretorno': 1,
            'show_descretorno': 0,
            'show_dhprocess': 0,
            'show_transmissor_lote_efdreinf_error': 0, }

        post = False

        if request.method == 'POST':

            post = True
            dict_fields = {
                'reinf': 'reinf',
                'evtcomprod': 'evtcomprod',
                'identidade__icontains': 'identidade__icontains',
                'ideevento': 'ideevento',
                'indretif__icontains': 'indretif__icontains',
                'nrrecibo__icontains': 'nrrecibo__icontains',
                'perapur__icontains': 'perapur__icontains',
                'tpamb__icontains': 'tpamb__icontains',
                'procemi__icontains': 'procemi__icontains',
                'verproc__icontains': 'verproc__icontains',
                'idecontri': 'idecontri',
                'tpinsc__icontains': 'tpinsc__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'infocomprod': 'infocomprod',
                'ideestab': 'ideestab',
                'tpinscestab__icontains': 'tpinscestab__icontains',
                'nrinscestab__icontains': 'nrinscestab__icontains',
                'vlrrecbrutatotal__icontains': 'vlrrecbrutatotal__icontains',
                'vlrcpapur__icontains': 'vlrcpapur__icontains',
                'vlrratapur__icontains': 'vlrratapur__icontains',
                'vlrsenarapur__icontains': 'vlrsenarapur__icontains',
                'vlrcpsusptotal__icontains': 'vlrcpsusptotal__icontains',
                'vlrratsusptotal__icontains': 'vlrratsusptotal__icontains',
                'vlrsenarsusptotal__icontains': 'vlrsenarsusptotal__icontains',
                'versao__icontains': 'versao__icontains',
                'transmissor_lote_efdreinf__icontains': 'transmissor_lote_efdreinf__icontains',
                'status__icontains': 'status__icontains',
                'cdretorno__icontains': 'cdretorno__icontains', }

            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)

            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)

            if request.method == 'POST':
                dict_fields = {
                    'reinf': 'reinf',
                    'evtcomprod': 'evtcomprod',
                    'identidade__icontains': 'identidade__icontains',
                    'ideevento': 'ideevento',
                    'indretif__icontains': 'indretif__icontains',
                    'nrrecibo__icontains': 'nrrecibo__icontains',
                    'perapur__icontains': 'perapur__icontains',
                    'tpamb__icontains': 'tpamb__icontains',
                    'procemi__icontains': 'procemi__icontains',
                    'verproc__icontains': 'verproc__icontains',
                    'idecontri': 'idecontri',
                    'tpinsc__icontains': 'tpinsc__icontains',
                    'nrinsc__icontains': 'nrinsc__icontains',
                    'infocomprod': 'infocomprod',
                    'ideestab': 'ideestab',
                    'tpinscestab__icontains': 'tpinscestab__icontains',
                    'nrinscestab__icontains': 'nrinscestab__icontains',
                    'vlrrecbrutatotal__icontains': 'vlrrecbrutatotal__icontains',
                    'vlrcpapur__icontains': 'vlrcpapur__icontains',
                    'vlrratapur__icontains': 'vlrratapur__icontains',
                    'vlrsenarapur__icontains': 'vlrsenarapur__icontains',
                    'vlrcpsusptotal__icontains': 'vlrcpsusptotal__icontains',
                    'vlrratsusptotal__icontains': 'vlrratsusptotal__icontains',
                    'vlrsenarsusptotal__icontains': 'vlrsenarsusptotal__icontains',
                    'versao__icontains': 'versao__icontains',
                    'transmissor_lote_efdreinf__icontains': 'transmissor_lote_efdreinf__icontains',
                    'status__icontains': 'status__icontains',
                    'cdretorno__icontains': 'cdretorno__icontains', }
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)

        dict_qs = clear_dict_fields(dict_fields)
        r2050_evtcomprod_lista = r2050evtComProd.objects.filter(**dict_qs).filter().exclude(id=0).all()

        if not post and len(r2050_evtcomprod_lista) > 100:
            filtrar = True
            r2050_evtcomprod_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lote_efdreinf_lista = TransmissorLoteEfdreinf.objects.all()
        retornos_r5001_lista = r5001evtTotal.objects.all()
        retornos_r5011_lista = r5011evtTotalContrib.objects.all()
        retornos_r9001_lista = r9001evtTotal.objects.all()
        retornos_r9002_lista = r9002evtRet.objects.all()
        retornos_r9011_lista = r9011evtTotalContrib.objects.all()
        retornos_r9012_lista = r9012evtRetCons.objects.all()
        transmissor_lote_efdreinf_error_lista = TransmissorLoteEfdreinf.objects.all()
        #r2050_evtcomprod_listar_custom

        request.session['return'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'output': output,
            'r2050_evtcomprod_lista': r2050_evtcomprod_lista,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'modulos': ['efdreinf', ],
            'paginas': ['r2050_evtcomprod', ],
            'show_fields': show_fields,
            'filtrar': filtrar,
            'transmissor_lote_efdreinf_lista': transmissor_lote_efdreinf_lista,
            'retornos_r5001_lista': retornos_r5001_lista,
            'retornos_r5011_lista': retornos_r5011_lista,
            'retornos_r9001_lista': retornos_r9001_lista,
            'retornos_r9002_lista': retornos_r9002_lista,
            'retornos_r9011_lista': retornos_r9011_lista,
            'retornos_r9012_lista': retornos_r9012_lista,
            'transmissor_lote_efdreinf_error_lista': transmissor_lote_efdreinf_error_lista,
        }

        if output == 'pdf':

            from emensageriapro.functions import render_to_pdf
            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='r2050_evtcomprod_listar.html',
                filename="r2050_evtcomprod.pdf",
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

            response = render_to_response('r2050_evtcomprod_listar.html', context)
            filename = "r2050_evtcomprod.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        elif output == 'csv':

            response = render_to_response('csv/r2050_evtcomprod.csv', context)
            filename = "r2050_evtcomprod.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'

            return response

        else:

            return render(request, 'r2050_evtcomprod_listar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'data': datetime.datetime.now(),
            'modulos': ['efdreinf', ],
            'paginas': ['r2050_evtcomprod', ],
        }
        return render(request, 'permissao_negada.html', context)