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
from emensageriapro.s5011.forms import *
from emensageriapro.s5011.models import *
from emensageriapro.controle_de_acesso.models import *


@login_required
def listar(request, output=None):

    if request.user.has_perm('s5011.can_see_s5011basesRemun'):
    
        filtrar = False
        
        dict_fields = {}
        show_fields = { 
            'show_s5011_idelotacao': 1,
            'show_indincid': 1,
            'show_codcateg': 1,
            'show_basescp': 0,
            'show_vrbccp00': 1,
            'show_vrbccp15': 1,
            'show_vrbccp20': 1,
            'show_vrbccp25': 1,
            'show_vrsuspbccp00': 1,
            'show_vrsuspbccp15': 1,
            'show_vrsuspbccp20': 1,
            'show_vrsuspbccp25': 1,
            'show_vrdescsest': 1,
            'show_vrcalcsest': 1,
            'show_vrdescsenat': 1,
            'show_vrcalcsenat': 1,
            'show_vrsalfam': 1,
            'show_vrsalmat': 1, }
            
        post = False
        
        if request.method == 'POST':
        
            post = True
            dict_fields = { 
                's5011_idelotacao__icontains': 's5011_idelotacao__icontains',
                'indincid__icontains': 'indincid__icontains',
                'codcateg__icontains': 'codcateg__icontains',
                'basescp': 'basescp',
                'vrbccp00__icontains': 'vrbccp00__icontains',
                'vrbccp15__icontains': 'vrbccp15__icontains',
                'vrbccp20__icontains': 'vrbccp20__icontains',
                'vrbccp25__icontains': 'vrbccp25__icontains',
                'vrsuspbccp00__icontains': 'vrsuspbccp00__icontains',
                'vrsuspbccp15__icontains': 'vrsuspbccp15__icontains',
                'vrsuspbccp20__icontains': 'vrsuspbccp20__icontains',
                'vrsuspbccp25__icontains': 'vrsuspbccp25__icontains',
                'vrdescsest__icontains': 'vrdescsest__icontains',
                'vrcalcsest__icontains': 'vrcalcsest__icontains',
                'vrdescsenat__icontains': 'vrdescsenat__icontains',
                'vrcalcsenat__icontains': 'vrcalcsenat__icontains',
                'vrsalfam__icontains': 'vrsalfam__icontains',
                'vrsalmat__icontains': 'vrsalmat__icontains', }
                
            for a in dict_fields:
            
                dict_fields[a] = request.POST.get(a or None)
                
            for a in show_fields:
            
                show_fields[a] = request.POST.get(a or None)
                
            if request.method == 'POST':
            
                dict_fields = { 
                    's5011_idelotacao__icontains': 's5011_idelotacao__icontains',
                    'indincid__icontains': 'indincid__icontains',
                    'codcateg__icontains': 'codcateg__icontains',
                    'basescp': 'basescp',
                    'vrbccp00__icontains': 'vrbccp00__icontains',
                    'vrbccp15__icontains': 'vrbccp15__icontains',
                    'vrbccp20__icontains': 'vrbccp20__icontains',
                    'vrbccp25__icontains': 'vrbccp25__icontains',
                    'vrsuspbccp00__icontains': 'vrsuspbccp00__icontains',
                    'vrsuspbccp15__icontains': 'vrsuspbccp15__icontains',
                    'vrsuspbccp20__icontains': 'vrsuspbccp20__icontains',
                    'vrsuspbccp25__icontains': 'vrsuspbccp25__icontains',
                    'vrdescsest__icontains': 'vrdescsest__icontains',
                    'vrcalcsest__icontains': 'vrcalcsest__icontains',
                    'vrdescsenat__icontains': 'vrdescsenat__icontains',
                    'vrcalcsenat__icontains': 'vrcalcsenat__icontains',
                    'vrsalfam__icontains': 'vrsalfam__icontains',
                    'vrsalmat__icontains': 'vrsalmat__icontains', }
                    
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
                    
        dict_qs = clear_dict_fields(dict_fields)
        s5011_basesremun_lista = s5011basesRemun.objects.filter(**dict_qs).filter().exclude(id=0).all()
        
        if not post and len(s5011_basesremun_lista) > 100:
        
            filtrar = True
            s5011_basesremun_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
            
        #[VARIAVEIS_LISTA_FILTRO_RELATORIO]
        #s5011_basesremun_listar_custom
        
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'output': output,
            's5011_basesremun_lista': s5011_basesremun_lista, 
            'modulos': ['s5011', ],
            'paginas': ['s5011_basesremun', ],
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
                template='s5011_basesremun_listar.html',
                filename="s5011_basesremun.pdf",
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
            response = render_to_response('s5011_basesremun_listar.html', context)
            filename = "s5011_basesremun.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
            
        elif output == 'csv':
        
            from django.shortcuts import render_to_response
            response = render_to_response('csv/s5011_basesremun.csv', context)
            filename = "s5011_basesremun.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        
        else:
        
            return render(request, 's5011_basesremun_listar.html', context)
            
    else:
    
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'output': output,
            'data': datetime.datetime.now(),
            'modulos': ['s5011', ],
            'paginas': ['s5011_basesremun', ],
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)