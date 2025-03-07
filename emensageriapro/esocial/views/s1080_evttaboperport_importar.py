#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s1080.models import *
from emensageriapro.functions import read_from_xml



def read_s1080_evttaboperport_string(request, dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s1080_evttaboperport_obj(request, doc, status, validar)
    return dados



def read_s1080_evttaboperport(request, dados, arquivo, validar=False):

    import untangle
    from emensageriapro.mensageiro.models import ImportacaoArquivosEventos
    from emensageriapro.mensageiro.views.processar_arquivos import move_event

    xml = ler_arquivo(arquivo.arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    dados = read_s1080_evttaboperport_obj(
        request, doc, STATUS_EVENTO_IMPORTADO, validar, arquivo)

    novo_arquivo = move_event(arquivo, 'processado')

    s1080evtTabOperPort.objects.filter(id=dados['id']).update(arquivo=novo_arquivo)

    ImportacaoArquivosEventos.objects.filter(id=arquivo.id).update(versao=dados['versao'], arquivo=novo_arquivo)

    return dados



def read_s1080_evttaboperport_obj(request, doc, status, validar=False, arquivo=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s1080_evttaboperport_dados = {}
    s1080_evttaboperport_dados['status'] = status
    s1080_evttaboperport_dados['arquivo_original'] = 1
    if arquivo:
        s1080_evttaboperport_dados['arquivo'] = arquivo.arquivo
    s1080_evttaboperport_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s1080_evttaboperport_dados['identidade'] = doc.eSocial.evtTabOperPort['Id']
    evtTabOperPort = doc.eSocial.evtTabOperPort

    if 'inclusao' in dir(evtTabOperPort.infoOperPortuario): s1080_evttaboperport_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTabOperPort.infoOperPortuario): s1080_evttaboperport_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTabOperPort.infoOperPortuario): s1080_evttaboperport_dados['operacao'] = 3

    try:
        s1080_evttaboperport_dados['tpamb'] = read_from_xml(evtTabOperPort.ideEvento.tpAmb.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1080_evttaboperport_dados['procemi'] = read_from_xml(evtTabOperPort.ideEvento.procEmi.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1080_evttaboperport_dados['verproc'] = read_from_xml(evtTabOperPort.ideEvento.verProc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    try:
        s1080_evttaboperport_dados['tpinsc'] = read_from_xml(evtTabOperPort.ideEmpregador.tpInsc.cdata, 'esocial', 'N', None)
    except AttributeError:
        pass

    try:
        s1080_evttaboperport_dados['nrinsc'] = read_from_xml(evtTabOperPort.ideEmpregador.nrInsc.cdata, 'esocial', 'C', None)
    except AttributeError:
        pass

    s1080_evttaboperport = s1080evtTabOperPort.objects.create(**s1080_evttaboperport_dados)

    if 'infoOperPortuario' in dir(evtTabOperPort) and 'inclusao' in dir(evtTabOperPort.infoOperPortuario):

        for inclusao in evtTabOperPort.infoOperPortuario.inclusao:

            s1080_inclusao_dados = {}
            s1080_inclusao_dados['s1080_evttaboperport_id'] = s1080_evttaboperport.id

            try:
                s1080_inclusao_dados['cnpjopportuario'] = read_from_xml(inclusao.ideOperPortuario.cnpjOpPortuario.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1080_inclusao_dados['inivalid'] = read_from_xml(inclusao.ideOperPortuario.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1080_inclusao_dados['fimvalid'] = read_from_xml(inclusao.ideOperPortuario.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1080_inclusao_dados['aliqrat'] = read_from_xml(inclusao.dadosOperPortuario.aliqRat.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1080_inclusao_dados['fap'] = read_from_xml(inclusao.dadosOperPortuario.fap.cdata, 'esocial', 'N', 4)
            except AttributeError:
                pass

            try:
                s1080_inclusao_dados['aliqratajust'] = read_from_xml(inclusao.dadosOperPortuario.aliqRatAjust.cdata, 'esocial', 'N', 4)
            except AttributeError:
                pass

            s1080_inclusao = s1080inclusao.objects.create(**s1080_inclusao_dados)

    if 'infoOperPortuario' in dir(evtTabOperPort) and 'alteracao' in dir(evtTabOperPort.infoOperPortuario):

        for alteracao in evtTabOperPort.infoOperPortuario.alteracao:

            s1080_alteracao_dados = {}
            s1080_alteracao_dados['s1080_evttaboperport_id'] = s1080_evttaboperport.id

            try:
                s1080_alteracao_dados['cnpjopportuario'] = read_from_xml(alteracao.ideOperPortuario.cnpjOpPortuario.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1080_alteracao_dados['inivalid'] = read_from_xml(alteracao.ideOperPortuario.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1080_alteracao_dados['fimvalid'] = read_from_xml(alteracao.ideOperPortuario.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1080_alteracao_dados['aliqrat'] = read_from_xml(alteracao.dadosOperPortuario.aliqRat.cdata, 'esocial', 'N', None)
            except AttributeError:
                pass

            try:
                s1080_alteracao_dados['fap'] = read_from_xml(alteracao.dadosOperPortuario.fap.cdata, 'esocial', 'N', 4)
            except AttributeError:
                pass

            try:
                s1080_alteracao_dados['aliqratajust'] = read_from_xml(alteracao.dadosOperPortuario.aliqRatAjust.cdata, 'esocial', 'N', 4)
            except AttributeError:
                pass

            s1080_alteracao = s1080alteracao.objects.create(**s1080_alteracao_dados)

            if 'novaValidade' in dir(alteracao):

                for novaValidade in alteracao.novaValidade:

                    s1080_alteracao_novavalidade_dados = {}
                    s1080_alteracao_novavalidade_dados['s1080_alteracao_id'] = s1080_alteracao.id

                    try:
                        s1080_alteracao_novavalidade_dados['inivalid'] = read_from_xml(novaValidade.iniValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    try:
                        s1080_alteracao_novavalidade_dados['fimvalid'] = read_from_xml(novaValidade.fimValid.cdata, 'esocial', 'C', None)
                    except AttributeError:
                        pass

                    s1080_alteracao_novavalidade = s1080alteracaonovaValidade.objects.create(**s1080_alteracao_novavalidade_dados)

    if 'infoOperPortuario' in dir(evtTabOperPort) and 'exclusao' in dir(evtTabOperPort.infoOperPortuario):

        for exclusao in evtTabOperPort.infoOperPortuario.exclusao:

            s1080_exclusao_dados = {}
            s1080_exclusao_dados['s1080_evttaboperport_id'] = s1080_evttaboperport.id

            try:
                s1080_exclusao_dados['cnpjopportuario'] = read_from_xml(exclusao.ideOperPortuario.cnpjOpPortuario.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1080_exclusao_dados['inivalid'] = read_from_xml(exclusao.ideOperPortuario.iniValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            try:
                s1080_exclusao_dados['fimvalid'] = read_from_xml(exclusao.ideOperPortuario.fimValid.cdata, 'esocial', 'C', None)
            except AttributeError:
                pass

            s1080_exclusao = s1080exclusao.objects.create(**s1080_exclusao_dados)
    s1080_evttaboperport_dados['evento'] = 's1080'
    s1080_evttaboperport_dados['id'] = s1080_evttaboperport.id
    s1080_evttaboperport_dados['identidade_evento'] = doc.eSocial.evtTabOperPort['Id']

    from emensageriapro.esocial.views.s1080_evttaboperport_validar_evento import validar_evento_funcao

    if validar:
        validar_evento_funcao(request, s1080_evttaboperport.id)

    return s1080_evttaboperport_dados