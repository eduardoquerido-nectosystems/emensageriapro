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
from emensageriapro.s5013.forms import *
from emensageriapro.s5013.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s5013.models import s5013dpsPerApur
from emensageriapro.s5013.forms import form_s5013_dpsperapur
from emensageriapro.s5013.models import s5013infoDpsPerAntE
from emensageriapro.s5013.forms import form_s5013_infodpsperante



@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    
    evento_dados = {}
    evento_dados['status'] = STATUS_EVENTO_CADASTRADO
    
    if pk:
    
        s5013_infodpsfgts = get_object_or_404(s5013infoDpsFGTS, id=pk)
        evento_dados = s5013_infodpsfgts.evento()

    if request.user.has_perm('s5013.can_see_s5013infoDpsFGTS'):
        
        if pk:
        
            s5013_infodpsfgts_form = form_s5013_infodpsfgts(
                request.POST or None, 
                instance=s5013_infodpsfgts)
                                         
        else:
        
            s5013_infodpsfgts_form = form_s5013_infodpsfgts(request.POST or None)
                                         
        if request.method == 'POST':
        
            if s5013_infodpsfgts_form.is_valid():
            
                obj = s5013_infodpsfgts_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not pk:
                
                    gravar_auditoria(
                        '{}',
                        json.dumps(
                            model_to_dict(obj), 
                            indent=4, 
                            sort_keys=True, 
                            default=str), 
                        's5013_infodpsfgts', 
                        obj.id, 
                        request.user.id, 1)
                                 
                else:
                
                    gravar_auditoria(
                        json.dumps(
                            model_to_dict(s5013_infodpsfgts), 
                            indent=4, 
                            sort_keys=True, 
                            default=str),
                        json.dumps(
                            model_to_dict(obj), 
                            indent=4, 
                            sort_keys=True, 
                            default=str), 
                        's5013_infodpsfgts', 
                        pk, 
                        request.user.id, 2)
                                     
                if request.session['return_page'] not in (
                    's5013_infodpsfgts_apagar', 
                    's5013_infodpsfgts_salvar', 
                    's5013_infodpsfgts'):
                    
                    return redirect(
                        request.session['return_page'], 
                        pk=request.session['return_pk'])
                    
                if pk != obj.id:
                
                    return redirect(
                        's5013_infodpsfgts_salvar', 
                        pk=obj.id)
                    
            else:
            
                messages.error(request, u'Erro ao salvar!')
               
        s5013_infodpsfgts_form = disabled_form_fields(
            s5013_infodpsfgts_form, 
            request.user.has_perm('s5013.change_s5013infoDpsFGTS'))
        
        if pk:
        
            if evento_dados['status'] != STATUS_EVENTO_CADASTRADO:
            
                s5013_infodpsfgts_form = disabled_form_fields(s5013_infodpsfgts_form, 0)
                
        if output:
        
            s5013_infodpsfgts_form = disabled_form_for_print(s5013_infodpsfgts_form)
            
        
        s5013_dpsperapur_lista = None 
        s5013_dpsperapur_form = None 
        s5013_infodpsperante_lista = None 
        s5013_infodpsperante_form = None 
        
        if pk:
        
            s5013_infodpsfgts = get_object_or_404(s5013infoDpsFGTS, id=pk)
            
            s5013_dpsperapur_form = form_s5013_dpsperapur(
                initial={ 's5013_infodpsfgts': s5013_infodpsfgts })
            s5013_dpsperapur_form.fields['s5013_infodpsfgts'].widget.attrs['readonly'] = True
            s5013_dpsperapur_lista = s5013dpsPerApur.objects.\
                filter(s5013_infodpsfgts_id=s5013_infodpsfgts.id).all()
                
            s5013_infodpsperante_form = form_s5013_infodpsperante(
                initial={ 's5013_infodpsfgts': s5013_infodpsfgts })
            s5013_infodpsperante_form.fields['s5013_infodpsfgts'].widget.attrs['readonly'] = True
            s5013_infodpsperante_lista = s5013infoDpsPerAntE.objects.\
                filter(s5013_infodpsfgts_id=s5013_infodpsfgts.id).all()
                
                
        else:
        
            s5013_infodpsfgts = None
            
        tabelas_secundarias = []
        
        if tab or 's5013_infodpsfgts' in request.session['return_page']:
        
            request.session['return_pk'] = pk
            request.session['return_tab'] = tab
            request.session['return_page'] = 's5013_infodpsfgts_salvar'
            
        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s5013_infodpsfgts').all()
        
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_dados': evento_dados,
            'controle_alteracoes': controle_alteracoes, 
            's5013_infodpsfgts': s5013_infodpsfgts, 
            's5013_infodpsfgts_form': s5013_infodpsfgts_form, 
            'modulos': ['s5013', ],
            'paginas': ['s5013_infodpsfgts', ],
            's5013_dpsperapur_form': s5013_dpsperapur_form,
            's5013_dpsperapur_lista': s5013_dpsperapur_lista,
            's5013_infodpsperante_form': s5013_infodpsperante_form,
            's5013_infodpsperante_lista': s5013_infodpsperante_lista,
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #s5013_infodpsfgts_salvar_custom_variaveis_context#
        }
        
        if output == 'pdf':
        
            from wkhtmltopdf.views import PDFTemplateResponse
            
            response = PDFTemplateResponse(
                request=request,
                template='s5013_infodpsfgts_salvar.html',
                filename="s5013_infodpsfgts.pdf",
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
            
            response = render_to_response('s5013_infodpsfgts_salvar.html', context)
            filename = "s5013_infodpsfgts.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response
            
        else:
        
            return render(request, 's5013_infodpsfgts_salvar.html', context)

    else:
    
        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['s5013', ],
            'paginas': ['s5013_infodpsfgts', ],
            'data': datetime.datetime.now(),
        }
        
        return render(request, 
                      'permissao_negada.html', 
                      context)