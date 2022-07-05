from flask import Blueprint, request

from modules.auth.validator import validate_login, validate_empresa, validate_cnpj,validate_user_id, validate_t, validate_usuarioempresa, validate_user_company
from modules.auth.controllers import login, list_all_users, update_user, delete_user, user_id, create_new_user, create_new_company, empresa_cnpj, list_all_company, delete_company, update_company, create_new_usercompany, list_permission, delele_access
from Decorators import validate_token

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
        'message': f'Bem-Vindo, login realizado com Sucesso!',
        'email': dados_recebido['email'],
        "token": msg
    }

@auth_routes.route('/users', methods=['GET',])
@validate_token
def usuario():
    dados_recebido = request.args
    dados_recebidos = request.user
    if dados_recebidos['permission_id'] != '1' and dados_recebidos['id'] != int(dados_recebido['id']):
        return 'Usuário não tem permissão', 403

    msg, status = validate_user_id(dados_recebido)
    if not status:
        return msg, 400

    user = user_id(dados_recebido['id'])
    return {
        'usuario':user 
    }

@auth_routes.route('/users_all', methods=['GET',])
@validate_token
def listausuario():
    dados_recebidos = request.user
    if dados_recebidos['permission_id'] != '1':
        return 'Usuário não tem permissão', 403
    
    new_users = list_all_users()

    return {
        'users_list': new_users
    }

@auth_routes.route('/user', methods=["DELETE"])
@validate_token
def user_deleted():
    dados_recebido_url = request.args
    dados_recebidos = request.user
    if dados_recebidos['permission_id'] != '1':
        return 'Usuário não tem permissão', 403

    msg, status = validate_user_id(dados_recebido_url)
    if not status:
        return msg, 400

    new_users = delete_user(dados_recebido_url['id'])

    return {
        'new_user_list':new_users
    }

@auth_routes.route('/novo_usuario', methods=["POST"])
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
   
@auth_routes.route('/user', methods=["PUT"])
@validate_token
def user_atualisa():
    dados_recebido_url = request.args
    dados_recebidos = request.user
    if dados_recebidos['permission_id'] != '1' and dados_recebidos['id'] != int(dados_recebido_url['id']):
        return 'Usuário não tem permissão', 403

    msg, status = validate_user_id(dados_recebido_url)
    if not status:
        return msg, 400

    dados_recebido_corpo = request.json
    new_users = update_user(dados_recebido_url['id'], dados_recebido_corpo)

    return {'new_users_list': new_users}  
    
@auth_routes.route('/nova_empresa', methods=["POST"])
@validate_token
def novaempresa():
    dados_recebido = request.json
    dados_recebidos_token = request.user
    if dados_recebidos_token['permission_id'] != '1':
        return 'Usuário não tem permissão', 403

    msg, status = validate_empresa(dados_recebido)
    if not status:
        return msg, 400

    dados_recebido_corpo = request.json
    EMPRESA = create_new_company(dados_recebido_corpo)

    return EMPRESA

@auth_routes.route('/company', methods=['GET',])
@validate_token
def empresa():
    dados_recebido = request.args
    msg, status = validate_cnpj(dados_recebido)
    if not status:
        return msg, 400

    company_cnpj = empresa_cnpj(dados_recebido['cnpj'])
    return {
        'Empresa':company_cnpj
    }

@auth_routes.route('/company_all', methods=['GET',])
@validate_token
def listaempresas():
    dados_recebidos_token = request.user
    if dados_recebidos_token['permission_id'] != '1':
        return 'Usuário não tem permissão', 403

    list_company = list_all_company()

    return {
        'company_list': list_company
    }

@auth_routes.route('/company', methods=["DELETE"])
@validate_token
def company_deleted():
    dados_recebido = request.args
    dados_recebidos_token = request.user
    if dados_recebidos_token['permission_id'] != '1':
        return 'Usuário não tem permissão', 403

    msg, status = validate_cnpj(dados_recebido)
    if not status:
        return msg, 400

    delete_empresa = delete_company()

    return {
        'new_company_list':delete_empresa
    }

@auth_routes.route('/company', methods=["PUT"])
@validate_token
def company_atualisa():
    dados_recebido_url = request.args
    dados_recebidos_token = request.user
    if dados_recebidos_token['permission_id'] != '1':
        return 'Usuário não tem permissão', 403

    msg, status = validate_cnpj(dados_recebido_url)
    if not status:
        return msg, 400

    dados_recebido_corpo = request.json
    new_company = update_company(dados_recebido_url['cnpj'], dados_recebido_corpo)

    return {'new_company_list': new_company}

@auth_routes.route('/user_company', methods=["POST"])
@validate_token
def usuarioempresa():
    dados_recebido = request.json
    dados_recebidos_token = request.user
    if dados_recebidos_token['permission_id'] != '1':
        return 'Usuário não tem permissão', 403

    msg, status = validate_usuarioempresa(dados_recebido)
    if not status:
        return msg, 400

    if dados_recebido['User_ID'] == dados_recebidos_token['id']:
    #and dados_recebido['Empresa_ID_empresa'] == dados_recebidos_token['Empresa_ID_empresa']:
        return 'Permissão de usuário e empresa já cadastrado', 403

    dados_recebido_corpo = request.json
    USUARIOEMPRESA = create_new_usercompany(dados_recebido_corpo)

    return USUARIOEMPRESA

@auth_routes.route('/user_company_all', methods=['GET',])
@validate_token
def lista_empresas():
    dados_recebido = request.args
    dados_recebidos_token = request.user
        
    msg, status = validate_user_id(dados_recebido)
    if not status:
        return msg, 400

    if dados_recebidos_token['permission_id'] != '1' and dados_recebidos_token['id'] != int(dados_recebido['id']):
        return 'Usuário não tem permissão', 403

    list_user_company_all = list_permission(dados_recebido['id'])

    return {
        'user_company_list': list_user_company_all
    }

# @auth_routes.route('/create_permission', methods=['POST',])
# @validate_token
# def createpermission():
#     dados_recebido = request.args
#     dados_recebidos = request.user
#     if dados_recebidos['permission_id'] != '1':
#         return 'Usuário não tem permissão', 403

#     msg, status = validate_user_id(dados_recebido)
#     if not status:
#         return msg, 400

#     user = list_permission()
#     return {
#         'usuario':user 
#     }

@auth_routes.route('/delete_permission', methods=["DELETE"])
@validate_token
def delete_permission():
    dados_recebido = request.json
    dados_recebidos_token = request.user
    if dados_recebidos_token['permission_id'] != '1':
        return 'Usuário não tem permissão', 403

    msg, status = validate_user_company(dados_recebido)
    if not status:
        return msg, 400

    delete_permission = delele_access(dados_recebido)

    return {
        'new_company_list':delete_permission
    }