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
from emensageriapro.s2200.forms import *
from emensageriapro.s2200.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.esocial.models import s2200evtAdmissao


@login_required
def listar(request, output=None):

    if request.user.has_perm('s2200.can_see_s2200localTrabDom'):

        filtrar = False

        dict_fields = {}
        show_fields = {
            'show_s2200_evtadmissao': 1,
            'show_tplograd': 0,
            'show_dsclograd': 1,
            'show_nrlograd': 1,
            'show_complemento': 0,
            'show_bairro': 0,
            'show_cep': 0,
            'show_codmunic': 0,
            'show_uf': 0, }

        post = False

        if request.method == 'POST':

            post = True
            dict_fields = {
                's2200_evtadmissao__icontains': 's2200_evtadmissao__icontains',
                'tplograd__icontains': 'tplograd__icontains',
                'dsclograd__icontains': 'dsclograd__icontains',
                'nrlograd__icontains': 'nrlograd__icontains',
                'complemento__icontains': 'complemento__icontains',
                'bairro__icontains': 'bairro__icontains',
                'cep__icontains': 'cep__icontains',
                'codmunic__icontains': 'codmunic__icontains',
                'uf__icontains': 'uf__icontains', }

            for a in dict_fields:

                dict_fields[a] = request.POST.get(a or None)

            for a in show_fields:

                show_fields[a] = request.POST.get(a or None)

            if request.method == 'POST':

                dict_fields = {
                    's2200_evtadmissao__icontains': 's2200_evtadmissao__icontains',
                    'tplograd__icontains': 'tplograd__icontains',
                    'dsclograd__icontains': 'dsclograd__icontains',
                    'nrlograd__icontains': 'nrlograd__icontains',
                    'complemento__icontains': 'complemento__icontains',
                    'bairro__icontains': 'bairro__icontains',
                    'cep__icontains': 'cep__icontains',
                    'codmunic__icontains': 'codmunic__icontains',
                    'uf__icontains': 'uf__icontains', }

                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)

        dict_qs = clear_dict_fields(dict_fields)
        s2200_localtrabdom_lista = s2200localTrabDom.objects.filter(**dict_qs).filter().exclude(id=0).all()

        if not post and len(s2200_localtrabdom_lista) > 100:

            filtrar = True
            s2200_localtrabdom_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        s2200_evtadmissao_lista = s2200evtAdmissao.objects.all()
        #s2200_localtrabdom_listar_custom

        request.session['return'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'output': output,
            's2200_localtrabdom_lista': s2200_localtrabdom_lista,
            'modulos': ['s2200', ],
            'paginas': ['s2200_localtrabdom', ],
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'show_fields': show_fields,
            'filtrar': filtrar,
            's2200_evtadmissao_lista': s2200_evtadmissao_lista,
        }

        if output == 'pdf':

            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='s2200_localtrabdom_listar.html',
                filename="s2200_localtrabdom.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True}, )
         
            return response

        elif output == 'xls':

            from django.shortcuts import render_to_response
            response = render_to_response('s2200_localtrabdom_listar.html', context)
            filename = "s2200_localtrabdom.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif output == 'csv':

            from django.shortcuts import render_to_response
            response = render_to_response('csv/s2200_localtrabdom.csv', context)
            filename = "s2200_localtrabdom.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        else:

            return render(request, 's2200_localtrabdom_listar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'output': output,
            'data': datetime.datetime.now(),
            'modulos': ['s2200', ],
            'paginas': ['s2200_localtrabdom', ],
        }

        return render(request,
                      'permissao_negada.html',
                      context)