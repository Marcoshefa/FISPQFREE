from flask import Blueprint, request

from modules.auth.validator import validate_login
from modules.auth.validator import validate_user_id
from modules.auth.validator import validate_t
from modules.auth.controllers import login, list_all_users, user_id, delete_user, update_users, create_new_user

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/login', methods=["POST"])
def login_route():
    # request.json => para pegar as informacoes do corpo da requisicao
    # request.args => para pegar os parametros da url
    
    # validacao dos dados de entrada
    dados_recebido = request.json
    msg, status = validate_login(request.json)
    if not status:
        return msg, 400

    # processamento
    msg, status = login(dados_recebido)
    if status>= 400:
        return msg, status
    
    # formatamos o retorno
    return {
        'messagem': f'Bem-Vindo, login realizado com Sucesso!',
        'email': dados_recebido['email']
    }

@auth_routes.route('/users', methods=['GET',])
def usuario():
    dados_recebido = request.args
    msg, status = validate_user_id(dados_recebido)
    if not status:
        return msg, 400

    usuario = user_id(dados_recebido['id'])
    if not usuario:
       return 'Usuário não encontrado!', 404

    return usuario

@auth_routes.route('/users_todos', methods=['GET',])
def listausuario():
    new_users = list_all_users()

    return {
        'users_list': new_users
    }

@auth_routes.route('/user', methods=["DELETE"])
def user_deleted():
    dados_recebido = request.args
    msg, status = validate_user_id(dados_recebido)
    if not status:
        return msg, 400

    new_users = delete_user(dados_recebido['id'])

    return {
        'new_user_list':new_users
    }

@auth_routes.route('/user', methods=["PUT"])
def user_atualisa():
    dados_recebido_url = request.args
    msg, status = validate_user_id(dados_recebido_url)
    if not status:
        return msg, 400

    dados_recebido_corpo = request.json
    new_users = update_users(dados_recebido_url['id'], dados_recebido_corpo)

    return {'new_users_list': new_users}

#@auth_routes.route('/empresa', methods=["GET"])
#def listaempresa():
        #return {
            #'empresas': EMPRESAS,
            #}

@auth_routes.route('/novo_usuario', methods=["POST"])
def novousurario():
    dados_recebido = request.json
    msg, status = validate_t(dados_recebido)
    if not status:
        return msg, 400

    dados_recebido_corpo = request.json
    USERS = create_new_user(dados_recebido_corpo)

    return USERS
   
    
    

