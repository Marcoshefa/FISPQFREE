from datetime import datetime

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
        'password': '123456',
        'created_at': datetime(2022, 5, 1, 12, 0),
        'updated_at': datetime(2022, 5, 1, 12, 0),
    }
]

EMPRESAS = [
    {
        'ID_empresa': 1,
        'nome':'Quimlab',
        'endereco':'jacareí',
        'telefone':'1239554646',
        'telefone_emergencia':'01234567',
        'email':'quimlab@quimlab.com.br',
    },
    {
        'ID_empresa': 2,
        'nome':'Quimlab2',
        'endereco':'jacareí2',
        'telefone':'12395546462',
        'telefone_emergencia':'012345672',
        'email':'quimlab@quimlab.com.br2',
    }
]

def login(dados_recebido):
        
    usuario_selecionado = None
    for user in USERS:
        if user['email'] == dados_recebido['email']:
            usuario_selecionado = user
            break

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404

    if user['password'] != dados_recebido['password']:
        return 'Senha Incorreta', 403

    return '', 200

def list_all_users():
    new_users = []

    for user in USERS:
        new_user = user
        del new_user['password']
        new_users.append(new_user)

    return new_users

def user_id(id):
    for usuario in USERS:
        if int(id) == usuario['id']:
            del usuario['password']
            return usuario

    return None

def delete_user(id):
    new_users = []
    for user in USERS:
        if user['id'] != int(id):
            new_users.append(user)

    return new_users

def update_users(id, dados_recebido_corpo):
    new_users = []
    for user in USERS:
        if int(id) == user['id']:
            if 'nome' in dados_recebido_corpo:
                user['name'] = dados_recebido_corpo['nome']

            if 'email' in dados_recebido_corpo:
                user['email'] = dados_recebido_corpo['email']

            if 'celular' in dados_recebido_corpo:
                user['celular'] = dados_recebido_corpo['celular']
        new_users.append(user)

    return new_users

def create_new_user(dados_recebido):
    for user in USERS:
        if user['email'] == (dados_recebido['email']):
            return 'Usuário já cadastrado',409

    new_users = []
    USERS.append(dados_recebido)
    return {
        'new_list':USERS
    }