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
from emensageriapro.s2200.models import s2200CTPS
from emensageriapro.s2200.forms import form_s2200_ctps
from emensageriapro.s2200.models import s2200RIC
from emensageriapro.s2200.forms import form_s2200_ric
from emensageriapro.s2200.models import s2200RG
from emensageriapro.s2200.forms import form_s2200_rg
from emensageriapro.s2200.models import s2200RNE
from emensageriapro.s2200.forms import form_s2200_rne
from emensageriapro.s2200.models import s2200OC
from emensageriapro.s2200.forms import form_s2200_oc
from emensageriapro.s2200.models import s2200CNH
from emensageriapro.s2200.forms import form_s2200_cnh



@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO

    evento_dados = {}
    evento_dados['status'] = STATUS_EVENTO_CADASTRADO

    if pk:

        s2200_documentos = get_object_or_404(s2200documentos, id=pk)
        evento_dados = s2200_documentos.evento()

    if request.user.has_perm('s2200.can_see_s2200documentos'):

        if pk:

            s2200_documentos_form = form_s2200_documentos(
                request.POST or None,
                instance=s2200_documentos)
                     
        else:

            s2200_documentos_form = form_s2200_documentos(request.POST or None)
                     
        if request.method == 'POST':

            if s2200_documentos_form.is_valid():

                obj = s2200_documentos_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                 
                if 'return_page' in request.session and request.session['return_page'] and 's2200-documentos' not in request.session['return_page']:

                    return HttpResponseRedirect(request.session['return_page'])

                if pk != obj.id:

                    return redirect(
                        's2200_documentos_salvar',
                        pk=obj.id)

            else:

                messages.error(request, u'Erro ao salvar!')

        s2200_documentos_form = disabled_form_fields(
            s2200_documentos_form,
            request.user.has_perm('s2200.change_s2200documentos'))

        if pk:

            if evento_dados['status'] != STATUS_EVENTO_CADASTRADO:

                s2200_documentos_form = disabled_form_fields(s2200_documentos_form, 0)

        if output:

            s2200_documentos_form = disabled_form_for_print(s2200_documentos_form)


        s2200_ctps_lista = None
        s2200_ctps_form = None
        s2200_ric_lista = None
        s2200_ric_form = None
        s2200_rg_lista = None
        s2200_rg_form = None
        s2200_rne_lista = None
        s2200_rne_form = None
        s2200_oc_lista = None
        s2200_oc_form = None
        s2200_cnh_lista = None
        s2200_cnh_form = None

        if pk:

            s2200_documentos = get_object_or_404(s2200documentos, id=pk)

            s2200_ctps_form = form_s2200_ctps(
                initial={ 's2200_documentos': s2200_documentos })
            s2200_ctps_form.fields['s2200_documentos'].widget.attrs['readonly'] = True
            s2200_ctps_lista = s2200CTPS.objects.\
                filter(s2200_documentos_id=s2200_documentos.id).all()

            s2200_ric_form = form_s2200_ric(
                initial={ 's2200_documentos': s2200_documentos })
            s2200_ric_form.fields['s2200_documentos'].widget.attrs['readonly'] = True
            s2200_ric_lista = s2200RIC.objects.\
                filter(s2200_documentos_id=s2200_documentos.id).all()

            s2200_rg_form = form_s2200_rg(
                initial={ 's2200_documentos': s2200_documentos })
            s2200_rg_form.fields['s2200_documentos'].widget.attrs['readonly'] = True
            s2200_rg_lista = s2200RG.objects.\
                filter(s2200_documentos_id=s2200_documentos.id).all()

            s2200_rne_form = form_s2200_rne(
                initial={ 's2200_documentos': s2200_documentos })
            s2200_rne_form.fields['s2200_documentos'].widget.attrs['readonly'] = True
            s2200_rne_lista = s2200RNE.objects.\
                filter(s2200_documentos_id=s2200_documentos.id).all()

            s2200_oc_form = form_s2200_oc(
                initial={ 's2200_documentos': s2200_documentos })
            s2200_oc_form.fields['s2200_documentos'].widget.attrs['readonly'] = True
            s2200_oc_lista = s2200OC.objects.\
                filter(s2200_documentos_id=s2200_documentos.id).all()

            s2200_cnh_form = form_s2200_cnh(
                initial={ 's2200_documentos': s2200_documentos })
            s2200_cnh_form.fields['s2200_documentos'].widget.attrs['readonly'] = True
            s2200_cnh_lista = s2200CNH.objects.\
                filter(s2200_documentos_id=s2200_documentos.id).all()


        else:

            s2200_documentos = None

        tabelas_secundarias = []

        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s2200_documentos').all()

        if not request.POST:
            request.session['return_page'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_dados': evento_dados,
            'controle_alteracoes': controle_alteracoes,
            's2200_documentos': s2200_documentos,
            's2200_documentos_form': s2200_documentos_form,
            'modulos': ['s2200', ],
            'paginas': ['s2200_documentos', ],
            's2200_ctps_form': s2200_ctps_form,
            's2200_ctps_lista': s2200_ctps_lista,
            's2200_ric_form': s2200_ric_form,
            's2200_ric_lista': s2200_ric_lista,
            's2200_rg_form': s2200_rg_form,
            's2200_rg_lista': s2200_rg_lista,
            's2200_rne_form': s2200_rne_form,
            's2200_rne_lista': s2200_rne_lista,
            's2200_oc_form': s2200_oc_form,
            's2200_oc_lista': s2200_oc_lista,
            's2200_cnh_form': s2200_cnh_form,
            's2200_cnh_lista': s2200_cnh_lista,
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #s2200_documentos_salvar_custom_variaveis_context#
        }

        if output == 'pdf':

            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='s2200_documentos_salvar.html',
                filename="s2200_documentos.pdf",
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

            response = render_to_response('s2200_documentos_salvar.html', context)
            filename = "s2200_documentos.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 's2200_documentos_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['s2200', ],
            'paginas': ['s2200_documentos', ],
            'data': datetime.datetime.now(),
        }

        return render(request,
                      'permissao_negada.html',
                      context)