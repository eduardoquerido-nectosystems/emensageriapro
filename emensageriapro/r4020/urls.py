#coding:utf-8
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from emensageriapro.r4020.views import r4020_idepgto_apagar as r4020_idepgto_apagar_views
from emensageriapro.r4020.views import r4020_idepgto_listar as r4020_idepgto_listar_views
from emensageriapro.r4020.views import r4020_idepgto_salvar as r4020_idepgto_salvar_views
from emensageriapro.r4020.views import r4020_idepgto_api as r4020_idepgto_api_views
from emensageriapro.r4020.views import r4020_infopgto_apagar as r4020_infopgto_apagar_views
from emensageriapro.r4020.views import r4020_infopgto_listar as r4020_infopgto_listar_views
from emensageriapro.r4020.views import r4020_infopgto_salvar as r4020_infopgto_salvar_views
from emensageriapro.r4020.views import r4020_infopgto_api as r4020_infopgto_api_views
from emensageriapro.r4020.views import r4020_ir_apagar as r4020_ir_apagar_views
from emensageriapro.r4020.views import r4020_ir_listar as r4020_ir_listar_views
from emensageriapro.r4020.views import r4020_ir_salvar as r4020_ir_salvar_views
from emensageriapro.r4020.views import r4020_ir_api as r4020_ir_api_views
from emensageriapro.r4020.views import r4020_csll_apagar as r4020_csll_apagar_views
from emensageriapro.r4020.views import r4020_csll_listar as r4020_csll_listar_views
from emensageriapro.r4020.views import r4020_csll_salvar as r4020_csll_salvar_views
from emensageriapro.r4020.views import r4020_csll_api as r4020_csll_api_views
from emensageriapro.r4020.views import r4020_cofins_apagar as r4020_cofins_apagar_views
from emensageriapro.r4020.views import r4020_cofins_listar as r4020_cofins_listar_views
from emensageriapro.r4020.views import r4020_cofins_salvar as r4020_cofins_salvar_views
from emensageriapro.r4020.views import r4020_cofins_api as r4020_cofins_api_views
from emensageriapro.r4020.views import r4020_pp_apagar as r4020_pp_apagar_views
from emensageriapro.r4020.views import r4020_pp_listar as r4020_pp_listar_views
from emensageriapro.r4020.views import r4020_pp_salvar as r4020_pp_salvar_views
from emensageriapro.r4020.views import r4020_pp_api as r4020_pp_api_views
from emensageriapro.r4020.views import r4020_fci_apagar as r4020_fci_apagar_views
from emensageriapro.r4020.views import r4020_fci_listar as r4020_fci_listar_views
from emensageriapro.r4020.views import r4020_fci_salvar as r4020_fci_salvar_views
from emensageriapro.r4020.views import r4020_fci_api as r4020_fci_api_views
from emensageriapro.r4020.views import r4020_scp_apagar as r4020_scp_apagar_views
from emensageriapro.r4020.views import r4020_scp_listar as r4020_scp_listar_views
from emensageriapro.r4020.views import r4020_scp_salvar as r4020_scp_salvar_views
from emensageriapro.r4020.views import r4020_scp_api as r4020_scp_api_views
from emensageriapro.r4020.views import r4020_infoprocret_apagar as r4020_infoprocret_apagar_views
from emensageriapro.r4020.views import r4020_infoprocret_listar as r4020_infoprocret_listar_views
from emensageriapro.r4020.views import r4020_infoprocret_salvar as r4020_infoprocret_salvar_views
from emensageriapro.r4020.views import r4020_infoprocret_api as r4020_infoprocret_api_views
from emensageriapro.r4020.views import r4020_infoprocjud_apagar as r4020_infoprocjud_apagar_views
from emensageriapro.r4020.views import r4020_infoprocjud_listar as r4020_infoprocjud_listar_views
from emensageriapro.r4020.views import r4020_infoprocjud_salvar as r4020_infoprocjud_salvar_views
from emensageriapro.r4020.views import r4020_infoprocjud_api as r4020_infoprocjud_api_views
from emensageriapro.r4020.views import r4020_despprocjud_apagar as r4020_despprocjud_apagar_views
from emensageriapro.r4020.views import r4020_despprocjud_listar as r4020_despprocjud_listar_views
from emensageriapro.r4020.views import r4020_despprocjud_salvar as r4020_despprocjud_salvar_views
from emensageriapro.r4020.views import r4020_despprocjud_api as r4020_despprocjud_api_views
from emensageriapro.r4020.views import r4020_ideadv_apagar as r4020_ideadv_apagar_views
from emensageriapro.r4020.views import r4020_ideadv_listar as r4020_ideadv_listar_views
from emensageriapro.r4020.views import r4020_ideadv_salvar as r4020_ideadv_salvar_views
from emensageriapro.r4020.views import r4020_ideadv_api as r4020_ideadv_api_views
from emensageriapro.r4020.views import r4020_origemrec_apagar as r4020_origemrec_apagar_views
from emensageriapro.r4020.views import r4020_origemrec_listar as r4020_origemrec_listar_views
from emensageriapro.r4020.views import r4020_origemrec_salvar as r4020_origemrec_salvar_views
from emensageriapro.r4020.views import r4020_origemrec_api as r4020_origemrec_api_views
from emensageriapro.r4020.views import r4020_infopgtoext_apagar as r4020_infopgtoext_apagar_views
from emensageriapro.r4020.views import r4020_infopgtoext_listar as r4020_infopgtoext_listar_views
from emensageriapro.r4020.views import r4020_infopgtoext_salvar as r4020_infopgtoext_salvar_views
from emensageriapro.r4020.views import r4020_infopgtoext_api as r4020_infopgtoext_api_views


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


    url(r'^r4020-idepgto/apagar/(?P<pk>[0-9]+)/$',
        r4020_idepgto_apagar_views.apagar,
        name='r4020_idepgto_apagar'),

    url(r'^r4020-idepgto/api/$',
        r4020_idepgto_api_views.r4020idePgtoList.as_view() ),

    url(r'^r4020-idepgto/api/(?P<pk>[0-9]+)/$',
        r4020_idepgto_api_views.r4020idePgtoDetail.as_view() ),

    url(r'^r4020-idepgto/$',
        r4020_idepgto_listar_views.listar,
        name='r4020_idepgto'),

    url(r'^r4020-idepgto/salvar/(?P<pk>[0-9]+)/$',
        r4020_idepgto_salvar_views.salvar,
        name='r4020_idepgto_salvar'),

    url(r'^r4020-idepgto/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4020_idepgto_salvar_views.salvar,
        name='r4020_idepgto_salvar_tab'),

    url(r'^r4020-idepgto/cadastrar/$',
        r4020_idepgto_salvar_views.salvar,
        name='r4020_idepgto_cadastrar'),

    url(r'^r4020-idepgto/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4020_idepgto_salvar_views.salvar,
        name='r4020_idepgto_salvar_output'),

    url(r'^r4020-idepgto/(?P<output>[\w-]+)/$',
        r4020_idepgto_listar_views.listar,
        name='r4020_idepgto_output'),

    url(r'^r4020-infopgto/apagar/(?P<pk>[0-9]+)/$',
        r4020_infopgto_apagar_views.apagar,
        name='r4020_infopgto_apagar'),

    url(r'^r4020-infopgto/api/$',
        r4020_infopgto_api_views.r4020infoPgtoList.as_view() ),

    url(r'^r4020-infopgto/api/(?P<pk>[0-9]+)/$',
        r4020_infopgto_api_views.r4020infoPgtoDetail.as_view() ),

    url(r'^r4020-infopgto/$',
        r4020_infopgto_listar_views.listar,
        name='r4020_infopgto'),

    url(r'^r4020-infopgto/salvar/(?P<pk>[0-9]+)/$',
        r4020_infopgto_salvar_views.salvar,
        name='r4020_infopgto_salvar'),

    url(r'^r4020-infopgto/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4020_infopgto_salvar_views.salvar,
        name='r4020_infopgto_salvar_tab'),

    url(r'^r4020-infopgto/cadastrar/$',
        r4020_infopgto_salvar_views.salvar,
        name='r4020_infopgto_cadastrar'),

    url(r'^r4020-infopgto/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4020_infopgto_salvar_views.salvar,
        name='r4020_infopgto_salvar_output'),

    url(r'^r4020-infopgto/(?P<output>[\w-]+)/$',
        r4020_infopgto_listar_views.listar,
        name='r4020_infopgto_output'),

    url(r'^r4020-ir/apagar/(?P<pk>[0-9]+)/$',
        r4020_ir_apagar_views.apagar,
        name='r4020_ir_apagar'),

    url(r'^r4020-ir/api/$',
        r4020_ir_api_views.r4020IRList.as_view() ),

    url(r'^r4020-ir/api/(?P<pk>[0-9]+)/$',
        r4020_ir_api_views.r4020IRDetail.as_view() ),

    url(r'^r4020-ir/$',
        r4020_ir_listar_views.listar,
        name='r4020_ir'),

    url(r'^r4020-ir/salvar/(?P<pk>[0-9]+)/$',
        r4020_ir_salvar_views.salvar,
        name='r4020_ir_salvar'),

    url(r'^r4020-ir/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4020_ir_salvar_views.salvar,
        name='r4020_ir_salvar_tab'),

    url(r'^r4020-ir/cadastrar/$',
        r4020_ir_salvar_views.salvar,
        name='r4020_ir_cadastrar'),

    url(r'^r4020-ir/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4020_ir_salvar_views.salvar,
        name='r4020_ir_salvar_output'),

    url(r'^r4020-ir/(?P<output>[\w-]+)/$',
        r4020_ir_listar_views.listar,
        name='r4020_ir_output'),

    url(r'^r4020-csll/apagar/(?P<pk>[0-9]+)/$',
        r4020_csll_apagar_views.apagar,
        name='r4020_csll_apagar'),

    url(r'^r4020-csll/api/$',
        r4020_csll_api_views.r4020CSLLList.as_view() ),

    url(r'^r4020-csll/api/(?P<pk>[0-9]+)/$',
        r4020_csll_api_views.r4020CSLLDetail.as_view() ),

    url(r'^r4020-csll/$',
        r4020_csll_listar_views.listar,
        name='r4020_csll'),

    url(r'^r4020-csll/salvar/(?P<pk>[0-9]+)/$',
        r4020_csll_salvar_views.salvar,
        name='r4020_csll_salvar'),

    url(r'^r4020-csll/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4020_csll_salvar_views.salvar,
        name='r4020_csll_salvar_tab'),

    url(r'^r4020-csll/cadastrar/$',
        r4020_csll_salvar_views.salvar,
        name='r4020_csll_cadastrar'),

    url(r'^r4020-csll/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4020_csll_salvar_views.salvar,
        name='r4020_csll_salvar_output'),

    url(r'^r4020-csll/(?P<output>[\w-]+)/$',
        r4020_csll_listar_views.listar,
        name='r4020_csll_output'),

    url(r'^r4020-cofins/apagar/(?P<pk>[0-9]+)/$',
        r4020_cofins_apagar_views.apagar,
        name='r4020_cofins_apagar'),

    url(r'^r4020-cofins/api/$',
        r4020_cofins_api_views.r4020CofinsList.as_view() ),

    url(r'^r4020-cofins/api/(?P<pk>[0-9]+)/$',
        r4020_cofins_api_views.r4020CofinsDetail.as_view() ),

    url(r'^r4020-cofins/$',
        r4020_cofins_listar_views.listar,
        name='r4020_cofins'),

    url(r'^r4020-cofins/salvar/(?P<pk>[0-9]+)/$',
        r4020_cofins_salvar_views.salvar,
        name='r4020_cofins_salvar'),

    url(r'^r4020-cofins/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4020_cofins_salvar_views.salvar,
        name='r4020_cofins_salvar_tab'),

    url(r'^r4020-cofins/cadastrar/$',
        r4020_cofins_salvar_views.salvar,
        name='r4020_cofins_cadastrar'),

    url(r'^r4020-cofins/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4020_cofins_salvar_views.salvar,
        name='r4020_cofins_salvar_output'),

    url(r'^r4020-cofins/(?P<output>[\w-]+)/$',
        r4020_cofins_listar_views.listar,
        name='r4020_cofins_output'),

    url(r'^r4020-pp/apagar/(?P<pk>[0-9]+)/$',
        r4020_pp_apagar_views.apagar,
        name='r4020_pp_apagar'),

    url(r'^r4020-pp/api/$',
        r4020_pp_api_views.r4020PPList.as_view() ),

    url(r'^r4020-pp/api/(?P<pk>[0-9]+)/$',
        r4020_pp_api_views.r4020PPDetail.as_view() ),

    url(r'^r4020-pp/$',
        r4020_pp_listar_views.listar,
        name='r4020_pp'),

    url(r'^r4020-pp/salvar/(?P<pk>[0-9]+)/$',
        r4020_pp_salvar_views.salvar,
        name='r4020_pp_salvar'),

    url(r'^r4020-pp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4020_pp_salvar_views.salvar,
        name='r4020_pp_salvar_tab'),

    url(r'^r4020-pp/cadastrar/$',
        r4020_pp_salvar_views.salvar,
        name='r4020_pp_cadastrar'),

    url(r'^r4020-pp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4020_pp_salvar_views.salvar,
        name='r4020_pp_salvar_output'),

    url(r'^r4020-pp/(?P<output>[\w-]+)/$',
        r4020_pp_listar_views.listar,
        name='r4020_pp_output'),

    url(r'^r4020-fci/apagar/(?P<pk>[0-9]+)/$',
        r4020_fci_apagar_views.apagar,
        name='r4020_fci_apagar'),

    url(r'^r4020-fci/api/$',
        r4020_fci_api_views.r4020FCIList.as_view() ),

    url(r'^r4020-fci/api/(?P<pk>[0-9]+)/$',
        r4020_fci_api_views.r4020FCIDetail.as_view() ),

    url(r'^r4020-fci/$',
        r4020_fci_listar_views.listar,
        name='r4020_fci'),

    url(r'^r4020-fci/salvar/(?P<pk>[0-9]+)/$',
        r4020_fci_salvar_views.salvar,
        name='r4020_fci_salvar'),

    url(r'^r4020-fci/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4020_fci_salvar_views.salvar,
        name='r4020_fci_salvar_tab'),

    url(r'^r4020-fci/cadastrar/$',
        r4020_fci_salvar_views.salvar,
        name='r4020_fci_cadastrar'),

    url(r'^r4020-fci/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4020_fci_salvar_views.salvar,
        name='r4020_fci_salvar_output'),

    url(r'^r4020-fci/(?P<output>[\w-]+)/$',
        r4020_fci_listar_views.listar,
        name='r4020_fci_output'),

    url(r'^r4020-scp/apagar/(?P<pk>[0-9]+)/$',
        r4020_scp_apagar_views.apagar,
        name='r4020_scp_apagar'),

    url(r'^r4020-scp/api/$',
        r4020_scp_api_views.r4020SCPList.as_view() ),

    url(r'^r4020-scp/api/(?P<pk>[0-9]+)/$',
        r4020_scp_api_views.r4020SCPDetail.as_view() ),

    url(r'^r4020-scp/$',
        r4020_scp_listar_views.listar,
        name='r4020_scp'),

    url(r'^r4020-scp/salvar/(?P<pk>[0-9]+)/$',
        r4020_scp_salvar_views.salvar,
        name='r4020_scp_salvar'),

    url(r'^r4020-scp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4020_scp_salvar_views.salvar,
        name='r4020_scp_salvar_tab'),

    url(r'^r4020-scp/cadastrar/$',
        r4020_scp_salvar_views.salvar,
        name='r4020_scp_cadastrar'),

    url(r'^r4020-scp/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4020_scp_salvar_views.salvar,
        name='r4020_scp_salvar_output'),

    url(r'^r4020-scp/(?P<output>[\w-]+)/$',
        r4020_scp_listar_views.listar,
        name='r4020_scp_output'),

    url(r'^r4020-infoprocret/apagar/(?P<pk>[0-9]+)/$',
        r4020_infoprocret_apagar_views.apagar,
        name='r4020_infoprocret_apagar'),

    url(r'^r4020-infoprocret/api/$',
        r4020_infoprocret_api_views.r4020infoProcRetList.as_view() ),

    url(r'^r4020-infoprocret/api/(?P<pk>[0-9]+)/$',
        r4020_infoprocret_api_views.r4020infoProcRetDetail.as_view() ),

    url(r'^r4020-infoprocret/$',
        r4020_infoprocret_listar_views.listar,
        name='r4020_infoprocret'),

    url(r'^r4020-infoprocret/salvar/(?P<pk>[0-9]+)/$',
        r4020_infoprocret_salvar_views.salvar,
        name='r4020_infoprocret_salvar'),

    url(r'^r4020-infoprocret/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4020_infoprocret_salvar_views.salvar,
        name='r4020_infoprocret_salvar_tab'),

    url(r'^r4020-infoprocret/cadastrar/$',
        r4020_infoprocret_salvar_views.salvar,
        name='r4020_infoprocret_cadastrar'),

    url(r'^r4020-infoprocret/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4020_infoprocret_salvar_views.salvar,
        name='r4020_infoprocret_salvar_output'),

    url(r'^r4020-infoprocret/(?P<output>[\w-]+)/$',
        r4020_infoprocret_listar_views.listar,
        name='r4020_infoprocret_output'),

    url(r'^r4020-infoprocjud/apagar/(?P<pk>[0-9]+)/$',
        r4020_infoprocjud_apagar_views.apagar,
        name='r4020_infoprocjud_apagar'),

    url(r'^r4020-infoprocjud/api/$',
        r4020_infoprocjud_api_views.r4020infoProcJudList.as_view() ),

    url(r'^r4020-infoprocjud/api/(?P<pk>[0-9]+)/$',
        r4020_infoprocjud_api_views.r4020infoProcJudDetail.as_view() ),

    url(r'^r4020-infoprocjud/$',
        r4020_infoprocjud_listar_views.listar,
        name='r4020_infoprocjud'),

    url(r'^r4020-infoprocjud/salvar/(?P<pk>[0-9]+)/$',
        r4020_infoprocjud_salvar_views.salvar,
        name='r4020_infoprocjud_salvar'),

    url(r'^r4020-infoprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4020_infoprocjud_salvar_views.salvar,
        name='r4020_infoprocjud_salvar_tab'),

    url(r'^r4020-infoprocjud/cadastrar/$',
        r4020_infoprocjud_salvar_views.salvar,
        name='r4020_infoprocjud_cadastrar'),

    url(r'^r4020-infoprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4020_infoprocjud_salvar_views.salvar,
        name='r4020_infoprocjud_salvar_output'),

    url(r'^r4020-infoprocjud/(?P<output>[\w-]+)/$',
        r4020_infoprocjud_listar_views.listar,
        name='r4020_infoprocjud_output'),

    url(r'^r4020-despprocjud/apagar/(?P<pk>[0-9]+)/$',
        r4020_despprocjud_apagar_views.apagar,
        name='r4020_despprocjud_apagar'),

    url(r'^r4020-despprocjud/api/$',
        r4020_despprocjud_api_views.r4020despProcJudList.as_view() ),

    url(r'^r4020-despprocjud/api/(?P<pk>[0-9]+)/$',
        r4020_despprocjud_api_views.r4020despProcJudDetail.as_view() ),

    url(r'^r4020-despprocjud/$',
        r4020_despprocjud_listar_views.listar,
        name='r4020_despprocjud'),

    url(r'^r4020-despprocjud/salvar/(?P<pk>[0-9]+)/$',
        r4020_despprocjud_salvar_views.salvar,
        name='r4020_despprocjud_salvar'),

    url(r'^r4020-despprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4020_despprocjud_salvar_views.salvar,
        name='r4020_despprocjud_salvar_tab'),

    url(r'^r4020-despprocjud/cadastrar/$',
        r4020_despprocjud_salvar_views.salvar,
        name='r4020_despprocjud_cadastrar'),

    url(r'^r4020-despprocjud/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4020_despprocjud_salvar_views.salvar,
        name='r4020_despprocjud_salvar_output'),

    url(r'^r4020-despprocjud/(?P<output>[\w-]+)/$',
        r4020_despprocjud_listar_views.listar,
        name='r4020_despprocjud_output'),

    url(r'^r4020-ideadv/apagar/(?P<pk>[0-9]+)/$',
        r4020_ideadv_apagar_views.apagar,
        name='r4020_ideadv_apagar'),

    url(r'^r4020-ideadv/api/$',
        r4020_ideadv_api_views.r4020ideAdvList.as_view() ),

    url(r'^r4020-ideadv/api/(?P<pk>[0-9]+)/$',
        r4020_ideadv_api_views.r4020ideAdvDetail.as_view() ),

    url(r'^r4020-ideadv/$',
        r4020_ideadv_listar_views.listar,
        name='r4020_ideadv'),

    url(r'^r4020-ideadv/salvar/(?P<pk>[0-9]+)/$',
        r4020_ideadv_salvar_views.salvar,
        name='r4020_ideadv_salvar'),

    url(r'^r4020-ideadv/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4020_ideadv_salvar_views.salvar,
        name='r4020_ideadv_salvar_tab'),

    url(r'^r4020-ideadv/cadastrar/$',
        r4020_ideadv_salvar_views.salvar,
        name='r4020_ideadv_cadastrar'),

    url(r'^r4020-ideadv/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4020_ideadv_salvar_views.salvar,
        name='r4020_ideadv_salvar_output'),

    url(r'^r4020-ideadv/(?P<output>[\w-]+)/$',
        r4020_ideadv_listar_views.listar,
        name='r4020_ideadv_output'),

    url(r'^r4020-origemrec/apagar/(?P<pk>[0-9]+)/$',
        r4020_origemrec_apagar_views.apagar,
        name='r4020_origemrec_apagar'),

    url(r'^r4020-origemrec/api/$',
        r4020_origemrec_api_views.r4020origemRecList.as_view() ),

    url(r'^r4020-origemrec/api/(?P<pk>[0-9]+)/$',
        r4020_origemrec_api_views.r4020origemRecDetail.as_view() ),

    url(r'^r4020-origemrec/$',
        r4020_origemrec_listar_views.listar,
        name='r4020_origemrec'),

    url(r'^r4020-origemrec/salvar/(?P<pk>[0-9]+)/$',
        r4020_origemrec_salvar_views.salvar,
        name='r4020_origemrec_salvar'),

    url(r'^r4020-origemrec/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4020_origemrec_salvar_views.salvar,
        name='r4020_origemrec_salvar_tab'),

    url(r'^r4020-origemrec/cadastrar/$',
        r4020_origemrec_salvar_views.salvar,
        name='r4020_origemrec_cadastrar'),

    url(r'^r4020-origemrec/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4020_origemrec_salvar_views.salvar,
        name='r4020_origemrec_salvar_output'),

    url(r'^r4020-origemrec/(?P<output>[\w-]+)/$',
        r4020_origemrec_listar_views.listar,
        name='r4020_origemrec_output'),

    url(r'^r4020-infopgtoext/apagar/(?P<pk>[0-9]+)/$',
        r4020_infopgtoext_apagar_views.apagar,
        name='r4020_infopgtoext_apagar'),

    url(r'^r4020-infopgtoext/api/$',
        r4020_infopgtoext_api_views.r4020infoPgtoExtList.as_view() ),

    url(r'^r4020-infopgtoext/api/(?P<pk>[0-9]+)/$',
        r4020_infopgtoext_api_views.r4020infoPgtoExtDetail.as_view() ),

    url(r'^r4020-infopgtoext/$',
        r4020_infopgtoext_listar_views.listar,
        name='r4020_infopgtoext'),

    url(r'^r4020-infopgtoext/salvar/(?P<pk>[0-9]+)/$',
        r4020_infopgtoext_salvar_views.salvar,
        name='r4020_infopgtoext_salvar'),

    url(r'^r4020-infopgtoext/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/$',
        r4020_infopgtoext_salvar_views.salvar,
        name='r4020_infopgtoext_salvar_tab'),

    url(r'^r4020-infopgtoext/cadastrar/$',
        r4020_infopgtoext_salvar_views.salvar,
        name='r4020_infopgtoext_cadastrar'),

    url(r'^r4020-infopgtoext/salvar/(?P<pk>[0-9]+)/(?P<tab>[\w-]+)/(?P<output>[\w-]+)/$',
        r4020_infopgtoext_salvar_views.salvar,
        name='r4020_infopgtoext_salvar_output'),

    url(r'^r4020-infopgtoext/(?P<output>[\w-]+)/$',
        r4020_infopgtoext_listar_views.listar,
        name='r4020_infopgtoext_output'),


]