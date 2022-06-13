def validate_login(dados_recebidos):
    if not dados_recebidos.get('email'):
        return 'E-mail obrigatorio!', False

    if not dados_recebidos.get('password'):
        return 'Password obrigatorio!', False

    return '', True

def validate_user_id(dados_recebidos_url):
    if not dados_recebidos_url.get('id'):
        return 'ID obrigatorio!', False

    return '', True

def validate_t(dados_recebidos):
    if not dados_recebidos.get('email'):
        return 'e-mail obrigatorio!', False

    if not dados_recebidos.get('password'):
        return 'Password obrigatorio!', False

    if not dados_recebidos.get('name'):
        return 'name obrigatorio!', False

    return '', True

def validate_empresa(dados_recebidos):
    if not dados_recebidos.get('cnpj'):
        return 'CNPJ obrigatorio!', False

    return '', True

def validate_cnpj(dados_recebidos):
    if not dados_recebidos.get('cnpj'):
        return 'CNPJ obrigatório!', False

    return '', True

def validate_usuarioempresa(dados_recebidos):
    if not dados_recebidos.get('User_ID'):
        return 'User_ID obrigatorio!', False

    if not dados_recebidos.get('Empresa_ID_empresa'):
        return 'Empresa_ID_empresa obrigatorio!', False

    return '', True

# def validate_permission(dados_recebidos):
#     if not dados_recebidos.get('user_id'):
#         return 'user_id obrigatorio!', False

#     if not dados_recebidos.get('empresa_id'):
#         return 'empresa_id obrigatorio!', False

#     return '', True

def validate_user_company(dados_recebido):
    if not dados_recebido.get('User_ID'):
        return 'user_id obrigatorio!', False

    if not dados_recebido.get('id_company'):
        return 'empresa_id obrigatorio!', False

    return '', True