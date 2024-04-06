import re

from wtforms import Form, BooleanField, StringField, TelField, EmailField, DecimalField, SelectField, validators, FileField, TextAreaField
from wtforms.validators import DataRequired


class VendaForm(Form):

    nome = StringField('Nome do carro', [validators.Length(min=3, max=50)])
    modelo = StringField('Modelo', [validators.Length(min=3, max=50)])
    marca = SelectField('Marca', choices=[('', ''), ('px', 'Pixar'), ('dny', 'Disney')])
    valor = StringField('Preço de venda')
    anexo = FileField('Anexo')
    descricao = TextAreaField('Descrição')


class CompraForm(Form):

    nome = StringField('Nome completo')
    cpf = StringField('CPF')
    telefone = StringField('Telefone')
    email = StringField('E-mail')

