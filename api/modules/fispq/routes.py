from flask import Blueprint, request
from Decorators import validate_token
from modules.fispq.validators import validate_f, validate_c
from modules.fispq.controllers import list_all_fispqs, update_fispq, delete_fispq, fispq_id, create_new_fispq, get_frases_by_onu



fispq_routes = Blueprint('fispq', __name__, url_prefix="/fispq")

@fispq_routes.route('/<id_fispq>', methods=['GET',])
@validate_token
def fispq(id_fispq):
    # dados_recebido = request.args
    dados_recebidos = request.user
    if dados_recebidos['permission_id'] != '1' and dados_recebidos['id'] != int(id_fispq):
        return 'Usuário não tem permissão', 403

    # msg, status = validate_user_id(dados_recebido)
    # if not status:
    #     return msg, 400

    fispq = fispq_id(id_fispq)
    return {
        'fispq':fispq 
    }

@fispq_routes.route('/', methods=['GET',])
@validate_token
def listafispq():
    dados_recebidos = request.user
    if dados_recebidos['permission_id'] != '1':
        return 'Usuário não tem permissão', 403
    
    new_fispqs = list_all_fispqs()

    return {
        'fispqs_list': new_fispqs
    }

@fispq_routes.route('/<id_fispq>', methods=["DELETE"])
@validate_token
def fispq_deleted_router(id_fispq):
    # dados_recebido_url = request.args
    dados_recebidos = request.user
    # dados_recebidos = request.json
    if dados_recebidos['permission_id'] != '1':
        return 'Usuário não tem permissão', 403

    msg, status_code = delete_fispq(id_fispq)
    if status_code > 300:
        return {
            "error": msg
        }, status_code

    return {
        "message": msg
    }, status_code


@fispq_routes.route('/', methods=["POST"])
@validate_token
def novafispq():
    dados_recebido = request.json
    dados_recebidos = request.user
    if dados_recebidos['permission_id'] != '1':
        return 'Usuário não tem permissão', 403

    msg, status = validate_f(dados_recebido)
    if not status:
        return msg, 400
    
    fispq = create_new_fispq(dados_recebido)

    return fispq
   
    # FISPQS = create_new_fispq(dados_recebido)

    # return FISPQS

# @fispq_routes.route('/comp/', methods=["POST"])
# @validate_token
# def novafispqcomp():
#     dados_recebido = request.json
#     dados_recebidos = request.user
#     if dados_recebidos['permission_id'] != '1':
#         return 'Usuário não tem permissão', 403

#     msg, status = validate_c(dados_recebido)
#     if not status:
#         return msg, 400
    
#     fispqcomp = create_new_fispq_comp(dados_recebido)

#     return fispqcomp
   
@fispq_routes.route('/<id_fispq>', methods=["PUT"])
@validate_token
def fispq_atualisa(id_fispq):
    dados_recebido_url = request.args
    dados_recebidos = request.user
    if dados_recebidos['permission_id'] != '1' and dados_recebidos['id'] != int(dados_recebido_url['id']):
        return 'Usuário não tem permissão', 403

    dados_recebido_corpo = request.json
    msg, status_code = update_fispq(id_fispq, dados_recebido_corpo)
    if status_code > 300:
            return {
                "error": msg
            }, status_code
        
    return {
        "message": msg
    }, status_code

# @fispq_routes.route('/frase_perigo', methods=['GET',])
# @validate_token



@fispq_routes.route('/frases_by_onu/<n_onu>', methods=['GET'])
@validate_token
def frases_by_onu(n_onu):
    resposta = get_frases_by_onu(n_onu)

    return resposta

    # def frase_perigo():
#     dados_recebidos = request.user
#     if dados_recebidos['permission_id'] != '1':
#         return 'Usuário não tem permissão', 403
    
#     frases_per = lista_frase_perigo()

#     return {
#         'frase_per_lista': frases_per
#     }

# @fispq_routes.route('/frase_banco', methods=['GET',])
# @validate_token
# def frase_banco():
#     dados_recebidos = request.user
#     if dados_recebidos['permission_id'] != '1':
#         return 'Usuário não tem permissão', 403

    # fispqbanco = fispq_banco
    # return {
    #     'fispqbanco':fispqbanco 
    # }