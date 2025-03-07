#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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

from constance import config
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.shortcuts import render,redirect
from emensageriapro.padrao import *
from emensageriapro.controle_de_acesso.forms import *
from emensageriapro.controle_de_acesso.models import *
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.core.urlresolvers import reverse
from datetime import datetime


def json_to_dict(texto):
    import json
    dicionario = json.loads(texto)
    return dicionario

def dict_to_json(dicionario):
    import json
    json_string = json.dumps(dicionario)
    return json_string


def gera_senha(tamanho):
    from random import choice
    caracters = '0123456789abcdefghijlmnopqrstuwvxz!?@#$'
    senha = ''
    for char in xrange(tamanho):
        senha += choice(caracters)
    return senha


def enviar_email_senha_recuperar(nome, email_usuario, senha):
    from django.utils.html import strip_tags
    from django.core.mail import send_mail
    from emensageriapro.settings import LINK_WEBSITE
    EMAIL_RECUPERACAO_SENHA = config.EMAIL_RECUPERACAO_SENHA
    EMAIL_RECUPERACAO_SENHA_ASSUNTO = config.EMAIL_RECUPERACAO_SENHA_ASSUNTO
    EMAIL_RECUPERACAO_SENHA_MENSAGEM = config.EMAIL_RECUPERACAO_SENHA_MENSAGEM
    user = User.objects.get(email=email_usuario)
    nome = '%s %s' % (user.first_name, user.last_name)
    dados = {}
    dados['nome'] = nome.upper()
    dados['endereco'] = LINK_WEBSITE
    dados['usuario'] = user.username
    dados['senha'] = senha
    mensagem_html = EMAIL_RECUPERACAO_SENHA_MENSAGEM % dados

    send_mail(
        EMAIL_RECUPERACAO_SENHA_ASSUNTO,
        strip_tags(mensagem_html),
        EMAIL_RECUPERACAO_SENHA,
        [ email_usuario, ],
        fail_silently=False,
        html_message=mensagem_html,
    )


def recuperar_senha_funcao(email):
    dados_usuario = User.objects.get(email=email)
    from django.contrib.auth.hashers import make_password
    nova_senha = gera_senha(10)
    hashed_password = make_password(nova_senha)
    User.objects.filter(email=email).update(password=hashed_password)
    enviar_email_senha_recuperar(dados_usuario.first_name, email, nova_senha)




def recuperar_senha(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            dados_usuario = User.objects.get(email=email)
        except:
            dados_usuario = None
        if dados_usuario:
            from django.contrib.auth.hashers import make_password
            nova_senha = gera_senha(10)
            hashed_password = make_password(nova_senha)
            User.objects.filter(email=email).update(password=hashed_password)
            enviar_email_senha_recuperar(dados_usuario.first_name, email, nova_senha)
            messages.success(request, 'Senha criada/alterada com sucesso, a nova senha foi enviada para seu e-mail!')
            return redirect('login')
        else:
            messages.error(request, 'Este email não está cadastrado em nossa base de dados!')
    context = {}
    return render(request, 'login_recuperar_senha.html', context)



def get_permissoes(permissoes):
    dict = {}
    for a in permissoes:
        chave = a.config_paginas.endereco
        dict[chave+'_listar'] = a.permite_listar
        dict[chave+'_cadastrar'] = a.permite_cadastrar
        dict[chave+'_editar'] = a.permite_editar
        dict[chave+'_visualizar'] = a.permite_visualizar
        dict[chave+'_apagar'] = a.permite_apagar
    return dict


#
#
#
# def make_password(txt_pass):
#     import hashlib
#     hash0 = hashlib.md5(txt_pass).hexdigest()
#     hash1 = hashlib.sha224(txt_pass).hexdigest()
#     txt_pass_hash = hash0+ hash1
#     return txt_pass_hash