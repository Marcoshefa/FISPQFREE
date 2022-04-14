def validate_login(dados_recebidos):
    if not dados_recebidos.get('email'):
        return 'E-mail obrigatorio!', False

    if not dados_recebidos.get('password'):
        return 'Password obrigatorio!', False

    return '', True