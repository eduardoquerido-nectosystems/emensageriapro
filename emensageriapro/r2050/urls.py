#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.r2050.views import r2050_tipocom_apagar as r2050_tipocom_apagar_views
from emensageriapro.r2050.views import r2050_tipocom_listar as r2050_tipocom_listar_views
from emensageriapro.r2050.views import r2050_tipocom_salvar as r2050_tipocom_salvar_views
from emensageriapro.r2050.views import r2050_tipocom_api as r2050_tipocom_api_views
from emensageriapro.r2050.views import r2050_infoproc_apagar as r2050_infoproc_apagar_views
from emensageriapro.r2050.views import r2050_infoproc_listar as r2050_infoproc_listar_views
from emensageriapro.r2050.views import r2050_infoproc_salvar as r2050_infoproc_salvar_views
from emensageriapro.r2050.views import r2050_infoproc_api as r2050_infoproc_api_views


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


urlpatterns = [


    url(r'^r2050-tipocom/apagar/(?P<pk>[0-9]+)/$',
        r2050_tipocom_apagar_views.apagar,
        name='r2050_tipocom_apagar'),

    url(r'^r2050-tipocom/api/$',
        r2050_tipocom_api_views.r2050tipoComList.as_view() ),

    url(r'^r2050-tipocom/api/(?P<pk>[0-9]+)/$',
        r2050_tipocom_api_views.r2050tipoComDetail.as_view() ),

    url(r'^r2050-tipocom/$',
        r2050_tipocom_listar_views.listar,
        name='r2050_tipocom'),

    url(r'^r2050-tipocom/salvar/(?P<pk>[0-9]+)/$',
        r2050_tipocom_salvar_views.salvar,
        name='r2050_tipocom_salvar'),

    url(r'^r2050-tipocom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2050_tipocom_salvar_views.salvar,
        name='r2050_tipocom_salvar_tab'),

    url(r'^r2050-tipocom/cadastrar/$',
        r2050_tipocom_salvar_views.salvar,
        name='r2050_tipocom_cadastrar'),

    url(r'^r2050-tipocom/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r2050_tipocom_salvar_views.salvar,
        name='r2050_tipocom_salvar_output'),

    url(r'^r2050-tipocom/(?P<output>[\w-]+)/$',
        r2050_tipocom_listar_views.listar,
        name='r2050_tipocom_output'),

    url(r'^r2050-infoproc/apagar/(?P<pk>[0-9]+)/$',
        r2050_infoproc_apagar_views.apagar,
        name='r2050_infoproc_apagar'),

    url(r'^r2050-infoproc/api/$',
        r2050_infoproc_api_views.r2050infoProcList.as_view() ),

    url(r'^r2050-infoproc/api/(?P<pk>[0-9]+)/$',
        r2050_infoproc_api_views.r2050infoProcDetail.as_view() ),

    url(r'^r2050-infoproc/$',
        r2050_infoproc_listar_views.listar,
        name='r2050_infoproc'),

    url(r'^r2050-infoproc/salvar/(?P<pk>[0-9]+)/$',
        r2050_infoproc_salvar_views.salvar,
        name='r2050_infoproc_salvar'),

    url(r'^r2050-infoproc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r2050_infoproc_salvar_views.salvar,
        name='r2050_infoproc_salvar_tab'),

    url(r'^r2050-infoproc/cadastrar/$',
        r2050_infoproc_salvar_views.salvar,
        name='r2050_infoproc_cadastrar'),

    url(r'^r2050-infoproc/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r2050_infoproc_salvar_views.salvar,
        name='r2050_infoproc_salvar_output'),

    url(r'^r2050-infoproc/(?P<output>[\w-]+)/$',
        r2050_infoproc_listar_views.listar,
        name='r2050_infoproc_output'),


]