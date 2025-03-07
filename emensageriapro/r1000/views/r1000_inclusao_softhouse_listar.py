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
from emensageriapro.r1000.forms import *
from emensageriapro.r1000.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.r1000.models import r1000inclusao


@login_required
def listar(request, output=None):

    if request.user.has_perm('r1000.can_see_r1000inclusaosoftHouse'):

        filtrar = False

        dict_fields = {}
        show_fields = {
            'show_r1000_inclusao': 1,
            'show_cnpjsofthouse': 1,
            'show_nmrazao': 1,
            'show_nmcont': 0,
            'show_telefone': 0,
            'show_email': 0, }

        post = False

        if request.method == 'POST':

            post = True
            dict_fields = {
                'r1000_inclusao__icontains': 'r1000_inclusao__icontains',
                'cnpjsofthouse__icontains': 'cnpjsofthouse__icontains',
                'nmrazao__icontains': 'nmrazao__icontains',
                'nmcont__icontains': 'nmcont__icontains',
                'telefone__icontains': 'telefone__icontains',
                'email__icontains': 'email__icontains', }

            for a in dict_fields:

                dict_fields[a] = request.POST.get(a or None)

            for a in show_fields:

                show_fields[a] = request.POST.get(a or None)

            if request.method == 'POST':

                dict_fields = {
                    'r1000_inclusao__icontains': 'r1000_inclusao__icontains',
                    'cnpjsofthouse__icontains': 'cnpjsofthouse__icontains',
                    'nmrazao__icontains': 'nmrazao__icontains',
                    'nmcont__icontains': 'nmcont__icontains',
                    'telefone__icontains': 'telefone__icontains',
                    'email__icontains': 'email__icontains', }

                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)

        dict_qs = clear_dict_fields(dict_fields)
        r1000_inclusao_softhouse_lista = r1000inclusaosoftHouse.objects.filter(**dict_qs).filter().exclude(id=0).all()

        if not post and len(r1000_inclusao_softhouse_lista) > 100:

            filtrar = True
            r1000_inclusao_softhouse_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        r1000_inclusao_lista = r1000inclusao.objects.all()
        #r1000_inclusao_softhouse_listar_custom

        request.session['return'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'output': output,
            'r1000_inclusao_softhouse_lista': r1000_inclusao_softhouse_lista,
            'modulos': ['r1000', ],
            'paginas': ['r1000_inclusao_softhouse', ],
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'show_fields': show_fields,
            'filtrar': filtrar,
            'r1000_inclusao_lista': r1000_inclusao_lista,
        }

        if output == 'pdf':

            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='r1000_inclusao_softhouse_listar.html',
                filename="r1000_inclusao_softhouse.pdf",
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
            response = render_to_response('r1000_inclusao_softhouse_listar.html', context)
            filename = "r1000_inclusao_softhouse.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif output == 'csv':

            from django.shortcuts import render_to_response
            response = render_to_response('csv/r1000_inclusao_softhouse.csv', context)
            filename = "r1000_inclusao_softhouse.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        else:

            return render(request, 'r1000_inclusao_softhouse_listar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'output': output,
            'data': datetime.datetime.now(),
            'modulos': ['r1000', ],
            'paginas': ['r1000_inclusao_softhouse', ],
        }

        return render(request,
                      'permissao_negada.html',
                      context)