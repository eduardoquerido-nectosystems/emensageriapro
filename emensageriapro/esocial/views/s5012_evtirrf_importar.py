#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s5012.models import *
from emensageriapro.functions import read_from_xml



def read_s5012_evtirrf_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s5012_evtirrf_obj(request, doc, status, validar)
    return dados



def read_s5012_evtirrf(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s5012_evtirrf_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s5012evtIrrf.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s5012_evtirrf_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s5012_evtirrf_dados = {}
    s5012_evtirrf_dados['status'] = status
    s5012_evtirrf_dados['arquivo_original'] = 1
    if arquivo:
        s5012_evtirrf_dados['arquivo'] = arquivo.arquivo
    s5012_evtirrf_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s5012_evtirrf_dados['identidade'] = doc.eSocial.evtIrrf['Id']
    evtIrrf = doc.eSocial.evtIrrf

    try:
        s5012_evtirrf_dados['perapur'] = read_from_xml(evtIrrf.ideEvento.perApur.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5012_evtirrf_dados['tpinsc'] = read_from_xml(evtIrrf.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s5012_evtirrf_dados['nrinsc'] = read_from_xml(evtIrrf.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5012_evtirrf_dados['nrrecarqbase'] = read_from_xml(evtIrrf.infoIRRF.nrRecArqBase.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s5012_evtirrf_dados['indexistinfo'] = read_from_xml(evtIrrf.infoIRRF.indExistInfo.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    s5012_evtirrf = s5012evtIrrf.objects.create(**s5012_evtirrf_dados)

    if 'infoIRRF' in dir(evtIrrf) and 'infoCRContrib' in dir(evtIrrf.infoIRRF):

        for infoCRContrib in evtIrrf.infoIRRF.infoCRContrib:

            s5012_infocrcontrib_dados = {}
            s5012_infocrcontrib_dados['s5012_evtirrf_id'] = s5012_evtirrf.id

            try:
                s5012_infocrcontrib_dados['tpcr'] = read_from_xml(infoCRContrib.tpCR.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s5012_infocrcontrib_dados['vrcr'] = read_from_xml(infoCRContrib.vrCR.cdata, 'esocial', 'N', 2)
            except AttributeError:
                pass

            s5012_infocrcontrib = s5012infoCRContrib.objects.create(**s5012_infocrcontrib_dados)
    s5012_evtirrf_dados['evento'] = 's5012'
    s5012_evtirrf_dados['id'] = s5012_evtirrf.id
    s5012_evtirrf_dados['identidade_evento'] = doc.eSocial.evtIrrf['Id']

    from emensageriapro.esocial.views.s5012_evtirrf_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s5012_evtirrf.id)

    return s5012_evtirrf_dados