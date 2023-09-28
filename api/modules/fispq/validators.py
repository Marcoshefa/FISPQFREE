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

def validate_f(dados_recebidos):
    if not dados_recebidos.get('cod_int'):
        return 'Código interno é Obrigatório', False
    
    if not dados_recebidos.get('produto'):
        return 'Nome da substância ou produto é Obrigatório', False
    
    if not dados_recebidos.get('todas_frases_classificacao'):
        return 'CLASSIFICAÇÃO DE PERIGO é Obrigatório', False
    return '', True

def validate_c(dados_recebidos):
    if not dados_recebidos.get('cod_int_comp'):
        return 'Código interno é Obrigatório', False
    return '', True
