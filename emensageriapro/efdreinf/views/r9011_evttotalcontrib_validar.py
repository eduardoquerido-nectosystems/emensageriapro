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


def validacoes_r9011_evttotalcontrib(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtTotalContrib = doc.Reinf.evtTotalContrib
    #variaveis

    if 'ideEvento' in dir(evtTotalContrib.ideEvento):
        for ideEvento in evtTotalContrib.ideEvento:

            if 'perApur' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.perApur',
                                                  ideEvento.perApur.cdata,
                                                  1, u'None')

    if 'ideContri' in dir(evtTotalContrib.ideContri):
        for ideContri in evtTotalContrib.ideContri:

            if 'tpInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.tpInsc',
                                                  ideContri.tpInsc.cdata,
                                                  1, u'1, 2')

            if 'nrInsc' in dir(ideContri):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideContri.nrInsc',
                                                  ideContri.nrInsc.cdata,
                                                  1, u'None')

    if 'ideRecRetorno' in dir(evtTotalContrib.ideRecRetorno):
        for ideRecRetorno in evtTotalContrib.ideRecRetorno:

            if 'ideStatus' in dir(ideRecRetorno.ideStatus):
                for ideStatus in ideRecRetorno.ideStatus:

                    if 'cdRetorno' in dir(ideStatus):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideStatus.cdRetorno',
                                                          ideStatus.cdRetorno.cdata,
                                                          1, u'0, 1, 2')

                    if 'descRetorno' in dir(ideStatus):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'ideStatus.descRetorno',
                                                          ideStatus.descRetorno.cdata,
                                                          1, u'None')

                    if 'regOcorrs' in dir(ideStatus.regOcorrs):
                        for regOcorrs in ideStatus.regOcorrs:
        
                            if 'tpOcorr' in dir(regOcorrs):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'regOcorrs.tpOcorr',
                                                                  regOcorrs.tpOcorr.cdata,
                                                                  1, u'None')
        
                            if 'localErroAviso' in dir(regOcorrs):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'regOcorrs.localErroAviso',
                                                                  regOcorrs.localErroAviso.cdata,
                                                                  1, u'None')
        
                            if 'codResp' in dir(regOcorrs):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'regOcorrs.codResp',
                                                                  regOcorrs.codResp.cdata,
                                                                  1, u'None')
        
                            if 'dscResp' in dir(regOcorrs):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'regOcorrs.dscResp',
                                                                  regOcorrs.dscResp.cdata,
                                                                  1, u'None')

    if 'infoRecEv' in dir(evtTotalContrib.infoRecEv):
        for infoRecEv in evtTotalContrib.infoRecEv:

            if 'nrProtEntr' in dir(infoRecEv):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoRecEv.nrProtEntr',
                                                  infoRecEv.nrProtEntr.cdata,
                                                  1, u'None')

            if 'dhProcess' in dir(infoRecEv):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoRecEv.dhProcess',
                                                  infoRecEv.dhProcess.cdata,
                                                  1, u'None')

            if 'tpEv' in dir(infoRecEv):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoRecEv.tpEv',
                                                  infoRecEv.tpEv.cdata,
                                                  1, u'R-1000, R-1070, R-2010, R-2020, R-2030, R-2040, R-2050, R-2060, R-2098, R-2099, R-3010, R-4010, R-4020, R-4040, R-4098, R-4099, R-9000, R-9001, R-9002, R-9011, R-9012')

            if 'idEv' in dir(infoRecEv):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoRecEv.idEv',
                                                  infoRecEv.idEv.cdata,
                                                  1, u'None')

            if 'hash' in dir(infoRecEv):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoRecEv.hash',
                                                  infoRecEv.hash.cdata,
                                                  1, u'None')

    if 'infoTotalContrib' in dir(evtTotalContrib.infoTotalContrib):
        for infoTotalContrib in evtTotalContrib.infoTotalContrib:

            if 'nrRecArqBase' in dir(infoTotalContrib):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoTotalContrib.nrRecArqBase',
                                                  infoTotalContrib.nrRecArqBase.cdata,
                                                  0, u'None')

            if 'indExistInfo' in dir(infoTotalContrib):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoTotalContrib.indExistInfo',
                                                  infoTotalContrib.indExistInfo.cdata,
                                                  1, u'1, 2, 3')

            if 'RTom' in dir(infoTotalContrib.RTom):
                for RTom in infoTotalContrib.RTom:

                    if 'cnpjPrestador' in dir(RTom):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RTom.cnpjPrestador',
                                                          RTom.cnpjPrestador.cdata,
                                                          1, u'None')

                    if 'cno' in dir(RTom):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RTom.cno',
                                                          RTom.cno.cdata,
                                                          0, u'None')

                    if 'vlrTotalBaseRet' in dir(RTom):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RTom.vlrTotalBaseRet',
                                                          RTom.vlrTotalBaseRet.cdata,
                                                          1, u'None')

                    if 'infoCRTom' in dir(RTom.infoCRTom):
                        for infoCRTom in RTom.infoCRTom:
        
                            if 'CRTom' in dir(infoCRTom):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCRTom.CRTom',
                                                                  infoCRTom.CRTom.cdata,
                                                                  1, u'114106, 116201')
        
                            if 'vlrCRTom' in dir(infoCRTom):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCRTom.vlrCRTom',
                                                                  infoCRTom.vlrCRTom.cdata,
                                                                  0, u'None')
        
                            if 'vlrCRTomSusp' in dir(infoCRTom):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCRTom.vlrCRTomSusp',
                                                                  infoCRTom.vlrCRTomSusp.cdata,
                                                                  0, u'None')

            if 'RPrest' in dir(infoTotalContrib.RPrest):
                for RPrest in infoTotalContrib.RPrest:

                    if 'tpInscTomador' in dir(RPrest):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RPrest.tpInscTomador',
                                                          RPrest.tpInscTomador.cdata,
                                                          1, u'1, 4')

                    if 'nrInscTomador' in dir(RPrest):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RPrest.nrInscTomador',
                                                          RPrest.nrInscTomador.cdata,
                                                          1, u'None')

                    if 'vlrTotalBaseRet' in dir(RPrest):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RPrest.vlrTotalBaseRet',
                                                          RPrest.vlrTotalBaseRet.cdata,
                                                          1, u'None')

                    if 'vlrTotalRetPrinc' in dir(RPrest):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RPrest.vlrTotalRetPrinc',
                                                          RPrest.vlrTotalRetPrinc.cdata,
                                                          1, u'None')

                    if 'vlrTotalRetAdic' in dir(RPrest):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RPrest.vlrTotalRetAdic',
                                                          RPrest.vlrTotalRetAdic.cdata,
                                                          0, u'None')

                    if 'vlrTotalNRetPrinc' in dir(RPrest):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RPrest.vlrTotalNRetPrinc',
                                                          RPrest.vlrTotalNRetPrinc.cdata,
                                                          0, u'None')

                    if 'vlrTotalNRetAdic' in dir(RPrest):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RPrest.vlrTotalNRetAdic',
                                                          RPrest.vlrTotalNRetAdic.cdata,
                                                          0, u'None')

            if 'RRecRepAD' in dir(infoTotalContrib.RRecRepAD):
                for RRecRepAD in infoTotalContrib.RRecRepAD:

                    if 'CRRecRepAD' in dir(RRecRepAD):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RRecRepAD.CRRecRepAD',
                                                          RRecRepAD.CRRecRepAD.cdata,
                                                          1, u'115102')

                    if 'vlrCRRecRepAD' in dir(RRecRepAD):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RRecRepAD.vlrCRRecRepAD',
                                                          RRecRepAD.vlrCRRecRepAD.cdata,
                                                          1, u'None')

                    if 'vlrCRRecRepADSusp' in dir(RRecRepAD):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RRecRepAD.vlrCRRecRepADSusp',
                                                          RRecRepAD.vlrCRRecRepADSusp.cdata,
                                                          0, u'None')

            if 'RComl' in dir(infoTotalContrib.RComl):
                for RComl in infoTotalContrib.RComl:

                    if 'CRComl' in dir(RComl):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RComl.CRComl',
                                                          RComl.CRComl.cdata,
                                                          1, u'165701, 165702, 164605, 164606, 121302, 121304')

                    if 'vlrCRComl' in dir(RComl):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RComl.vlrCRComl',
                                                          RComl.vlrCRComl.cdata,
                                                          1, u'None')

                    if 'vlrCRComlSusp' in dir(RComl):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RComl.vlrCRComlSusp',
                                                          RComl.vlrCRComlSusp.cdata,
                                                          0, u'None')

            if 'RCPRB' in dir(infoTotalContrib.RCPRB):
                for RCPRB in infoTotalContrib.RCPRB:

                    if 'CRCPRB' in dir(RCPRB):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RCPRB.CRCPRB',
                                                          RCPRB.CRCPRB.cdata,
                                                          1, u'299101, 298501, 298504, 298506')

                    if 'vlrCRCPRB' in dir(RCPRB):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RCPRB.vlrCRCPRB',
                                                          RCPRB.vlrCRCPRB.cdata,
                                                          1, u'None')

                    if 'vlrCRCPRBSusp' in dir(RCPRB):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'RCPRB.vlrCRCPRBSusp',
                                                          RCPRB.vlrCRCPRBSusp.cdata,
                                                          0, u'None')
    return validacoes_lista