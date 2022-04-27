from ast import If
from datetime import datetime
from mailbox import NotEmptyError
from flask import Blueprint, request

from modules.auth.validator import validate_login
from modules.auth.validator import validate_user_id
from modules.auth.validator import validate_t

auth_routes = Blueprint('auth', __name__)


USERS = [
    {
        'id': 1,
        'name': 'Carlos Noronha',
        'email': 'carlos@floatacademy.com',
        'celular': '12974020976',
        'password': '12345678',
        'created_at': datetime(2022, 5, 1, 12, 0),
        'updated_at': datetime(2022, 5, 1, 12, 0),
    },
    {
        'id': 2,
        'name': 'Marcos',
        'email': 'marcoshefa@gmail.com',
        'celular': '12974020975',
        'password': '123456',
        'created_at': datetime(2022, 5, 1, 12, 0),
        'updated_at': datetime(2022, 5, 1, 12, 0),
    }
]

EMPRESAS = [
    {
        'ID_empresa': 1,
        'nome':'Quimlab',
        'endereco':'jacareí',
        'telefone':'1239554646',
        'telefone_emergencia':'01234567',
        'email':'quimlab@quimlab.com.br',
    },
    {
        'ID_empresa': 2,
        'nome':'Quimlab2',
        'endereco':'jacareí2',
        'telefone':'12395546462',
        'telefone_emergencia':'012345672',
        'email':'quimlab@quimlab.com.br2',
    }
]

@auth_routes.route('/login', methods=["POST"])
def login():
    # request.json => para pegar as informacoes do corpo da requisicao
    # request.args => para pegar os parametros da url
    
    # validacao dos dados de entrada
    dados_recebido = request.json
    msg, status = validate_login(request.json)
    if not status:
        return msg, 400

    # processamento
    usuario_selecionado = None
    for user in USERS:
        if user['email'] == dados_recebido['email']:
            usuario_selecionado = user
            break

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404

    if user['password'] != dados_recebido['password']:
        return 'Senha Incorreta', 403
    
    # formatamos o retorno
    return {
        'messagem': f'Bem-Vindo, login realizado com Sucesso!',
        'email': dados_recebido['email']
    }

@auth_routes.route('/users', methods=['GET',])
def usuario():
    dados_recebido = request.args
    for usuario in USERS:
        if usuario['id'] == int(dados_recebido['id']):
            return usuario

@auth_routes.route('/users_todos', methods=['GET',])
def listausuario():
        return {
            'usuarios': USERS,
            }

@auth_routes.route('/user', methods=["DELETE"])
def user_deleted():
    dados_recebido = request.args
    msg, status = validate_user_id(dados_recebido)
    if not status:
        return msg, 400

    new_users = []
    for user in USERS:
        if user['id'] != int(dados_recebido['id']):
            new_users.append(user)

    return {
        'new_users_list': new_users
    }

@auth_routes.route('/user', methods=["PUT"])
def user_atualisa():
    dados_recebido_url = request.args
    msg, status = validate_user_id(dados_recebido_url)
    if not status:
        return msg, 400

    dados_recebido_corpo = request.json

    new_users = []
    for user in USERS:
        if int(dados_recebido_url['id']) == user['id']:
            if 'nome' in dados_recebido_corpo:
                user['name'] = dados_recebido_corpo['nome']

            if 'email' in dados_recebido_corpo:
                user['email'] = dados_recebido_corpo['email']

            if 'celular' in dados_recebido_corpo:
                user['celular'] = dados_recebido_corpo['celular']
        new_users.append(user)

    return {
        'new_users_list': new_users
    }

@auth_routes.route('/empresa', methods=["GET"])
def listaempresa():
        return {
            'empresas': EMPRESAS,
            }

@auth_routes.route('/novo_usuario', methods=["POST"])
def novousurario():
    dados_recebido_url = request.args
    msg, status = validate_t(dados_recebido_url)
    if not status:
        return msg, 400

    for user in USERS:
        if user['email'] == (dados_recebido_url['email']):
            return 'Usuário já cadastrado'

