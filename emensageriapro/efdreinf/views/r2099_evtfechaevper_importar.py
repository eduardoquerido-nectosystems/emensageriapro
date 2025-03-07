#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.efdreinf.models import *
from emensageriapro.r2099.models import *
from emensageriapro.functions import read_from_xml



def read_r2099_evtfechaevper_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_r2099_evtfechaevper_obj(request, doc, status, validar)
    return dados



def read_r2099_evtfechaevper(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_r2099_evtfechaevper_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    r2099evtFechaEvPer.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_r2099_evtfechaevper_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.Reinf['xmlns'].split('/')

    r2099_evtfechaevper_dados = {}
    r2099_evtfechaevper_dados['status'] = status
    r2099_evtfechaevper_dados['arquivo_original'] = 1
    if arquivo:
        r2099_evtfechaevper_dados['arquivo'] = arquivo.arquivo
    r2099_evtfechaevper_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2099_evtfechaevper_dados['identidade'] = doc.Reinf.evtFechaEvPer['id']
    evtFechaEvPer = doc.Reinf.evtFechaEvPer

    try:
        r2099_evtfechaevper_dados['perapur'] = read_from_xml(evtFechaEvPer.ideEvento.perApur.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['tpamb'] = read_from_xml(evtFechaEvPer.ideEvento.tpAmb.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['procemi'] = read_from_xml(evtFechaEvPer.ideEvento.procEmi.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['verproc'] = read_from_xml(evtFechaEvPer.ideEvento.verProc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['tpinsc'] = read_from_xml(evtFechaEvPer.ideContri.tpInsc.cdata, 'efdreinf', 'N', None)
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['nrinsc'] = read_from_xml(evtFechaEvPer.ideContri.nrInsc.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['evtservtm'] = read_from_xml(evtFechaEvPer.infoFech.evtServTm.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['evtservpr'] = read_from_xml(evtFechaEvPer.infoFech.evtServPr.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['evtassdesprec'] = read_from_xml(evtFechaEvPer.infoFech.evtAssDespRec.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['evtassdesprep'] = read_from_xml(evtFechaEvPer.infoFech.evtAssDespRep.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['evtcomprod'] = read_from_xml(evtFechaEvPer.infoFech.evtComProd.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['evtcprb'] = read_from_xml(evtFechaEvPer.infoFech.evtCPRB.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['evtpgtos'] = read_from_xml(evtFechaEvPer.infoFech.evtPgtos.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    try:
        r2099_evtfechaevper_dados['compsemmovto'] = read_from_xml(evtFechaEvPer.infoFech.compSemMovto.cdata, 'efdreinf', 'C', None)
    except AttributeError:
        pass

    r2099_evtfechaevper = r2099evtFechaEvPer.objects.create(**r2099_evtfechaevper_dados)

    if 'ideRespInf' in dir(evtFechaEvPer):

        for ideRespInf in evtFechaEvPer.ideRespInf:

            r2099_iderespinf_dados = {}
            r2099_iderespinf_dados['r2099_evtfechaevper_id'] = r2099_evtfechaevper.id

            try:
                r2099_iderespinf_dados['nmresp'] = read_from_xml(ideRespInf.nmResp.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2099_iderespinf_dados['cpfresp'] = read_from_xml(ideRespInf.cpfResp.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2099_iderespinf_dados['telefone'] = read_from_xml(ideRespInf.telefone.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            try:
                r2099_iderespinf_dados['email'] = read_from_xml(ideRespInf.email.cdata, 'efdreinf', 'C', None)
            except AttributeError:
                pass

            r2099_iderespinf = r2099ideRespInf.objects.create(**r2099_iderespinf_dados)
    r2099_evtfechaevper_dados['evento'] = 'r2099'
    r2099_evtfechaevper_dados['id'] = r2099_evtfechaevper.id
    r2099_evtfechaevper_dados['identidade_evento'] = doc.Reinf.evtFechaEvPer['id']

    from emensageriapro.efdreinf.views.r2099_evtfechaevper_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, r2099_evtfechaevper.id)

    return r2099_evtfechaevper_dados