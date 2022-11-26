from flask import Blueprint, request
from Decorators import validate_token
from modules.user.validators import validate_t, validate_change_password
from modules.user.controllers import list_all_users, update_user, delete_user, get_user_id, create_new_user, change_password


user_routes = Blueprint('user', __name__, url_prefix="/user")



@user_routes.route('/<user_id>', methods=['GET',])
@validate_token
def usuario(user_id):
# def usuario():
    # dados_recebido = request.args
    dados_recebidos = request.user
    if dados_recebidos['permission_id'] != '1' and dados_recebidos['id'] != int(user_id):
    # if dados_recebidos['permission_id'] != '1' and dados_recebidos['id'] != int():
        return 'Usuário não tem permissão', 403

    # msg, status = validate_user_id(dados_recebido)
    # if not status:
    #     return msg, 400
    user = get_user_id(user_id)
    # user = get_user_id(dados_recebido["id"])
    return {
        'usuario':user 
    }

@user_routes.route('/', methods=['GET',])
@validate_token
def listausuario():
    dados_recebidos = request.user
    if dados_recebidos['permission_id'] != '1':
        return 'Usuário não tem permissão', 403
    
    new_users = list_all_users()

    return {
        'users_list': new_users
    }

@user_routes.route('/<id_user>', methods=["DELETE"])
@validate_token
def user_deleted(id_user):
    # dados_recebido_url = request.args
    dados_recebidos = request.user
    if dados_recebidos['permission_id'] != '1':
        return 'Usuário não tem permissão', 403

    msg, status_code = delete_user(id_user)
    if status_code > 300:
        return {
            "error": msg
        }, status_code

    return {
        "message": msg
    }, status_code

    # msg, status = validate_user_id(dados_recebido_url)
    # if not status:
    #     return msg, 400

    # new_users = delete_user(dados_recebido_url['id_user'])

    # return {
    #     'new_user_list':new_users
    # }

@user_routes.route('/', methods=["POST"])
@validate_token
def novousurario():
    dados_recebido = request.json
    dados_recebidos = request.user
    if dados_recebidos['permission_id'] != '1':
        return 'Usuário não tem permissão', 403

    msg, status = validate_t(dados_recebido)
    if not status:
        return msg, 400

    dados_recebido_corpo = request.json
    USERS = create_new_user(dados_recebido_corpo)

    return USERS
   
@user_routes.route('/<id_user>', methods=["PUT"])
@validate_token
def user_atualisa(id_user):
    dados_recebido_url = request.args
    dados_recebidos = request.user
    if dados_recebidos['permission_id'] != '1' and dados_recebidos['id'] != int(dados_recebido_url['id']):
        return 'Usuário não tem permissão', 403

    dados_recebido_corpo = request.json
    msg, status_code = update_user(id_user, dados_recebido_corpo)
    if status_code > 300:
            return {
                "error": msg
            }, status_code
        
    return {
        "message": msg
    }, status_code

@user_routes.route('/change_password/<user_id>', methods=["POST"])
@validate_token
def change_password_route(user_id):
    dados_recebidos = request.user
    if dados_recebidos['permission_id'] != '1' and dados_recebidos['id'] != int(user_id):
        return 'Usuário não tem permissão', 403

    dados_recebidos = request.json
    msg, status = validate_change_password(dados_recebidos)
    if not status:
        return msg, 400

    msg, status = change_password(user_id, dados_recebidos['password'])

    return msg, status
