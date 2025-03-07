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
from emensageriapro.r9002.forms import *
from emensageriapro.r9002.models import *
from emensageriapro.controle_de_acesso.models import *


@login_required
def listar(request, output=None):

    if request.user.has_perm('r9002.can_see_r9002totApurDia'):
    
        filtrar = False
        
        dict_fields = {}
        show_fields = { 
            'show_r9002_infototal': 1,
            'show_perapurdia': 1,
            'show_crdia': 1,
            'show_vlrbasecrdia': 1,
            'show_vlrcrdia': 1,
            'show_vlrbasecrdiasusp': 0,
            'show_vlrcrdiasusp': 0, }
            
        post = False
        
        if request.method == 'POST':
        
            post = True
            dict_fields = { 
                'r9002_infototal__icontains': 'r9002_infototal__icontains',
                'perapurdia__icontains': 'perapurdia__icontains',
                'crdia__icontains': 'crdia__icontains',
                'vlrbasecrdia__icontains': 'vlrbasecrdia__icontains',
                'vlrcrdia__icontains': 'vlrcrdia__icontains',
                'vlrbasecrdiasusp__icontains': 'vlrbasecrdiasusp__icontains',
                'vlrcrdiasusp__icontains': 'vlrcrdiasusp__icontains', }
                
            for a in dict_fields:
            
                dict_fields[a] = request.POST.get(a or None)
                
            for a in show_fields:
            
                show_fields[a] = request.POST.get(a or None)
                
            if request.method == 'POST':
            
                dict_fields = { 
                    'r9002_infototal__icontains': 'r9002_infototal__icontains',
                    'perapurdia__icontains': 'perapurdia__icontains',
                    'crdia__icontains': 'crdia__icontains',
                    'vlrbasecrdia__icontains': 'vlrbasecrdia__icontains',
                    'vlrcrdia__icontains': 'vlrcrdia__icontains',
                    'vlrbasecrdiasusp__icontains': 'vlrbasecrdiasusp__icontains',
                    'vlrcrdiasusp__icontains': 'vlrcrdiasusp__icontains', }
                    
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
                    
        dict_qs = clear_dict_fields(dict_fields)
        r9002_totapurdia_lista = r9002totApurDia.objects.filter(**dict_qs).filter().exclude(id=0).all()
        
        if not post and len(r9002_totapurdia_lista) > 100:
        
            filtrar = True
            r9002_totapurdia_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
            
        #[VARIAVEIS_LISTA_FILTRO_RELATORIO]
        #r9002_totapurdia_listar_custom
        
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'output': output,
            'r9002_totapurdia_lista': r9002_totapurdia_lista, 
            'modulos': ['r9002', ],
            'paginas': ['r9002_totapurdia', ],
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'show_fields': show_fields,
            'filtrar': filtrar,
            #[VARIAVEIS_FILTRO_RELATORIO]
        }
            
        if output == 'pdf':
        
            from wkhtmltopdf.views import PDFTemplateResponse
            
            response = PDFTemplateResponse(
                request=request,
                template='r9002_totapurdia_listar.html',
                filename="r9002_totapurdia.pdf",
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
            response = render_to_response('r9002_totapurdia_listar.html', context)
            filename = "r9002_totapurdia.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
            
        elif output == 'csv':
        
            from django.shortcuts import render_to_response
            response = render_to_response('csv/r9002_totapurdia.csv', context)
            filename = "r9002_totapurdia.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        
        else:
        
            return render(request, 'r9002_totapurdia_listar.html', context)
            
    else:
    
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'output': output,
            'data': datetime.datetime.now(),
            'modulos': ['r9002', ],
            'paginas': ['r9002_totapurdia', ],
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)