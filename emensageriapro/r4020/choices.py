#coding:utf-8


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



CHOICES_EFDREINFINFORMACOESBENEFICIARIOSEXTERIOR = [

    (500, u'500 - A fonte pagadora é matriz da beneficiária no exterior.'),
    (510, u'510 - A fonte pagadora é filial, sucursal ou agência de beneficiária no exterior.'),
    (520, u'520 - A fonte pagadora é controlada ou coligada da beneficiária no exterior, na forma dos §§ 1º e 2º do art. 243 da Lei nº 6.404, de 15 de dezembro de 1976.'),
    (530, u'530 - A fonte pagadora é controladora ou coligada da beneficiária no exterior, na forma dos §§ 1º e 2º do art. 243 da Lei nº 6.404, de 1976.'),
    (540, u'540 - A fonte pagadora e a beneficiária no exterior estão sob controle societário ou administrativo comum ou quando pelo menos 10% do capital de cada uma, pertencer a uma mesma pessoa física ou jurídica.'),
    (550, u'550 - A fonte pagadora e a beneficiária no exterior têm participação societária no capital de uma terceira pessoa jurídica, cuja soma as caracterize como controladoras ou coligadas na forma dos §§ 1º e 2º do art. 243 da Lei nº 6.404, de 1976.'),
    (560, u'560 - A fonte pagadora ou a beneficiária no exterior mantenha contrato de exclusividade como agente, como distribuidor ou como concessionário nas operações com bens, serviços e direitos.'),
    (570, u'570 - A fonte pagadora e a beneficiária mantêm acordo de atuação conjunta.'),
    (900, u'900 - Não há relação entre a fonte pagadora e a beneficiária no exterior.'),

]




CHOICES_EFDREINFRENDIMENTOSBENEFICIARIOSEXTERIORTRIBUTACAO = [

    ('10', u'10 - Retenção do IRRF - alíquota padrão.'),
    ('11', u'11 - Retenção do IRRF - alíquota da tabela progressiva.'),
    ('12', u'12 - Retenção do IRRF - alíquota diferenciada (países com tributação favorecida).'),
    ('13', u'13 - Retenção do IRRF - alíquota limitada conforme cláusula em convênio.'),
    ('30', u'30 - Retenção do IRRF - outras hipóteses.'),
    ('40', u'40 - Não retenção do IRRF - isenção estabelecida em convênio.'),
    ('41', u'41 - Não retenção do IRRF - isenção prevista em lei interna'),
    ('42', u'42 - Não retenção do IRRF - alíquota Zero prevista em lei interna'),
    ('43', u'43 - Não retenção do IRRF - pagamento antecipado do imposto'),
    ('44', u'44 - Não retenção do IRRF - medida Judicial'),
    ('50', u'50 - Não retenção do IRRF - outras hipóteses'),

]




CHOICES_R4020_INDNIF = [

    (1, u'1 - Beneficiário com NIF'),
    (2, u'2 - Beneficiário dispensado do NIF'),
    (3, u'3 - País não exige NIF.'),

]




CHOICES_R4020_INDORIGEMRECURSOS = [

    (1, u'1 - Recursos do próprio declarante'),
    (2, u'2 - Recursos de terceiros - Declarante é a Instituição Financeira responsável apenas pelo repasse dos valores.'),

]




CHOICES_R4020_TPINSCADV = [

    (1, u'1 - Pessoa Física'),
    (2, u'2 - Pessoa Jurídica.'),

]




CHOICES_R4020_TPPROCRET = [

    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial.'),

]



