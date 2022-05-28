def validate_login(dados_recebidos):
    if not dados_recebidos.get('email'):
        return 'E-mail obrigatorio!', False

    if not dados_recebidos.get('password'):
        return 'Password obrigatorio!', False

    return '', True

def validate_user_id(dados_recebidos):
    if not dados_recebidos.get('id'):
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