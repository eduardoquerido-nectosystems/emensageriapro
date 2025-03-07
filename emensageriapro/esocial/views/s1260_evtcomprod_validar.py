#coding:utf-8


"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos<www.emensageria.com.br>
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


import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s1260_evtcomprod(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtComProd = doc.eSocial.evtComProd
    #variaveis

    if 'ideEvento' in dir(evtComProd.ideEvento):
        for ideEvento in evtComProd.ideEvento:

            if 'indRetif' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.indRetif',
                                                  ideEvento.indRetif.cdata,
                                                  1, u'1, 2')

            if 'nrRecibo' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.nrRecibo',
                                                  ideEvento.nrRecibo.cdata,
                                                  0, u'None')

            if 'indApuracao' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.indApuracao',
                                                  ideEvento.indApuracao.cdata,
                                                  1, u'1')

            if 'perApur' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.perApur',
                                                  ideEvento.perApur.cdata,
                                                  1, u'None')

            if 'tpAmb' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.tpAmb',
                                                  ideEvento.tpAmb.cdata,
                                                  1, u'1, 2')

            if 'procEmi' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.procEmi',
                                                  ideEvento.procEmi.cdata,
                                                  1, u'1, 2, 3, 4, 5')

            if 'verProc' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.verProc',
                                                  ideEvento.verProc.cdata,
                                                  1, u'None')

    if 'ideEmpregador' in dir(evtComProd.ideEmpregador):
        for ideEmpregador in evtComProd.ideEmpregador:

            if 'tpInsc' in dir(ideEmpregador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEmpregador.tpInsc',
                                                  ideEmpregador.tpInsc.cdata,
                                                  1, u'1, 2, 3, 4, 5')

            if 'nrInsc' in dir(ideEmpregador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEmpregador.nrInsc',
                                                  ideEmpregador.nrInsc.cdata,
                                                  1, u'None')

    if 'infoComProd' in dir(evtComProd.infoComProd):
        for infoComProd in evtComProd.infoComProd:

            if 'ideEstabel' in dir(infoComProd.ideEstabel):
                for ideEstabel in infoComProd.ideEstabel:

                    if 'nrInscEstabRural' in dir(ideEstabel):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideEstabel.nrInscEstabRural',
                                                          ideEstabel.nrInscEstabRural.cdata,
                                                          1, u'None')

                    if 'tpComerc' in dir(ideEstabel.tpComerc):
                        for tpComerc in ideEstabel.tpComerc:
        
                            if 'indComerc' in dir(tpComerc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'tpComerc.indComerc',
                                                                  tpComerc.indComerc.cdata,
                                                                  1, u'2, 3, 7, 8, 9')
        
                            if 'vrTotCom' in dir(tpComerc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'tpComerc.vrTotCom',
                                                                  tpComerc.vrTotCom.cdata,
                                                                  1, u'None')
        
                            if 'ideAdquir' in dir(tpComerc.ideAdquir):
                                for ideAdquir in tpComerc.ideAdquir:
                
                                    if 'tpInsc' in dir(ideAdquir):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideAdquir.tpInsc',
                                                                          ideAdquir.tpInsc.cdata,
                                                                          1, u'1, 2, 3, 4, 5')
                
                                    if 'nrInsc' in dir(ideAdquir):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideAdquir.nrInsc',
                                                                          ideAdquir.nrInsc.cdata,
                                                                          1, u'None')
                
                                    if 'vrComerc' in dir(ideAdquir):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'ideAdquir.vrComerc',
                                                                          ideAdquir.vrComerc.cdata,
                                                                          1, u'None')
                
                                    if 'nfs' in dir(ideAdquir.nfs):
                                        for nfs in ideAdquir.nfs:
                        
                                            if 'serie' in dir(nfs):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'nfs.serie',
                                                                                  nfs.serie.cdata,
                                                                                  0, u'None')
                        
                                            if 'nrDocto' in dir(nfs):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'nfs.nrDocto',
                                                                                  nfs.nrDocto.cdata,
                                                                                  1, u'None')
                        
                                            if 'dtEmisNF' in dir(nfs):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'nfs.dtEmisNF',
                                                                                  nfs.dtEmisNF.cdata,
                                                                                  1, u'None')
                        
                                            if 'vlrBruto' in dir(nfs):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'nfs.vlrBruto',
                                                                                  nfs.vlrBruto.cdata,
                                                                                  1, u'None')
                        
                                            if 'vrCPDescPR' in dir(nfs):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'nfs.vrCPDescPR',
                                                                                  nfs.vrCPDescPR.cdata,
                                                                                  1, u'None')
                        
                                            if 'vrRatDescPR' in dir(nfs):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'nfs.vrRatDescPR',
                                                                                  nfs.vrRatDescPR.cdata,
                                                                                  1, u'None')
                        
                                            if 'vrSenarDesc' in dir(nfs):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'nfs.vrSenarDesc',
                                                                                  nfs.vrSenarDesc.cdata,
                                                                                  1, u'None')
        
                            if 'infoProcJud' in dir(tpComerc.infoProcJud):
                                for infoProcJud in tpComerc.infoProcJud:
                
                                    if 'tpProc' in dir(infoProcJud):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcJud.tpProc',
                                                                          infoProcJud.tpProc.cdata,
                                                                          1, u'1, 2')
                
                                    if 'nrProc' in dir(infoProcJud):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcJud.nrProc',
                                                                          infoProcJud.nrProc.cdata,
                                                                          1, u'None')
                
                                    if 'codSusp' in dir(infoProcJud):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcJud.codSusp',
                                                                          infoProcJud.codSusp.cdata,
                                                                          1, u'None')
                
                                    if 'vrCPSusp' in dir(infoProcJud):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcJud.vrCPSusp',
                                                                          infoProcJud.vrCPSusp.cdata,
                                                                          0, u'None')
                
                                    if 'vrRatSusp' in dir(infoProcJud):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcJud.vrRatSusp',
                                                                          infoProcJud.vrRatSusp.cdata,
                                                                          0, u'None')
                
                                    if 'vrSenarSusp' in dir(infoProcJud):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoProcJud.vrSenarSusp',
                                                                          infoProcJud.vrSenarSusp.cdata,
                                                                          0, u'None')
    return validacoes_lista