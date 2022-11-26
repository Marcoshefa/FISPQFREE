def validate_t(dados_recebidos):
    if not dados_recebidos.get('email'):
        return 'e-mail obrigatorio!', False

    if not dados_recebidos.get('password'):
        return 'Password obrigatorio!', False

    if not dados_recebidos.get('name'):
        return 'name obrigatorio!', False

    return '', True

def validate_user_id(dados_recebidos_url):
    if not dados_recebidos_url.get('id'):
        return 'ID obrigatorio!', False

    return '', True

def validate_change_password(dados_recebido):
    if not dados_recebido.get('password'):
        return 'A senha é obrigatória', False

    elif len(dados_recebido['password']) < 8:
        return 'A senha precisa de no minimo 8 caracteres', False
    
    return '', True