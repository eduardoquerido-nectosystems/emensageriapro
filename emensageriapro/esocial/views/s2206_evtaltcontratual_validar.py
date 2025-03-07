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


def validacoes_s2206_evtaltcontratual(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle

    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtAltContratual = doc.eSocial.evtAltContratual
    #variaveis

    if 'ideEvento' in dir(evtAltContratual.ideEvento):
        for ideEvento in evtAltContratual.ideEvento:

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

    if 'ideEmpregador' in dir(evtAltContratual.ideEmpregador):
        for ideEmpregador in evtAltContratual.ideEmpregador:

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

    if 'ideVinculo' in dir(evtAltContratual.ideVinculo):
        for ideVinculo in evtAltContratual.ideVinculo:

            if 'cpfTrab' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.cpfTrab',
                                                  ideVinculo.cpfTrab.cdata,
                                                  1, u'None')

            if 'nisTrab' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.nisTrab',
                                                  ideVinculo.nisTrab.cdata,
                                                  1, u'None')

            if 'matricula' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.matricula',
                                                  ideVinculo.matricula.cdata,
                                                  1, u'None')

    if 'altContratual' in dir(evtAltContratual.altContratual):
        for altContratual in evtAltContratual.altContratual:

            if 'dtAlteracao' in dir(altContratual):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'altContratual.dtAlteracao',
                                                  altContratual.dtAlteracao.cdata,
                                                  1, u'None')

            if 'dtEf' in dir(altContratual):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'altContratual.dtEf',
                                                  altContratual.dtEf.cdata,
                                                  0, u'None')

            if 'dscAlt' in dir(altContratual):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'altContratual.dscAlt',
                                                  altContratual.dscAlt.cdata,
                                                  0, u'None')

            if 'vinculo' in dir(altContratual.vinculo):
                for vinculo in altContratual.vinculo:

                    if 'tpRegPrev' in dir(vinculo):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'vinculo.tpRegPrev',
                                                          vinculo.tpRegPrev.cdata,
                                                          1, u'1, 2, 3')

            if 'infoRegimeTrab' in dir(altContratual.infoRegimeTrab):
                for infoRegimeTrab in altContratual.infoRegimeTrab:

                    if 'infoCeletista' in dir(infoRegimeTrab.infoCeletista):
                        for infoCeletista in infoRegimeTrab.infoCeletista:
        
                            if 'tpRegJor' in dir(infoCeletista):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCeletista.tpRegJor',
                                                                  infoCeletista.tpRegJor.cdata,
                                                                  1, u'1, 2, 3, 4')
        
                            if 'natAtividade' in dir(infoCeletista):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCeletista.natAtividade',
                                                                  infoCeletista.natAtividade.cdata,
                                                                  1, u'1, 2')
        
                            if 'dtBase' in dir(infoCeletista):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCeletista.dtBase',
                                                                  infoCeletista.dtBase.cdata,
                                                                  0, u'None')
        
                            if 'cnpjSindCategProf' in dir(infoCeletista):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoCeletista.cnpjSindCategProf',
                                                                  infoCeletista.cnpjSindCategProf.cdata,
                                                                  1, u'None')
        
                            if 'trabTemp' in dir(infoCeletista.trabTemp):
                                for trabTemp in infoCeletista.trabTemp:
                
                                    if 'justProrr' in dir(trabTemp):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'trabTemp.justProrr',
                                                                          trabTemp.justProrr.cdata,
                                                                          1, u'None')
        
                            if 'aprend' in dir(infoCeletista.aprend):
                                for aprend in infoCeletista.aprend:
                
                                    if 'tpInsc' in dir(aprend):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'aprend.tpInsc',
                                                                          aprend.tpInsc.cdata,
                                                                          1, u'1, 2, 3, 4, 5')
                
                                    if 'nrInsc' in dir(aprend):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'aprend.nrInsc',
                                                                          aprend.nrInsc.cdata,
                                                                          1, u'None')

                    if 'infoEstatutario' in dir(infoRegimeTrab.infoEstatutario):
                        for infoEstatutario in infoRegimeTrab.infoEstatutario:
        
                            if 'tpPlanRP' in dir(infoEstatutario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstatutario.tpPlanRP',
                                                                  infoEstatutario.tpPlanRP.cdata,
                                                                  1, u'1, 2')
        
                            if 'indTetoRGPS' in dir(infoEstatutario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstatutario.indTetoRGPS',
                                                                  infoEstatutario.indTetoRGPS.cdata,
                                                                  0, u'S, N')
        
                            if 'indAbonoPerm' in dir(infoEstatutario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstatutario.indAbonoPerm',
                                                                  infoEstatutario.indAbonoPerm.cdata,
                                                                  0, u'S, N')
        
                            if 'indParcRemun' in dir(infoEstatutario):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoEstatutario.indParcRemun',
                                                                  infoEstatutario.indParcRemun.cdata,
                                                                  0, u'S, N')

            if 'infoContrato' in dir(altContratual.infoContrato):
                for infoContrato in altContratual.infoContrato:

                    if 'codCargo' in dir(infoContrato):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoContrato.codCargo',
                                                          infoContrato.codCargo.cdata,
                                                          0, u'None')

                    if 'codFuncao' in dir(infoContrato):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoContrato.codFuncao',
                                                          infoContrato.codFuncao.cdata,
                                                          0, u'None')

                    if 'codCateg' in dir(infoContrato):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoContrato.codCateg',
                                                          infoContrato.codCateg.cdata,
                                                          1, u'101, 102, 103, 104, 105, 106, 111, 201, 202, 301, 302, 303, 305, 306, 307, 308, 309, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 751, 761, 771, 781, 901, 902, 903, 904, 905')

                    if 'codCarreira' in dir(infoContrato):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoContrato.codCarreira',
                                                          infoContrato.codCarreira.cdata,
                                                          0, u'None')

                    if 'dtIngrCarr' in dir(infoContrato):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoContrato.dtIngrCarr',
                                                          infoContrato.dtIngrCarr.cdata,
                                                          0, u'None')

                    if 'remuneracao' in dir(infoContrato.remuneracao):
                        for remuneracao in infoContrato.remuneracao:
        
                            if 'vrSalFx' in dir(remuneracao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'remuneracao.vrSalFx',
                                                                  remuneracao.vrSalFx.cdata,
                                                                  1, u'None')
        
                            if 'undSalFixo' in dir(remuneracao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'remuneracao.undSalFixo',
                                                                  remuneracao.undSalFixo.cdata,
                                                                  1, u'1, 2, 3, 4, 5, 6, 7')
        
                            if 'dscSalVar' in dir(remuneracao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'remuneracao.dscSalVar',
                                                                  remuneracao.dscSalVar.cdata,
                                                                  0, u'None')

                    if 'duracao' in dir(infoContrato.duracao):
                        for duracao in infoContrato.duracao:
        
                            if 'tpContr' in dir(duracao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'duracao.tpContr',
                                                                  duracao.tpContr.cdata,
                                                                  1, u'1, 2, 3')
        
                            if 'dtTerm' in dir(duracao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'duracao.dtTerm',
                                                                  duracao.dtTerm.cdata,
                                                                  0, u'None')
        
                            if 'objDet' in dir(duracao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'duracao.objDet',
                                                                  duracao.objDet.cdata,
                                                                  0, u'None')

                    if 'localTrabalho' in dir(infoContrato.localTrabalho):
                        for localTrabalho in infoContrato.localTrabalho:
        
                            if 'localTrabGeral' in dir(localTrabalho.localTrabGeral):
                                for localTrabGeral in localTrabalho.localTrabGeral:
                
                                    if 'tpInsc' in dir(localTrabGeral):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabGeral.tpInsc',
                                                                          localTrabGeral.tpInsc.cdata,
                                                                          1, u'1, 2, 3, 4, 5')
                
                                    if 'nrInsc' in dir(localTrabGeral):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabGeral.nrInsc',
                                                                          localTrabGeral.nrInsc.cdata,
                                                                          1, u'None')
                
                                    if 'descComp' in dir(localTrabGeral):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabGeral.descComp',
                                                                          localTrabGeral.descComp.cdata,
                                                                          0, u'None')
        
                            if 'localTrabDom' in dir(localTrabalho.localTrabDom):
                                for localTrabDom in localTrabalho.localTrabDom:
                
                                    if 'tpLograd' in dir(localTrabDom):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabDom.tpLograd',
                                                                          localTrabDom.tpLograd.cdata,
                                                                          0, u'A, AC, ACA, ACL, AD, AE, AER, AL, AMD, AME, AN, ANT, ART, AT, ATL, A V, AV, AVC, AVM, AVV, BAL, BC, BCO, BEL, BL, BLO, BLS, BLV, BSQ, BVD, BX, C, CAL, CAM, CAN, CH, CHA, CIC, CIR, CJ, CJM, CMP, COL, COM, CON, COND, COR, CPO, CRG, CTN, DSC, DSV, DT, EB, EIM, ENS, ENT, EQ, ESC, ESD, ESE, ESI, ESL, ESM, ESP, ESS, EST, ESV, ETA, ETC, ETD, ETN, ETP, ETT, EVA, EVD, EX, FAV, FAZ, FER, FNT, FRA, FTE, GAL, GJA, HAB, IA, IND, IOA, JD, JDE, LD, LGA, LGO, LOT, LRG, LT, MER, MNA, MOD, MRG, MRO, MTE, NUC, NUR, O, OUT, PAR, PAS, PAT, PC, PCE, PDA, PDO, PNT, PR, PRL, PRM, PRQ, PRR, PSA, PSG, PSP, PSS, PTE, PTO, Q, QTA, QTS, R, R I, R L, R P, R V, RAM, RCR, REC, RER, RES, RET, RLA, RMP, ROA, ROD, ROT, RPE, RPR, RTN, RTT, SEG, SIT, SRV, ST, SUB, TCH, TER, TR, TRV, TUN, TV, TVP, TVV, UNI, V, V C, V L, VAC, VAL, VCO, VD, V-E, VER, VEV, VL, VLA, VLE, VLT, VPE, VRT, ZIG')
                
                                    if 'dscLograd' in dir(localTrabDom):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabDom.dscLograd',
                                                                          localTrabDom.dscLograd.cdata,
                                                                          1, u'None')
                
                                    if 'nrLograd' in dir(localTrabDom):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabDom.nrLograd',
                                                                          localTrabDom.nrLograd.cdata,
                                                                          1, u'None')
                
                                    if 'complemento' in dir(localTrabDom):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabDom.complemento',
                                                                          localTrabDom.complemento.cdata,
                                                                          0, u'None')
                
                                    if 'bairro' in dir(localTrabDom):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabDom.bairro',
                                                                          localTrabDom.bairro.cdata,
                                                                          0, u'None')
                
                                    if 'cep' in dir(localTrabDom):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabDom.cep',
                                                                          localTrabDom.cep.cdata,
                                                                          1, u'None')
                
                                    if 'codMunic' in dir(localTrabDom):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabDom.codMunic',
                                                                          localTrabDom.codMunic.cdata,
                                                                          1, u'5300108, 1400050, 1400027, 1400100, 1400159, 1400175, 1400209, 1400233, 1400282, 1400308, 1400407, 1400456, 1400472, 1400506, 1400605, 1400704, 1600105, 1600204, 1600212, 1600238, 1600253, 1600279, 1600303, 1600402, 1600501, 1600154, 1600535, 1600550, 1600600, 1600055, 1600709, 1600808, 1200013, 1200054, 1200104, 1200138, 1200179, 1200203, 1200252, 1200302, 1200328, 1200336, 1200344, 1200351, 1200385, 1200807, 1200393, 1200401, 1200427, 1200435, 1200500, 1200450, 1200609, 1200708, 1100015, 1100379, 1100403, 1100346, 1100023, 1100452, 1100031, 1100601, 1100049, 1100700, 1100809, 1100908, 1100056, 1100924, 1100064, 1100072, 1100080, 1100940, 1100098, 1101005, 1100106, 1101104, 1100114, 1100122, 1100130, 1101203, 1101302, 1101401, 1100148, 1100338, 1101435, 1100502, 1100155, 1101450, 1100189, 1101468, 1100205, 1100254, 1101476, 1100262, 1100288, 1100296, 1101484, 1101492, 1100320, 1101500, 1101559, 1101609, 1101708, 1101757, 1101807, 1100304, 1300029, 1300060, 1300086, 1300102, 1300144, 1300201, 1300300, 1300409, 1300508, 1300607, 1300631, 1300680, 1300706, 1300805, 1300839, 1300904, 1301001, 1301100, 1301159, 1301209, 1301308, 1301407, 1301506, 1301605, 1301654, 1301704, 1301803, 1301852, 1301902, 1301951, 1302009, 1302108, 1302207, 1302306, 1302405, 1302504, 1302553, 1302603, 1302702, 1302801, 1302900, 1303007, 1303106, 1303205, 1303304, 1303403, 1303502, 1303536, 1303569, 1303601, 1303700, 1303809, 1303908, 1303957, 1304005, 1304062, 1304104, 1304203, 1304237, 1304260, 1304302, 1304401, 2800100, 2800209, 2800308, 2800407, 2800506, 2800605, 2800670, 2800704, 2801009, 2801108, 2801207, 2801306, 2801405, 2801504, 2801603, 2801702, 2801900, 2802007, 2802106, 2802205, 2802304, 2802403, 2802502, 2802601, 2802700, 2802809, 2802908, 2803005, 2803104, 2803203, 2803302, 2803401, 2803500, 2803609, 2803708, 2803807, 2803906, 2804003, 2804102, 2804201, 2804300, 2804409, 2804458, 2804508, 2804607, 2804706, 2804805, 2804904, 2805000, 2805109, 2805208, 2805307, 2805406, 2805505, 2805604, 2805703, 2805802, 2805901, 2806008, 2806107, 2806206, 2806305, 2806503, 2806404, 2806602, 2806701, 2806800, 2806909, 2807006, 2807105, 2807204, 2807303, 2807402, 2807501, 2807600, 3200102, 3200169, 3200136, 3200201, 3200300, 3200359, 3200409, 3200508, 3200607, 3200706, 3200805, 3200904, 3201001, 3201100, 3201159, 3201209, 3201308, 3201407, 3201506, 3201605, 3201704, 3201803, 3201902, 3202009, 3202108, 3202207, 3202256, 3202306, 3202405, 3202454, 3202504, 3202553, 3202603, 3202652, 3202702, 3202801, 3202900, 3203007, 3203056, 3203106, 3203130, 3203163, 3203205, 3203304, 3203320, 3203346, 3203353, 3203403, 3203502, 3203601, 3203700, 3203809, 3203908, 3204005, 3204054, 3204104, 3204203, 3204252, 3204302, 3204351, 3204401, 3204500, 3204559, 3204609, 3204658, 3204708, 3204807, 3204906, 3204955, 3205002, 3205010, 3205036, 3205069, 3205101, 3205150, 3205176, 3205200, 3205309, 5000203, 5000252, 5000609, 5000708, 5000807, 5000856, 5000906, 5001003, 5001102, 5001243, 5001508, 5001904, 5002001, 5002100, 5002159, 5002209, 5002308, 5002407, 5002605, 5002704, 5002803, 5002902, 5002951, 5003108, 5003157, 5003207, 5003256, 5003306, 5003454, 5003488, 5003504, 5003702, 5003751, 5003801, 5003900, 5004007, 5004106, 5004304, 5004403, 5004502, 5004601, 5004700, 5004809, 5004908, 5005004, 5005103, 5005152, 5005202, 5005251, 5005400, 5005608, 5005681, 5005707, 5005806, 5006002, 5006200, 5006259, 5006309, 5006358, 5006408, 5006606, 5006903, 5007109, 5007208, 5007307, 5007406, 5007505, 5007554, 5007695, 5007802, 5007703, 5007901, 5007935, 5007950, 5007976, 5008008, 5008305, 5008404, 3300100, 3300159, 3300209, 3300225, 3300233, 3300258, 3300308, 3300407, 3300456, 3300506, 3300605, 3300704, 3300803, 3300902, 3301009, 3301108, 3300936, 3301157, 3301207, 3301306, 3300951, 3301405, 3301504, 3301603, 3301702, 3301801, 3301850, 3301876, 3301900, 3302007, 3302056, 3302106, 3302205, 3302254, 3302270, 3302304, 3302403, 3302452, 3302502, 3302601, 3302700, 3302809, 3302858, 3302908, 3303005, 3303104, 3303203, 3303302, 3303401, 3303500, 3303609, 3303708, 3303807, 3303856, 3303906, 3303955, 3304003, 3304102, 3304110, 3304128, 3304144, 3304151, 3304201, 3304300, 3304409, 3304508, 3304524, 3304557, 3304607, 3304706, 3304805, 3304755, 3304904, 3305000, 3305109, 3305133, 3305158, 3305208, 3305307, 3305406, 3305505, 3305554, 3305604, 3305703, 3305752, 3305802, 3305901, 3306008, 3306107, 3306156, 3306206, 3306305, 2700102, 2700201, 2700300, 2700409, 2700508, 2700607, 2700706, 2700805, 2700904, 2701001, 2701100, 2701209, 2701308, 2701357, 2701407, 2701506, 2701605, 2701704, 2701803, 2701902, 2702009, 2702108, 2702207, 2702306, 2702355, 2702405, 2702504, 2702553, 2702603, 2702702, 2702801, 2702900, 2703007, 2703106, 2703205, 2703304, 2703403, 2703502, 2703601, 2703700, 2703759, 2703809, 2703908, 2704005, 2704104, 2704203, 2704302, 2704401, 2704906, 2704500, 2704609, 2704708, 2704807, 2705002, 2705101, 2705200, 2705309, 2705408, 2705507, 2705606, 2705705, 2705804, 2705903, 2706000, 2706109, 2706208, 2706307, 2706406, 2706422, 2706448, 2706505, 2706604, 2706703, 2706802, 2706901, 2707008, 2707107, 2707206, 2707305, 2707404, 2707503, 2707602, 2707701, 2707800, 2707909, 2708006, 2708105, 2708204, 2708303, 2708402, 2708501, 2708600, 2708709, 2708808, 2708907, 2708956, 2709004, 2709103, 2709152, 2709202, 2709301, 2709400, 1700251, 1700301, 1700350, 1700400, 1700707, 1701002, 1701051, 1701101, 1701309, 1701903, 1702000, 1702109, 1702158, 1702208, 1702307, 1702406, 1702554, 1702703, 1702901, 1703008, 1703057, 1703073, 1703107, 1703206, 1703305, 1703602, 1703701, 1703800, 1703826, 1703842, 1703867, 1703883, 1703891, 1703909, 1704105, 1705102, 1704600, 1705508, 1716703, 1705557, 1705607, 1706001, 1706100, 1706258, 1706506, 1707009, 1707108, 1707207, 1707306, 1707405, 1707553, 1707652, 1707702, 1708205, 1708254, 1708304, 1709005, 1709302, 1709500, 1709807, 1710508, 1710706, 1710904, 1711100, 1711506, 1711803, 1711902, 1711951, 1712009, 1712157, 1712405, 1712454, 1712504, 1712702, 1712801, 1713205, 1713304, 1713601, 1713700, 1713957, 1714203, 1714302, 1714880, 1715002, 1715101, 1715150, 1715259, 1715507, 1721000, 1715705, 1713809, 1715754, 1716109, 1716208, 1716307, 1716505, 1716604, 1716653, 1717008, 1717206, 1717503, 1717800, 1717909, 1718006, 1718204, 1718303, 1718402, 1718451, 1718501, 1718550, 1718659, 1718709, 1718758, 1718808, 1718840, 1718865, 1718881, 1718899, 1718907, 1719004, 1720002, 1720101, 1720150, 1720200, 1720259, 1720309, 1720499, 1720655, 1720804, 1720853, 1720903, 1720937, 1720978, 1721109, 1721208, 1721257, 1721307, 1722081, 1722107, 5100102, 5100201, 5100250, 5100300, 5100359, 5100409, 5100508, 5100607, 5100805, 5101001, 5101209, 5101258, 5101308, 5101407, 5101605, 5101704, 5101803, 5101852, 5101902, 5102504, 5102603, 5102637, 5102678, 5102686, 5102694, 5102702, 5102793, 5102850, 5103007, 5103056, 5103106, 5103205, 5103254, 5103304, 5103353, 5103361, 5103379, 5103403, 5103437, 5103452, 5103502, 5103601, 5103700, 5103809, 5103858, 5103908, 5103957, 5104104, 5104203, 5104500, 5104526, 5104542, 5104559, 5104609, 5104807, 5104906, 5105002, 5105101, 5105150, 5105176, 5105200, 5105234, 5105259, 5105309, 5105580, 5105606, 5105622, 5105903, 5106000, 5106109, 5106158, 5106208, 5106216, 5108808, 5106182, 5108857, 5108907, 5108956, 5106224, 5106174, 5106232, 5106190, 5106240, 5106257, 5106273, 5106265, 5106315, 5106281, 5106299, 5106307, 5106372, 5106422, 5106455, 5106505, 5106653, 5106703, 5106752, 5106778, 5106802, 5106828, 5106851, 5107008, 5107040, 5107065, 5107156, 5107180, 5107198, 5107206, 5107578, 5107602, 5107701, 5107750, 5107248, 5107743, 5107768, 5107776, 5107263, 5107792, 5107800, 5107859, 5107297, 5107305, 5107354, 5107107, 5107404, 5107875, 5107883, 5107909, 5107925, 5107941, 5107958, 5108006, 5108055, 5108105, 5108204, 5108303, 5108352, 5108402, 5108501, 5105507, 5108600, 1500107, 1500131, 1500206, 1500305, 1500347, 1500404, 1500503, 1500602, 1500701, 1500800, 1500859, 1500909, 1500958, 1501006, 1501105, 1501204, 1501253, 1501303, 1501402, 1501451, 1501501, 1501576, 1501600, 1501709, 1501725, 1501758, 1501782, 1501808, 1501907, 1502004, 1501956, 1502103, 1502152, 1502202, 1502301, 1502400, 1502509, 1502608, 1502707, 1502756, 1502764, 1502772, 1502806, 1502855, 1502905, 1502939, 1502954, 1503002, 1503044, 1503077, 1503093, 1503101, 1503200, 1503309, 1503408, 1503457, 1503507, 1503606, 1503705, 1503754, 1503804, 1503903, 1504000, 1504059, 1504109, 1504208, 1504307, 1504406, 1504422, 1504455, 1504505, 1504604, 1504703, 1504752, 1504802, 1504901, 1504950, 1504976, 1505007, 1505031, 1505064, 1505106, 1505205, 1505304, 1505403, 1505437, 1505486, 1505494, 1505502, 1505536, 1505551, 1505601, 1505635, 1505650, 1505700, 1505809, 1505908, 1506005, 1506104, 1506112, 1506138, 1506161, 1506187, 1506195, 1506203, 1506302, 1506351, 1506401, 1506500, 1506559, 1506583, 1506609, 1506708, 1506807, 1506906, 1507003, 1507102, 1507151, 1507201, 1507300, 1507409, 1507458, 1507466, 1507474, 1507508, 1507607, 1507706, 1507755, 1507805, 1507904, 1507953, 1507961, 1507979, 1508001, 1508035, 1508050, 1508084, 1508100, 1508126, 1508159, 1508209, 1508308, 1508357, 1508407, 2400109, 2400208, 2400307, 2400406, 2400505, 2400604, 2400703, 2400802, 2400901, 2401008, 2401107, 2401206, 2401305, 2401404, 2401453, 2401503, 2401602, 2401651, 2401701, 2401800, 2401859, 2401909, 2402006, 2402105, 2402204, 2402303, 2402402, 2402501, 2402600, 2402709, 2402808, 2402907, 2403004, 2403103, 2403202, 2403301, 2403400, 2403509, 2403608, 2403707, 2403756, 2403806, 2403905, 2404002, 2404101, 2404200, 2404309, 2404408, 2404507, 2404606, 2404705, 2404804, 2404853, 2404903, 2405009, 2405108, 2405207, 2405306, 2405405, 2405504, 2405603, 2405702, 2405801, 2405900, 2406007, 2406106, 2406155, 2406205, 2406304, 2406403, 2406502, 2406601, 2406700, 2406809, 2406908, 2407005, 2407104, 2407203, 2407252, 2407302, 2407401, 2407500, 2407609, 2407708, 2407807, 2407906, 2408003, 2408102, 2408201, 2408300, 2408409, 2408508, 2408607, 2408706, 2408805, 2408904, 2403251, 2409100, 2409209, 2409308, 2409407, 2409506, 2409605, 2409704, 2409803, 2409902, 2410009, 2410108, 2410207, 2410256, 2410306, 2410405, 2410504, 2410603, 2410702, 2410801, 2410900, 2408953, 2411007, 2411106, 2411205, 2409332, 2411403, 2411429, 2411502, 2411601, 2411700, 2411809, 2411908, 2412005, 2412104, 2412203, 2412302, 2412401, 2412500, 2412559, 2412609, 2412708, 2412807, 2412906, 2413003, 2413102, 2413201, 2413300, 2413359, 2413409, 2413508, 2413557, 2413607, 2413706, 2413805, 2413904, 2414001, 2414100, 2414159, 2411056, 2414209, 2414308, 2414407, 2414456, 2414506, 2414605, 2414704, 2414753, 2414803, 2414902, 2415008, 2300101, 2300150, 2300200, 2300309, 2300408, 2300507, 2300606, 2300705, 2300754, 2300804, 2300903, 2301000, 2301109, 2301208, 2301257, 2301307, 2301406, 2301505, 2301604, 2301703, 2301802, 2301851, 2301901, 2301950, 2302008, 2302057, 2302107, 2302206, 2302305, 2302404, 2302503, 2302602, 2302701, 2302800, 2302909, 2303006, 2303105, 2303204, 2303303, 2303402, 2303501, 2303600, 2303659, 2303709, 2303808, 2303907, 2303931, 2303956, 2304004, 2304103, 2304202, 2304236, 2304251, 2304269, 2304277, 2304285, 2304301, 2304350, 2304400, 2304459, 2304509, 2304608, 2304657, 2304707, 2304806, 2304905, 2304954, 2305001, 2305100, 2305209, 2305233, 2305266, 2305308, 2305332, 2305357, 2305407, 2305506, 2305605, 2305654, 2305704, 2305803, 2305902, 2306009, 2306108, 2306207, 2306256, 2306306, 2306405, 2306504, 2306553, 2306603, 2306702, 2306801, 2306900, 2307007, 2307106, 2307205, 2307254, 2307304, 2307403, 2307502, 2307601, 2307635, 2307650, 2307700, 2307809, 2307908, 2308005, 2308104, 2308203, 2308302, 2308351, 2308377, 2308401, 2308500, 2308609, 2308708, 2308807, 2308906, 2309003, 2309102, 2309201, 2309300, 2309409, 2309458, 2309508, 2309607, 2309706, 2309805, 2309904, 2310001, 2310100, 2310209, 2310258, 2310308, 2310407, 2310506, 2310605, 2310704, 2310803, 2310852, 2310902, 2310951, 2311009, 2311108, 2311207, 2311231, 2311264, 2311306, 2311355, 2311405, 2311504, 2311603, 2311702, 2311801, 2311900, 2311959, 2312205, 2312007, 2312106, 2312304, 2312403, 2312502, 2312601, 2312700, 2312809, 2312908, 2313005, 2313104, 2313203, 2313252, 2313302, 2313351, 2313401, 2313500, 2313559, 2313609, 2313708, 2313757, 2313807, 2313906, 2313955, 2314003, 2314102, 2600054, 2600104, 2600203, 2600302, 2600401, 2600500, 2600609, 2600708, 2600807, 2600906, 2601003, 2601052, 2601102, 2601201, 2601300, 2601409, 2601508, 2601607, 2601706, 2601805, 2601904, 2602001, 2602100, 2602209, 2602308, 2602407, 2602506, 2602605, 2602704, 2602803, 2602902, 2603009, 2603108, 2603207, 2603306, 2603405, 2603454, 2603504, 2603603, 2603702, 2603801, 2603900, 2603926, 2604007, 2604106, 2604155, 2604205, 2604304, 2604403, 2604502, 2604601, 2604700, 2604809, 2604908, 2605004, 2605103, 2605152, 2605202, 2605301, 2605400, 2605459, 2605509, 2605608, 2605707, 2605806, 2605905, 2606002, 2606101, 2606200, 2606309, 2606408, 2606507, 2606606, 2606705, 2606804, 2606903, 2607604, 2607000, 2607109, 2607208, 2607307, 2607406, 2607505, 2607653, 2607703, 2607752, 2607802, 2607901, 2607950, 2608008, 2608057, 2608107, 2608206, 2608255, 2608305, 2608404, 2608453, 2608503, 2608602, 2608701, 2608750, 2608800, 2608909, 2609006, 2609105, 2609154, 2609204, 2609303, 2614303, 2609402, 2609501, 2609600, 2609709, 2609808, 2609907, 2610004, 2610103, 2610202, 2610301, 2610400, 2610509, 2610608, 2610707, 2610806, 2610905, 2611002, 2611101, 2611200, 2611309, 2611408, 2611507, 2611533, 2611606, 2611705, 2611804, 2611903, 2612000, 2612109, 2612208, 2612307, 2612406, 2612455, 2612471, 2612505, 2612554, 2612604, 2612703, 2612802, 2612901, 2613008, 2613107, 2613206, 2613305, 2613404, 2613503, 2613602, 2613701, 2613800, 2613909, 2614006, 2614105, 2614204, 2614402, 2614501, 2614600, 2614709, 2614808, 2614857, 2615003, 2615102, 2615201, 2615300, 2615409, 2615508, 2615607, 2615706, 2615805, 2615904, 2616001, 2616100, 2616183, 2616209, 2616308, 2616407, 2616506, 2100055, 2100105, 2100154, 2100204, 2100303, 2100402, 2100436, 2100477, 2100501, 2100550, 2100600, 2100709, 2100808, 2100832, 2100873, 2100907, 2100956, 2101004, 2101103, 2101202, 2101251, 2101301, 2101350, 2101400, 2101509, 2101608, 2101707, 2101772, 2101731, 2101806, 2101905, 2101939, 2101970, 2102002, 2102036, 2102077, 2102101, 2102150, 2102200, 2102309, 2102325, 2102358, 2102374, 2102408, 2102507, 2102556, 2102606, 2102705, 2102754, 2102804, 2102903, 2103000, 2103109, 2103125, 2103158, 2103174, 2103208, 2103257, 2103307, 2103406, 2103505, 2103554, 2103604, 2103703, 2103752, 2103802, 2103901, 2104008, 2104057, 2104073, 2104081, 2104099, 2104107, 2104206, 2104305, 2104404, 2104503, 2104552, 2104602, 2104628, 2104651, 2104677, 2104701, 2104800, 2104909, 2105005, 2105104, 2105153, 2105203, 2105302, 2105351, 2105401, 2105427, 2105450, 2105476, 2105500, 2105609, 2105658, 2105708, 2105807, 2105948, 2105906, 2105922, 2105963, 2105989, 2106003, 2106102, 2106201, 2106300, 2106326, 2106359, 2106375, 2106409, 2106508, 2106607, 2106631, 2106672, 2106706, 2106755, 2106805, 2106904, 2107001, 2107100, 2107209, 2107258, 2107308, 2107357, 2107407, 2107456, 2107506, 2107605, 2107704, 2107803, 2107902, 2108009, 2108058, 2108108, 2108207, 2108256, 2108306, 2108405, 2108454, 2108504, 2108603, 2108702, 2108801, 2108900, 2109007, 2109056, 2109106, 2109205, 2109239, 2109270, 2109304, 2109403, 2109452, 2109502, 2109551, 2109601, 2109700, 2109759, 2109809, 2109908, 2110005, 2110039, 2110104, 2110203, 2110237, 2110278, 2110302, 2110401, 2110500, 2110609, 2110658, 2110708, 2110807, 2110856, 2110906, 2111003, 2111029, 2111052, 2111078, 2111102, 2111201, 2111250, 2111300, 2111409, 2111508, 2111532, 2111573, 2111607, 2111631, 2111672, 2111706, 2111722, 2111748, 2111763, 2111789, 2111805, 2111904, 2111953, 2112001, 2112100, 2112209, 2112233, 2112274, 2112308, 2112407, 2112456, 2112506, 2112605, 2112704, 2112803, 2112852, 2112902, 2113009, 2114007, 2200053, 2200103, 2200202, 2200251, 2200277, 2200301, 2200400, 2200459, 2200509, 2200608, 2200707, 2200806, 2200905, 2200954, 2201002, 2201051, 2201101, 2201150, 2201176, 2201200, 2201309, 2201408, 2201507, 2201556, 2201572, 2201606, 2201705, 2201739, 2201770, 2201804, 2201903, 2201919, 2201929, 2201945, 2201960, 2201988, 2202000, 2202026, 2202059, 2202075, 2202083, 2202091, 2202109, 2202117, 2202133, 2202174, 2202208, 2202251, 2202307, 2202406, 2202455, 2202505, 2202539, 2202554, 2202604, 2202653, 2202703, 2202711, 2202729, 2202737, 2202752, 2202778, 2202802, 2202851, 2202901, 2203008, 2203107, 2203206, 2203230, 2203271, 2203255, 2203305, 2203354, 2203404, 2203453, 2203420, 2203503, 2203602, 2203701, 2203750, 2203800, 2203859, 2203909, 2204006, 2204105, 2204154, 2204204, 2204303, 2204352, 2204402, 2204501, 2204550, 2204600, 2204659, 2204709, 2204808, 2204907, 2205003, 2205102, 2205151, 2205201, 2205250, 2205276, 2205300, 2205359, 2205409, 2205458, 2205508, 2205516, 2205524, 2205532, 2205557, 2205573, 2205565, 2205581, 2205599, 2205540, 2205607, 2205706, 2205805, 2205854, 2205904, 2205953, 2206001, 2206050, 2206100, 2206209, 2206308, 2206357, 2206407, 2206506, 2206605, 2206654, 2206670, 2206696, 2206704, 2206753, 2206803, 2207959, 2206902, 2206951, 2207009, 2207108, 2207207, 2207306, 2207355, 2207405, 2207504, 2207553, 2207603, 2207702, 2207751, 2207777, 2207793, 2207801, 2207850, 2207900, 2207934, 2208007, 2208106, 2208205, 2208304, 2208403, 2208502, 2208551, 2208601, 2208650, 2208700, 2208809, 2208858, 2208874, 2208908, 2209005, 2209104, 2209153, 2209203, 2209302, 2209377, 2209351, 2209401, 2209450, 2209500, 2209559, 2209609, 2209658, 2209708, 2209757, 2209807, 2209856, 2209872, 2209906, 2209955, 2209971, 2210003, 2210052, 2210102, 2210201, 2210300, 2210359, 2210375, 2210383, 2210391, 2210409, 2210508, 2210607, 2210623, 2210631, 2210656, 2210706, 2210805, 2210904, 2210938, 2210953, 2210979, 2211001, 2211100, 2211209, 2211308, 2211357, 2211407, 2211506, 2211605, 2211704, 2500106, 2500205, 2500304, 2500403, 2500502, 2500536, 2500577, 2500601, 2500734, 2500775, 2500809, 2500908, 2501005, 2501104, 2501153, 2501203, 2501302, 2501351, 2501401, 2501500, 2501534, 2501609, 2501575, 2501708, 2501807, 2501906, 2502003, 2502052, 2502102, 2502151, 2502201, 2502300, 2502409, 2502508, 2502706, 2502805, 2502904, 2503001, 2503100, 2503209, 2503308, 2503407, 2503506, 2503555, 2503605, 2503704, 2503753, 2503803, 2503902, 2504009, 2516409, 2504033, 2504074, 2504108, 2504157, 2504207, 2504306, 2504355, 2504405, 2504504, 2504603, 2504702, 2504801, 2504850, 2504900, 2505006, 2505105, 2505238, 2505204, 2505279, 2505303, 2505352, 2505402, 2505600, 2505709, 2505808, 2505907, 2506004, 2506103, 2506202, 2506251, 2506301, 2506400, 2506509, 2506608, 2502607, 2506707, 2506806, 2506905, 2507002, 2507101, 2507200, 2507309, 2507408, 2507507, 2507606, 2507705, 2507804, 2507903, 2508000, 2508109, 2508208, 2508307, 2508406, 2508505, 2508554, 2508604, 2508703, 2508802, 2508901, 2509008, 2509057, 2509107, 2509156, 2509206, 2509305, 2509339, 2509370, 2509396, 2509404, 2509503, 2509602, 2509701, 2509800, 2509909, 2510006, 2510105, 2510204, 2510303, 2510402, 2510501, 2510600, 2510659, 2510709, 2510808, 2510907, 2511004, 2511103, 2511202, 2512721, 2511301, 2511400, 2511509, 2511608, 2511707, 2511806, 2511905, 2512002, 2512036, 2512077, 2512101, 2512200, 2512309, 2512408, 2512507, 2512606, 2512705, 2512747, 2512754, 2512762, 2512788, 2512804, 2512903, 2513000, 2513109, 2513158, 2513208, 2513307, 2513356, 2513406, 2513703, 2513802, 2513505, 2513604, 2513653, 2513851, 2513927, 2513901, 2513968, 2513943, 2513984, 2514008, 2500700, 2514107, 2514206, 2514305, 2514404, 2514503, 2514552, 2514602, 2514651, 2514701, 2514800, 2514453, 2514909, 2515005, 2515104, 2515203, 2515302, 2515401, 2515500, 2515609, 2515708, 2515807, 2515906, 2515930, 2515971, 2516003, 2516102, 2516151, 2516201, 2516300, 2516508, 2516607, 2516706, 2516755, 2516805, 2516904, 2517001, 2517100, 2517209, 2505501, 2517407, 5200050, 5200100, 5200134, 5200159, 5200175, 5200209, 5200258, 5200308, 5200506, 5200555, 5200605, 5200803, 5200829, 5200852, 5200902, 5201108, 5201207, 5201306, 5201405, 5201454, 5201504, 5201603, 5201702, 5201801, 5202155, 5202353, 5202502, 5202601, 5202809, 5203104, 5203203, 5203302, 5203401, 5203500, 5203559, 5203575, 5203609, 5203807, 5203906, 5203939, 5203962, 5204003, 5204102, 5204201, 5204250, 5204300, 5204409, 5204508, 5204557, 5204607, 5204656, 5204706, 5204805, 5204854, 5204904, 5204953, 5205000, 5205059, 5205109, 5205208, 5205307, 5205406, 5205455, 5205471, 5205497, 5205513, 5205521, 5205703, 5205802, 5205901, 5206206, 5206305, 5206404, 5206503, 5206602, 5206701, 5206800, 5206909, 5207105, 5208301, 5207253, 5207352, 5207402, 5207501, 5207535, 5207600, 5207808, 5207907, 5208004, 5208103, 5208152, 5208400, 5208509, 5208608, 5208707, 5208806, 5208905, 5209101, 5209150, 5209200, 5209291, 5209408, 5209457, 5209606, 5209705, 5209804, 5209903, 5209937, 5209952, 5210000, 5210109, 5210158, 5210208, 5210307, 5210406, 5210562, 5210604, 5210802, 5210901, 5211008, 5211206, 5211305, 5211404, 5211503, 5211602, 5211701, 5211800, 5211909, 5212006, 5212055, 5212105, 5212204, 5212253, 5212303, 5212501, 5212600, 5212709, 5212808, 5212907, 5212956, 5213004, 5213053, 5213087, 5213103, 5213400, 5213509, 5213707, 5213756, 5213772, 5213806, 5213855, 5213905, 5214002, 5214051, 5214101, 5214408, 5214507, 5214606, 5214705, 5214804, 5214838, 5214861, 5214879, 5214903, 5215009, 5215207, 5215231, 5215256, 5215306, 5215405, 5215504, 5215603, 5215652, 5215702, 5215801, 5215900, 5216007, 5216304, 5216403, 5216452, 5216809, 5216908, 5217104, 5217203, 5217302, 5217401, 5217609, 5217708, 5218003, 5218052, 5218102, 5218300, 5218391, 5218508, 5218607, 5218706, 5218789, 5218805, 5218904, 5219001, 5219100, 5219209, 5219258, 5219308, 5219357, 5219407, 5219456, 5219506, 5219605, 5219704, 5219712, 5219738, 5219753, 5219803, 5219902, 5220058, 5220009, 5220108, 5220157, 5220207, 5220264, 5220280, 5220405, 5220454, 5220504, 5220603, 5220686, 5220702, 5221007, 5221080, 5221197, 5221304, 5221403, 5221452, 5221502, 5221551, 5221577, 5221601, 5221700, 5221809, 5221858, 5221908, 5222005, 5222054, 5222203, 5222302, 4200051, 4200101, 4200200, 4200309, 4200408, 4200507, 4200556, 4200606, 4200705, 4200754, 4200804, 4200903, 4201000, 4201109, 4201208, 4201257, 4201273, 4201307, 4201406, 4201505, 4201604, 4201653, 4201703, 4201802, 4201901, 4201950, 4202057, 4202008, 4202073, 4212809, 4202081, 4202099, 4202107, 4202131, 4202156, 4202206, 4202305, 4202404, 4202438, 4202503, 4202537, 4202578, 4202602, 4202453, 4202701, 4202800, 4202859, 4202875, 4202909, 4203006, 4203105, 4203154, 4203204, 4203303, 4203402, 4203501, 4203600, 4203709, 4203808, 4203253, 4203907, 4203956, 4204004, 4204103, 4204152, 4204178, 4204194, 4204202, 4204251, 4204301, 4204350, 4204400, 4204459, 4204558, 4204509, 4204608, 4204707, 4204756, 4204806, 4204905, 4205001, 4205100, 4205159, 4205175, 4205191, 4205209, 4205308, 4205357, 4205407, 4205431, 4205456, 4205506, 4205555, 4205605, 4205704, 4205803, 4205902, 4206009, 4206108, 4206207, 4206306, 4206405, 4206504, 4206603, 4206652, 4206702, 4206751, 4206801, 4206900, 4207007, 4207106, 4207205, 4207304, 4207403, 4207502, 4207577, 4207601, 4207650, 4207684, 4207700, 4207759, 4207809, 4207858, 4207908, 4208005, 4208104, 4208203, 4208302, 4208401, 4208450, 4208500, 4208609, 4208708, 4208807, 4208906, 4208955, 4209003, 4209102, 4209151, 4209177, 4209201, 4209300, 4209409, 4209458, 4209508, 4209607, 4209706, 4209805, 4209854, 4209904, 4210001, 4210035, 4210050, 4210100, 4210209, 4210308, 4210407, 4210506, 4210555, 4210605, 4210704, 4210803, 4210852, 4210902, 4211009, 4211058, 4211108, 4211207, 4211256, 4211306, 4211405, 4211454, 4211504, 4211603, 4211652, 4211702, 4211751, 4211801, 4211850, 4211876, 4211892, 4211900, 4212007, 4212056, 4212106, 4212205, 4212239, 4212254, 4212270, 4212304, 4212403, 4212502, 4212601, 4212700, 4212908, 4213005, 4213104, 4213153, 4213203, 4213302, 4213351, 4213401, 4213500, 4213609, 4213708, 4213807, 4213906, 4214003, 4214102, 4214151, 4214201, 4214300, 4214409, 4214508, 4214607, 4214805, 4214706, 4214904, 4215000, 4215059, 4215075, 4215109, 4215208, 4215307, 4215356, 4215406, 4215455, 4215505, 4215554, 4215604, 4215653, 4215679, 4215687, 4215695, 4215703, 4215802, 4215752, 4215901, 4216008, 4216057, 4216107, 4216206, 4216305, 4216354, 4216255, 4216404, 4216503, 4216602, 4216701, 4216800, 4216909, 4217006, 4217105, 4217154, 4217204, 4217253, 4217303, 4217402, 4217501, 4217550, 4217600, 4217709, 4217758, 4217808, 4217907, 4217956, 4218004, 4218103, 4218202, 4218251, 4218301, 4218350, 4218400, 4218509, 4218608, 4218707, 4218756, 4218806, 4218855, 4218905, 4218954, 4219002, 4219101, 4219150, 4219176, 4219200, 4219309, 4219358, 4219408, 4219507, 4219606, 4219705, 4219853, 4100103, 4100202, 4100301, 4100400, 4100459, 4128625, 4100608, 4100707, 4100509, 4100806, 4100905, 4101002, 4101051, 4101101, 4101150, 4101200, 4101309, 4101408, 4101507, 4101606, 4101655, 4101705, 4101804, 4101853, 4101903, 4102000, 4102109, 4102208, 4102307, 4102406, 4102505, 4102703, 4102604, 4102752, 4102802, 4102901, 4103008, 4103024, 4103040, 4103057, 4103107, 4103156, 4103206, 4103222, 4103305, 4103354, 4103370, 4103404, 4103453, 4103479, 4103503, 4103602, 4103701, 4103800, 4103909, 4103958, 4104006, 4104055, 4104105, 4104204, 4104253, 4104303, 4104402, 4104428, 4104451, 4104501, 4104600, 4104659, 4104709, 4104808, 4104907, 4105003, 4105102, 4105201, 4105300, 4105409, 4105508, 4105607, 4105706, 4105805, 4105904, 4106001, 4106100, 4106209, 4106308, 4106407, 4106456, 4106506, 4106555, 4106803, 4106571, 4106605, 4106704, 4106852, 4106902, 4107009, 4107108, 4107124, 4107157, 4107207, 4107256, 4107306, 4128633, 4107405, 4107504, 4107538, 4107520, 4107546, 4107553, 4107603, 4107652, 4107702, 4107736, 4107751, 4107850, 4107801, 4107900, 4108007, 4108106, 4108205, 4108304, 4108452, 4108320, 4108403, 4108502, 4108551, 4108601, 4108650, 4108700, 4108809, 4108908, 4108957, 4109005, 4109104, 4109203, 4109302, 4109401, 4109500, 4109609, 4109658, 4109708, 4109757, 4109807, 4109906, 4110003, 4110052, 4110078, 4110102, 4110201, 4110300, 4110409, 4110508, 4110607, 4110656, 4110706, 4110805, 4110904, 4110953, 4111001, 4111100, 4111209, 4111258, 4111308, 4111407, 4111506, 4111555, 4111605, 4111704, 4111803, 4111902, 4112009, 4112108, 4112207, 4112306, 4112405, 4112504, 4112603, 4112702, 4112751, 4112801, 4112900, 4112959, 4113007, 4113106, 4113205, 4113254, 4113304, 4113403, 4113429, 4113452, 4113502, 4113601, 4113700, 4113734, 4113759, 4113809, 4113908, 4114005, 4114104, 4114203, 4114302, 4114351, 4114401, 4114500, 4114609, 4114708, 4114807, 4114906, 4115002, 4115101, 4115200, 4115309, 4115358, 4115408, 4115457, 4115507, 4115606, 4115705, 4115739, 4115754, 4115804, 4115853, 4115903, 4116000, 4116059, 4116109, 4116208, 4116307, 4116406, 4116505, 4116604, 4116703, 4116802, 4116901, 4116950, 4117008, 4117057, 4117107, 4117206, 4117255, 4117214, 4117222, 4117271, 4117297, 4117305, 4117404, 4117453, 4117503, 4117602, 4117701, 4117800, 4117909, 4118006, 4118105, 4118204, 4118303, 4118402, 4118451, 4118501, 4118600, 4118709, 4118808, 4118857, 4118907, 4119004, 4119103, 4119152, 4119251, 4119202, 4119301, 4119400, 4119509, 4119608, 4119657, 4119707, 4119806, 4119905, 4119954, 4120002, 4120101, 4120150, 4120200, 4120309, 4120333, 4120358, 4120408, 4120507, 4120606, 4120655, 4120705, 4120804, 4120853, 4120903, 4121000, 4121109, 4121208, 4121257, 4121307, 4121356, 4121406, 4121505, 4121604, 4121703, 4121752, 4121802, 4121901, 4122008, 4122107, 4122156, 4122172, 4122206, 4122305, 4122404, 4122503, 4122602, 4122651, 4122701, 4122800, 4122909, 4123006, 4123105, 4123204, 4123303, 4123402, 4123501, 4123600, 4123709, 4123808, 4123824, 4123857, 4123907, 4123956, 4124020, 4124053, 4124004, 4124103, 4124202, 4124301, 4124400, 4124509, 4124608, 4124707, 4124806, 4124905, 4125001, 4125100, 4125308, 4125357, 4125209, 4125407, 4125456, 4125506, 4125555, 4125605, 4125704, 4125753, 4125803, 4125902, 4126009, 4126108, 4126207, 4126256, 4126272, 4126306, 4126355, 4126405, 4126504, 4126603, 4126652, 4126678, 4126702, 4126801, 4126900, 4127007, 4127106, 4127205, 4127304, 4127403, 4127502, 4127601, 4127700, 4127809, 4127858, 4127882, 4127908, 4127957, 4127965, 4128005, 4128104, 4128203, 4128302, 4128401, 4128534, 4128559, 4128609, 4128658, 4128708, 4128500, 4128807, 2900108, 2900207, 2900306, 2900355, 2900405, 2900603, 2900702, 2900801, 2900900, 2901007, 2901106, 2901155, 2901205, 2901304, 2901353, 2901403, 2901502, 2901601, 2901700, 2901809, 2901908, 2901957, 2902054, 2902005, 2902104, 2902203, 2902252, 2902302, 2902401, 2902500, 2902609, 2902658, 2902708, 2902807, 2902906, 2903003, 2903102, 2903201, 2903235, 2903300, 2903276, 2903409, 2903508, 2903607, 2903706, 2903805, 2903904, 2903953, 2904001, 2904050, 2904100, 2904209, 2904308, 2904407, 2904506, 2904605, 2904704, 2904753, 2904803, 2904852, 2904902, 2905008, 2905107, 2905156, 2905206, 2905305, 2905404, 2905503, 2905602, 2905701, 2905800, 2905909, 2906006, 2906105, 2906204, 2906303, 2906402, 2906501, 2906600, 2906709, 2906808, 2906824, 2906857, 2906873, 2906899, 2906907, 2907004, 2907103, 2907202, 2907301, 2907400, 2907509, 2907558, 2907608, 2907707, 2907806, 2907905, 2908002, 2908101, 2908200, 2908309, 2908408, 2908507, 2908606, 2908705, 2908804, 2908903, 2909000, 2909109, 2909208, 2909307, 2909406, 2909505, 2909604, 2909703, 2909802, 2909901, 2910008, 2910057, 2910107, 2910206, 2910305, 2910404, 2910503, 2900504, 2910602, 2910701, 2910727, 2910750, 2910776, 2910800, 2910859, 2910909, 2911006, 2911105, 2911204, 2911253, 2911303, 2911402, 2911501, 2911600, 2911659, 2911709, 2911808, 2911857, 2911907, 2912004, 2912103, 2912202, 2912301, 2912400, 2912509, 2912608, 2912707, 2912806, 2912905, 2913002, 2913101, 2913200, 2913309, 2913408, 2913457, 2913507, 2913606, 2913705, 2913804, 2913903, 2914000, 2914109, 2914208, 2914307, 2914406, 2914505, 2914604, 2914653, 2914703, 2914802, 2914901, 2915007, 2915106, 2915205, 2915304, 2915353, 2915403, 2915502, 2915601, 2915700, 2915809, 2915908, 2916005, 2916104, 2916203, 2916302, 2916401, 2916500, 2916609, 2916708, 2916807, 2916856, 2916906, 2917003, 2917102, 2917201, 2917300, 2917334, 2917359, 2917409, 2917508, 2917607, 2917706, 2917805, 2917904, 2918001, 2918100, 2918209, 2918308, 2918357, 2918407, 2918456, 2918506, 2918555, 2918605, 2918704, 2918753, 2918803, 2918902, 2919009, 2919058, 2919108, 2919157, 2919207, 2919306, 2919405, 2919504, 2919553, 2919603, 2919702, 2919801, 2919900, 2919926, 2919959, 2920007, 2920106, 2920205, 2920304, 2920403, 2920452, 2920502, 2920601, 2920700, 2920809, 2920908, 2921005, 2921054, 2921104, 2921203, 2921302, 2921401, 2921450, 2921500, 2921609, 2921708, 2921807, 2921906, 2922003, 2922052, 2922102, 2922201, 2922250, 2922300, 2922409, 2922508, 2922607, 2922656, 2922706, 2922730, 2922755, 2922805, 2922854, 2922904, 2923001, 2923035, 2923050, 2923100, 2923209, 2923308, 2923357, 2923407, 2923506, 2923605, 2923704, 2923803, 2923902, 2924009, 2924058, 2924108, 2924207, 2924306, 2924405, 2924504, 2924603, 2924652, 2924678, 2924702, 2924801, 2924900, 2925006, 2925105, 2925204, 2925253, 2925303, 2925402, 2925501, 2925600, 2925709, 2925758, 2925808, 2925907, 2925931, 2925956, 2926004, 2926103, 2926202, 2926301, 2926400, 2926509, 2926608, 2926657, 2926707, 2926806, 2926905, 2927002, 2927101, 2927200, 2927309, 2927408, 2927507, 2927606, 2927705, 2927804, 2927903, 2928059, 2928109, 2928406, 2928505, 2928000, 2928208, 2928307, 2928604, 2928703, 2928802, 2928901, 2928950, 2929107, 2929008, 2929057, 2929206, 2929255, 2929305, 2929354, 2929370, 2929404, 2929503, 2929602, 2929701, 2929750, 2929800, 2929909, 2930006, 2930105, 2930204, 2930154, 2930303, 2930402, 2930501, 2930600, 2930709, 2930758, 2930766, 2930774, 2930808, 2930907, 2931004, 2931053, 2931103, 2931202, 2931301, 2931350, 2931400, 2931509, 2931608, 2931707, 2931806, 2931905, 2932002, 2932101, 2932200, 2932309, 2932408, 2932457, 2932507, 2932606, 2932705, 2932804, 2932903, 2933000, 2933059, 2933109, 2933158, 2933174, 2933208, 2933257, 2933307, 2933406, 2933455, 2933505, 2933604, 4300034, 4300059, 4300109, 4300208, 4300307, 4300406, 4300455, 4300471, 4300505, 4300554, 4300570, 4300604, 4300638, 4300646, 4300661, 4300703, 4300802, 4300851, 4300877, 4300901, 4301008, 4301073, 4301057, 4301206, 4301107, 4301305, 4301404, 4301503, 4301552, 4301602, 4301636, 4301651, 4301701, 4301750, 4301859, 4301875, 4301909, 4301925, 4301958, 4301800, 4302006, 4302055, 4302105, 4302154, 4302204, 4302220, 4302238, 4302253, 4302303, 4302352, 4302378, 4302402, 4302451, 4302501, 4302584, 4302600, 4302659, 4302709, 4302808, 4302907, 4303004, 4303103, 4303202, 4303301, 4303400, 4303509, 4303558, 4303608, 4303673, 4303707, 4303806, 4303905, 4304002, 4304101, 4304200, 4304309, 4304358, 4304408, 4304507, 4304606, 4304614, 4304622, 4304630, 4304655, 4304663, 4304689, 4304697, 4304671, 4304713, 4304705, 4304804, 4304853, 4304903, 4304952, 4305009, 4305108, 4305116, 4305124, 4305132, 4305157, 4305173, 4305207, 4305306, 4305355, 4305371, 4305405, 4305439, 4305447, 4305454, 4305504, 4305587, 4305603, 4305702, 4305801, 4305835, 4305850, 4305871, 4305900, 4305934, 4305959, 4305975, 4306007, 4306056, 4306072, 4306106, 4306130, 4306205, 4306304, 4306320, 4306353, 4306379, 4306403, 4306429, 4306452, 4306502, 4306601, 4306551, 4306700, 4306734, 4306759, 4306767, 4306809, 4306908, 4306924, 4306957, 4306932, 4306973, 4307005, 4307054, 4307203, 4307302, 4307401, 4307450, 4307500, 4307559, 4307609, 4307708, 4307807, 4307815, 4307831, 4307864, 4307906, 4308003, 4308052, 4308078, 4308102, 4308201, 4308250, 4308300, 4308409, 4308433, 4308458, 4308508, 4308607, 4308656, 4308706, 4308805, 4308854, 4308904, 4309001, 4309050, 4309100, 4309126, 4309159, 4309209, 4309258, 4309308, 4309407, 4309506, 4309555, 4307104, 4309571, 4309605, 4309654, 4309704, 4309753, 4309803, 4309902, 4309951, 4310009, 4310108, 4310207, 4310306, 4310330, 4310363, 4310405, 4310413, 4310439, 4310462, 4310504, 4310538, 4310553, 4310579, 4310603, 4310652, 4310702, 4310751, 4310801, 4310850, 4310876, 4310900, 4311007, 4311106, 4311122, 4311130, 4311155, 4311205, 4311239, 4311270, 4311304, 4311254, 4311403, 4311429, 4311502, 4311601, 4311627, 4311643, 4311718, 4311700, 4311734, 4311759, 4311775, 4311791, 4311809, 4311908, 4311981, 4312005, 4312054, 4312104, 4312138, 4312153, 4312179, 4312203, 4312252, 4312302, 4312351, 4312377, 4312385, 4312401, 4312427, 4312443, 4312450, 4312476, 4312500, 4312609, 4312617, 4312625, 4312658, 4312674, 4312708, 4312757, 4312807, 4312906, 4312955, 4313003, 4313011, 4313037, 4313060, 4313086, 4313102, 4313201, 4313300, 4313334, 4313359, 4313375, 4313490, 4313391, 4313409, 4313425, 4313441, 4313466, 4313508, 4313607, 4313656, 4313706, 4313805, 4313904, 4313953, 4314001, 4314027, 4314035, 4314050, 4314068, 4314076, 4314100, 4314134, 4314159, 4314175, 4314209, 4314308, 4314407, 4314423, 4314456, 4314464, 4314472, 4314498, 4314506, 4314555, 4314605, 4314704, 4314753, 4314779, 4314787, 4314803, 4314902, 4315008, 4315057, 4315073, 4315107, 4315131, 4315149, 4315156, 4315172, 4315206, 4315305, 4315313, 4315321, 4315354, 4315404, 4315453, 4315503, 4315552, 4315602, 4315701, 4315750, 4315800, 4315909, 4315958, 4316006, 4316105, 4316204, 4316303, 4316402, 4316428, 4316436, 4316451, 4316477, 4316501, 4316600, 4316709, 4316733, 4316758, 4316808, 4316972, 4316907, 4316956, 4317202, 4317251, 4317301, 4317004, 4317103, 4317400, 4317509, 4317608, 4317707, 4317558, 4317756, 4317806, 4317905, 4317954, 4318002, 4318051, 4318101, 4318200, 4318309, 4318408, 4318424, 4318432, 4318440, 4318457, 4318465, 4318481, 4318499, 4318507, 4318606, 4318614, 4318622, 4318705, 4318804, 4318903, 4319000, 4319109, 4319125, 4319158, 4319208, 4319307, 4319356, 4319364, 4319372, 4319406, 4319505, 4319604, 4319703, 4319711, 4319737, 4319752, 4319802, 4319901, 4320008, 4320107, 4320206, 4320230, 4320263, 4320305, 4320321, 4320354, 4320404, 4320453, 4320503, 4320552, 4320578, 4320602, 4320651, 4320677, 4320701, 4320800, 4320859, 4320909, 4321006, 4321105, 4321204, 4321303, 4321329, 4321352, 4321402, 4321436, 4321451, 4321469, 4321477, 4321493, 4321501, 4321600, 4321626, 4321634, 4321667, 4321709, 4321808, 4321832, 4321857, 4321907, 4321956, 4322004, 4322103, 4322152, 4322186, 4322202, 4322251, 4322301, 4322327, 4322343, 4322350, 4322376, 4322400, 4322509, 4322533, 4322541, 4322525, 4322558, 4322608, 4322707, 4322806, 4322855, 4322905, 4323002, 4323101, 4323200, 4323309, 4323358, 4323408, 4323457, 4323507, 4323606, 4323705, 4323754, 4323770, 4323804, 3500105, 3500204, 3500303, 3500402, 3500501, 3500550, 3500600, 3500709, 3500758, 3500808, 3500907, 3501004, 3501103, 3501152, 3501202, 3501301, 3501400, 3501509, 3501608, 3501707, 3501806, 3501905, 3502002, 3502101, 3502200, 3502309, 3502408, 3502507, 3502606, 3502705, 3502754, 3502804, 3502903, 3503000, 3503109, 3503158, 3503208, 3503307, 3503356, 3503406, 3503505, 3503604, 3503703, 3503802, 3503901, 3503950, 3504008, 3504107, 3504206, 3504305, 3504404, 3504503, 3504602, 3504701, 3504800, 3504909, 3505005, 3505104, 3505203, 3505302, 3505351, 3505401, 3505500, 3505609, 3505708, 3505807, 3505906, 3506003, 3506102, 3506201, 3506300, 3506359, 3506409, 3506508, 3506607, 3506706, 3506805, 3506904, 3507001, 3507100, 3507159, 3507209, 3507308, 3507407, 3507456, 3507506, 3507605, 3507704, 3507753, 3507803, 3507902, 3508009, 3508108, 3508207, 3508306, 3508405, 3508504, 3508603, 3508702, 3508801, 3508900, 3509007, 3509106, 3509205, 3509254, 3509304, 3509403, 3509452, 3509502, 3509601, 3509700, 3509809, 3509908, 3509957, 3510005, 3510104, 3510153, 3510203, 3510302, 3510401, 3510500, 3510609, 3510708, 3510807, 3510906, 3511003, 3511102, 3511201, 3511300, 3511409, 3511508, 3511607, 3511706, 3557204, 3511904, 3512001, 3512100, 3512209, 3512308, 3512407, 3512506, 3512605, 3512704, 3512803, 3512902, 3513009, 3513108, 3513207, 3513306, 3513405, 3513504, 3513603, 3513702, 3513801, 3513850, 3513900, 3514007, 3514106, 3514205, 3514304, 3514403, 3514502, 3514601, 3514700, 3514809, 3514908, 3514924, 3514957, 3515004, 3515004, 3515103, 3515129, 3515152, 3515186, 3515194, 3557303, 3515301, 3515202, 3515350, 3515400, 3515608, 3515509, 3515657, 3515707, 3515806, 3515905, 3516002, 3516101, 3516200, 3516309, 3516408, 3516507, 3516606, 3516705, 3516804, 3516853, 3516903, 3517000, 3517109, 3517208, 3517307, 3517406, 3517505, 3517604, 3517703, 3517802, 3517901, 3518008, 3518107, 3518206, 3518305, 3518404, 3518503, 3518602, 3518701, 3518800, 3518859, 3518909, 3519006, 3519055, 3519071, 3519105, 3519204, 3519253, 3519303, 3519402, 3519501, 3519600, 3519709, 3519808, 3519907, 3520004, 3520103, 3520202, 3520301, 3520426, 3520442, 3520400, 3520509, 3520608, 3520707, 3520806, 3520905, 3521002, 3521101, 3521150, 3521200, 3521309, 3521408, 3521507, 3521606, 3521705, 3521804, 3521903, 3522000, 3522109, 3522158, 3522208, 3522307, 3522406, 3522505, 3522604, 3522653, 3522703, 3522802, 3522901, 3523008, 3523107, 3523206, 3523305, 3523404, 3523503, 3523602, 3523701, 3523800, 3523909, 3524006, 3524105, 3524204, 3524303, 3524402, 3524501, 3524600, 3524709, 3524808, 3524907, 3525003, 3525102, 3525201, 3525300, 3525409, 3525508, 3525607, 3525706, 3525805, 3525854, 3525904, 3526001, 3526100, 3526209, 3526308, 3526407, 3526506, 3526605, 3526704, 3526803, 3526902, 3527009, 3527108, 3527207, 3527256, 3527306, 3527405, 3527504, 3527603, 3527702, 3527801, 3527900, 3528007, 3528106, 3528205, 3528304, 3528403, 3528502, 3528601, 3528700, 3528809, 3528858, 3528908, 3529005, 3529104, 3529203, 3529302, 3529401, 3529500, 3529609, 3529658, 3529708, 3529807, 3530003, 3529906, 3530102, 3530201, 3530300, 3530409, 3530508, 3530607, 3530706, 3530805, 3530904, 3531001, 3531100, 3531209, 3531308, 3531407, 3531506, 3531605, 3531803, 3531704, 3531902, 3532009, 3532058, 3532108, 3532157, 3532207, 3532306, 3532405, 3532504, 3532603, 3532702, 3532801, 3532827, 3532843, 3532868, 3532900, 3533007, 3533106, 3533205, 3533304, 3533403, 3533254, 3533502, 3533601, 3533700, 3533809, 3533908, 3534005, 3534104, 3534203, 3534302, 3534401, 3534500, 3534609, 3534708, 3534807, 3534757, 3534906, 3535002, 3535101, 3535200, 3535309, 3535408, 3535507, 3535606, 3535705, 3535804, 3535903, 3536000, 3536109, 3536208, 3536257, 3536307, 3536406, 3536505, 3536570, 3536604, 3536703, 3536802, 3536901, 3537008, 3537107, 3537156, 3537206, 3537305, 3537404, 3537503, 3537602, 3537701, 3537800, 3537909, 3538006, 3538105, 3538204, 3538303, 3538501, 3538600, 3538709, 3538808, 3538907, 3539004, 3539103, 3539202, 3539301, 3539400, 3539509, 3539608, 3539707, 3539806, 3539905, 3540002, 3540101, 3540200, 3540259, 3540309, 3540408, 3540507, 3540606, 3540705, 3540754, 3540804, 3540853, 3540903, 3541000, 3541059, 3541109, 3541208, 3541307, 3541406, 3541505, 3541604, 3541653, 3541703, 3541802, 3541901, 3542008, 3542107, 3542206, 3542305, 3542404, 3542503, 3542602, 3542701, 3542800, 3542909, 3543006, 3543105, 3543204, 3543238, 3543253, 3543303, 3543402, 3543600, 3543709, 3543808, 3543907, 3544004, 3544103, 3544202, 3543501, 3544251, 3544301, 3544400, 3544509, 3544608, 3544707, 3544806, 3544905, 3545001, 3545100, 3545159, 3545209, 3545308, 3545407, 3545506, 3545605, 3545704, 3545803, 3546009, 3546108, 3546207, 3546256, 3546306, 3546405, 3546504, 3546603, 3546702, 3546801, 3546900, 3547007, 3547106, 3547502, 3547403, 3547601, 3547650, 3547205, 3547304, 3547700, 3547809, 3547908, 3548005, 3548054, 3548104, 3548203, 3548302, 3548401, 3548500, 3548609, 3548708, 3548807, 3548906, 3549003, 3549102, 3549201, 3549250, 3549300, 3549409, 3549508, 3549607, 3549706, 3549805, 3549904, 3549953, 3550001, 3550100, 3550209, 3550308, 3550407, 3550506, 3550605, 3550704, 3550803, 3550902, 3551009, 3551108, 3551207, 3551306, 3551405, 3551603, 3551504, 3551702, 3551801, 3551900, 3552007, 3552106, 3552205, 3552304, 3552403, 3552551, 3552502, 3552601, 3552700, 3552809, 3552908, 3553005, 3553104, 3553203, 3553302, 3553401, 3553500, 3553609, 3553658, 3553708, 3553807, 3553856, 3553906, 3553955, 3554003, 3554102, 3554201, 3554300, 3554409, 3554508, 3554607, 3554656, 3554706, 3554755, 3554805, 3554904, 3554953, 3555000, 3555109, 3555208, 3555307, 3555356, 3555406, 3555505, 3555604, 3555703, 3555802, 3555901, 3556008, 3556107, 3556206, 3556305, 3556354, 3556404, 3556453, 3556503, 3556602, 3556701, 3556800, 3556909, 3556958, 3557006, 3557105, 3557154, 3100104, 3100203, 3100302, 3100401, 3100500, 3100609, 3100708, 3100807, 3100906, 3101003, 3101102, 3101201, 3101300, 3101409, 3101508, 3101607, 3101631, 3101706, 3101805, 3101904, 3102001, 3102050, 3153509, 3102100, 3102209, 3102308, 3102407, 3102506, 3102605, 3102803, 3102852, 3102902, 3103009, 3103108, 3103207, 3103306, 3103405, 3103504, 3103603, 3103702, 3103751, 3103801, 3103900, 3104007, 3104106, 3104205, 3104304, 3104403, 3104452, 3104502, 3104601, 3104700, 3104809, 3104908, 3105004, 3105103, 3105202, 3105301, 3105400, 3105509, 3105608, 3105707, 3105905, 3106002, 3106101, 3106200, 3106309, 3106408, 3106507, 3106655, 3106606, 3106705, 3106804, 3106903, 3107000, 3107109, 3107208, 3107307, 3107406, 3107505, 3107604, 3107703, 3107802, 3107901, 3108008, 3108107, 3108206, 3108255, 3108305, 3108404, 3108503, 3108701, 3108552, 3108602, 3108909, 3108800, 3109006, 3109105, 3109204, 3109253, 3109303, 3109402, 3109451, 3109501, 3109600, 3109709, 3102704, 3109808, 3109907, 3110004, 3110103, 3110202, 3110301, 3110400, 3110509, 3110608, 3110707, 3110806, 3110905, 3111002, 3111101, 3111150, 3111200, 3111309, 3111408, 3111507, 3111606, 3111903, 3111705, 3111804, 3112000, 3112059, 3112109, 3112208, 3112307, 3112406, 3112505, 3112604, 3112653, 3112703, 3112802, 3112901, 3113008, 3113107, 3113206, 3113305, 3113404, 3113503, 3113602, 3113701, 3113800, 3113909, 3114006, 3114105, 3114204, 3114303, 3114402, 3114501, 3114550, 3114600, 3114709, 3114808, 3114907, 3115003, 3115102, 3115300, 3115359, 3115409, 3115458, 3115474, 3115508, 3115607, 3115706, 3115805, 3115904, 3116001, 3116100, 3116159, 3116209, 3116308, 3116407, 3116506, 3116605, 3116704, 3116803, 3116902, 3117009, 3117108, 3115201, 3117306, 3117207, 3117405, 3117504, 3117603, 3117702, 3117801, 3117836, 3117876, 3117900, 3118007, 3118106, 3118205, 3118304, 3118403, 3118502, 3118601, 3118700, 3118809, 3118908, 3119005, 3119104, 3119203, 3119302, 3119401, 3119500, 3119609, 3119708, 3119807, 3119906, 3119955, 3120003, 3120102, 3120151, 3120201, 3120300, 3120409, 3120508, 3120607, 3120706, 3120805, 3120839, 3120870, 3120904, 3121001, 3121100, 3121209, 3121258, 3121308, 3121407, 3121506, 3121605, 3121704, 3121803, 3121902, 3122009, 3122108, 3122207, 3122306, 3122355, 3122405, 3122454, 3122470, 3122504, 3122603, 3122702, 3122801, 3122900, 3123007, 3123106, 3123205, 3123304, 3123403, 3123502, 3123528, 3123601, 3123700, 3123809, 3123858, 3123908, 3124005, 3124104, 3124203, 3124302, 3124401, 3124500, 3124609, 3124708, 3124807, 3124906, 3125002, 3125101, 3125200, 3125309, 3125408, 3125606, 3125705, 3125804, 3125903, 3125952, 3126000, 3126109, 3126208, 3126307, 3126406, 3126505, 3126604, 3126703, 3126752, 3126802, 3126901, 3126950, 3127008, 3127057, 3127073, 3127107, 3127206, 3127305, 3127339, 3127354, 3127370, 3127388, 3127404, 3127503, 3127602, 3127701, 3127800, 3127909, 3128006, 3128105, 3128204, 3128253, 3128303, 3128402, 3128501, 3128600, 3128709, 3128808, 3128907, 3129004, 3129103, 3129202, 3129301, 3129400, 3129509, 3129608, 3129657, 3129707, 3129806, 3129905, 3130002, 3130051, 3130101, 3130200, 3130309, 3130408, 3130507, 3130556, 3130606, 3130655, 3130705, 3130804, 3130903, 3131000, 3131109, 3131158, 3131208, 3131307, 3131406, 3131505, 3131604, 3131703, 3131802, 3131901, 3132008, 3132107, 3132206, 3132305, 3132404, 3132503, 3132602, 3132701, 3132800, 3132909, 3133006, 3133105, 3133204, 3133303, 3133402, 3133501, 3133600, 3133709, 3133758, 3133808, 3133907, 3134004, 3134103, 3134202, 3134301, 3134400, 3134509, 3134608, 3134707, 3134806, 3134905, 3135001, 3135050, 3135076, 3135100, 3135209, 3135308, 3135357, 3135407, 3135456, 3135506, 3135605, 3135704, 3135803, 3135902, 3136009, 3136108, 3136207, 3136306, 3136405, 3136504, 3136520, 3136553, 3136579, 3136652, 3136702, 3136801, 3136900, 3136959, 3137007, 3137106, 3137205, 3137304, 3137403, 3137502, 3137536, 3137601, 3137700, 3137809, 3137908, 3138005, 3138104, 3138203, 3138302, 3138351, 3138401, 3138500, 3138609, 3138625, 3138658, 3138674, 3138682, 3138708, 3138807, 3138906, 3139003, 3139102, 3139201, 3139250, 3139300, 3139409, 3139508, 3139607, 3139805, 3139706, 3139904, 3140001, 3140100, 3140159, 3140209, 3140308, 3140407, 3140506, 3140530, 3140555, 3140605, 3140704, 3171501, 3140803, 3140852, 3140902, 3141009, 3141108, 3141207, 3141306, 3141405, 3141504, 3141603, 3141702, 3141801, 3141900, 3142007, 3142106, 3142205, 3142254, 3142304, 3142403, 3142502, 3142601, 3142700, 3142809, 3142908, 3143005, 3143104, 3143153, 3143203, 3143401, 3143302, 3143450, 3143500, 3143609, 3143708, 3143807, 3143906, 3144003, 3144102, 3144201, 3144300, 3144359, 3144375, 3144409, 3144508, 3144607, 3144656, 3144672, 3144706, 3144805, 3144904, 3145000, 3145059, 3145109, 3145208, 3136603, 3145307, 3145356, 3145372, 3145406, 3145455, 3145505, 3145604, 3145703, 3145802, 3145851, 3145877, 3145901, 3146008, 3146107, 3146206, 3146255, 3146305, 3146552, 3146404, 3146503, 3146602, 3146701, 3146750, 3146909, 3147105, 3147006, 3147204, 3147303, 3147402, 3147600, 3147709, 3147501, 3147808, 3147907, 3147956, 3148004, 3148103, 3148202, 3148301, 3148400, 3148509, 3148608, 3148707, 3148756, 3148806, 3148905, 3149002, 3149101, 3149150, 3149200, 3149309, 3149408, 3149507, 3149606, 3149705, 3149804, 3149903, 3149952, 3150000, 3150109, 3150158, 3150208, 3150307, 3150406, 3150505, 3150539, 3150570, 3150604, 3150703, 3150802, 3150901, 3151008, 3151107, 3151206, 3151305, 3151404, 3151503, 3151602, 3151701, 3151800, 3151909, 3152006, 3152105, 3152131, 3152170, 3152204, 3152303, 3152402, 3152501, 3152600, 3152709, 3152808, 3152907, 3153004, 3153103, 3153202, 3153301, 3153400, 3153608, 3153707, 3153806, 3153905, 3154002, 3154101, 3154150, 3154200, 3154309, 3154408, 3154457, 3154507, 3154606, 3154705, 3154804, 3154903, 3155108, 3155009, 3155207, 3155306, 3155405, 3155504, 3155603, 3155702, 3155801, 3155900, 3156007, 3156106, 3156205, 3156304, 3156403, 3156452, 3156502, 3156601, 3156700, 3156809, 3156908, 3157005, 3157104, 3157203, 3157252, 3157278, 3157302, 3157336, 3157377, 3157401, 3157500, 3157609, 3157658, 3157708, 3157807, 3157906, 3158003, 3158102, 3158201, 3159209, 3159407, 3159308, 3159357, 3159506, 3159605, 3159704, 3159803, 3158300, 3158409, 3158508, 3158607, 3158706, 3158805, 3158904, 3158953, 3159001, 3159100, 3159902, 3160009, 3160108, 3160207, 3160306, 3160405, 3160454, 3160504, 3160603, 3160702, 3160801, 3160900, 3160959, 3161007, 3161056, 3161106, 3161205, 3161304, 3161403, 3161502, 3161601, 3161650, 3161700, 3161809, 3161908, 3125507, 3162005, 3162104, 3162203, 3162252, 3162302, 3162401, 3162450, 3162500, 3162559, 3162575, 3162609, 3162658, 3162708, 3162807, 3162906, 3162922, 3162948, 3162955, 3163003, 3163102, 3163201, 3163300, 3163409, 3163508, 3163607, 3163706, 3163805, 3163904, 3164100, 3164001, 3164209, 3164308, 3164407, 3164431, 3164472, 3164506, 3164605, 3164704, 3164803, 3164902, 3165206, 3165008, 3165107, 3165305, 3165404, 3165503, 3165537, 3165560, 3165578, 3165602, 3165701, 3165800, 3165909, 3166006, 3166105, 3166204, 3166303, 3166402, 3166501, 3166600, 3166808, 3166709, 3166907, 3166956, 3167004, 3167103, 3167202, 3165552, 3167301, 3167400, 3167509, 3167608, 3167707, 3167806, 3167905, 3168002, 3168051, 3168101, 3168200, 3168309, 3168408, 3168507, 3168606, 3168705, 3168804, 3168903, 3169000, 3169059, 3169109, 3169208, 3169307, 3169356, 3169406, 3169505, 3169604, 3169703, 3169802, 3169901, 3170008, 3170057, 3170107, 3170206, 3170305, 3170404, 3170438, 3170479, 3170503, 3170529, 3170578, 3170602, 3170651, 3170701, 3170750, 3170800, 3170909, 3171006, 3171030, 3171071, 3171105, 3171154, 3171204, 3171303, 3171402, 3171600, 3171709, 3171808, 3171907, 3172004, 3172103, 3172202, 2206720, 9999999, 5006275, 4314548, 4220000, 4212650')
                
                                    if 'uf' in dir(localTrabDom):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'localTrabDom.uf',
                                                                          localTrabDom.uf.cdata,
                                                                          1, u'None')

                    if 'horContratual' in dir(infoContrato.horContratual):
                        for horContratual in infoContrato.horContratual:
        
                            if 'qtdHrsSem' in dir(horContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'horContratual.qtdHrsSem',
                                                                  horContratual.qtdHrsSem.cdata,
                                                                  0, u'None')
        
                            if 'tpJornada' in dir(horContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'horContratual.tpJornada',
                                                                  horContratual.tpJornada.cdata,
                                                                  1, u'1, 2, 3, 9')
        
                            if 'dscTpJorn' in dir(horContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'horContratual.dscTpJorn',
                                                                  horContratual.dscTpJorn.cdata,
                                                                  0, u'None')
        
                            if 'tmpParc' in dir(horContratual):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'horContratual.tmpParc',
                                                                  horContratual.tmpParc.cdata,
                                                                  1, u'0, 1, 2, 3')
        
                            if 'horario' in dir(horContratual.horario):
                                for horario in horContratual.horario:
                
                                    if 'dia' in dir(horario):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'horario.dia',
                                                                          horario.dia.cdata,
                                                                          1, u'1, 2, 3, 4, 5, 6, 7, 8')
                
                                    if 'codHorContrat' in dir(horario):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'horario.codHorContrat',
                                                                          horario.codHorContrat.cdata,
                                                                          1, u'None')

                    if 'filiacaoSindical' in dir(infoContrato.filiacaoSindical):
                        for filiacaoSindical in infoContrato.filiacaoSindical:
        
                            if 'cnpjSindTrab' in dir(filiacaoSindical):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'filiacaoSindical.cnpjSindTrab',
                                                                  filiacaoSindical.cnpjSindTrab.cdata,
                                                                  1, u'None')

                    if 'alvaraJudicial' in dir(infoContrato.alvaraJudicial):
                        for alvaraJudicial in infoContrato.alvaraJudicial:
        
                            if 'nrProcJud' in dir(alvaraJudicial):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'alvaraJudicial.nrProcJud',
                                                                  alvaraJudicial.nrProcJud.cdata,
                                                                  1, u'None')

                    if 'observacoes' in dir(infoContrato.observacoes):
                        for observacoes in infoContrato.observacoes:
        
                            if 'observacao' in dir(observacoes):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'observacoes.observacao',
                                                                  observacoes.observacao.cdata,
                                                                  1, u'None')

                    if 'servPubl' in dir(infoContrato.servPubl):
                        for servPubl in infoContrato.servPubl:
        
                            if 'mtvAlter' in dir(servPubl):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'servPubl.mtvAlter',
                                                                  servPubl.mtvAlter.cdata,
                                                                  1, u'1, 2, 3, 8, 9')
    return validacoes_lista