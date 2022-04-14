from datetime import datetime
from flask import Blueprint, request

from modules.auth.validator import validate_login

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
        'password': 123456,
        'created_at': datetime(2022, 5, 1, 12, 0),
        'updated_at': datetime(2022, 5, 1, 12, 0),
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