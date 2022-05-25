from datetime import datetime
from database import mysql

def login(dados_recebido):
        
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM User WHERE email = %s", [dados_recebido['email']])
    usuario_selecionado = cursor.fetchone()

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404

    if usuario_selecionado[4] != dados_recebido['password']:
        return 'Senha Incorreta', 403

    cursor.close()

    return '', 200


def list_all_users():
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM User")

    users_db = cursor.fetchall()

    all_users = []

    for user in users_db:
        new_user = {
            'id': user[0],
            'name': user[1],
            'email': user[2],
            'celular': user[3],
            'created_at': user[5],
            'update_at': user[6],
            'permission_id': user[7]
        }

        all_users.append(new_user)

    cursor.close()

    return all_users

def user_id(id):
    cursor = mysql.get_db().cursor()

    # verificar se existe o usuario com o ID X no banco
    cursor.execute("SELECT * FROM User WHERE ID = %s", [id])
    usuario_selecionado = cursor.fetchone()

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404
    
    return usuario_selecionado

def delete_user(id):
    cursor = mysql.get_db().cursor()

    # verificar se existe o usuario com o ID X no banco
    cursor.execute("SELECT * FROM User WHERE ID = %s", [id])
    usuario_selecionado = cursor.fetchone()

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404
    
    cursor.execute("DELETE FROM User WHERE ID = %s", [id])

    mysql.get_db().commit()

    cursor.close()
    
    return 'Usuário deletado com sucesso!', 200

def update_user(id, dados_recebido_corpo):
    cursor = mysql.get_db().cursor()

    # verificar se existe o usuario com o ID X no banco
    cursor.execute("SELECT * FROM User WHERE ID = %s", [id])
    usuario_selecionado = cursor.fetchone()

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404

    # organizar as novas informacoes
    novo_nome = dados_recebido_corpo['name']
    novo_email = dados_recebido_corpo['email']
    novo_celular = dados_recebido_corpo['celular']
    data_atual = datetime.now()

    # atualizar no banco de dados com as novas informacoes para o usuario
    cursor.execute("UPDATE User SET name = %s, email = %s, celular = %s, update_at = %s WHERE ID = %s", 
        [novo_nome, novo_email, novo_celular, data_atual, id])
    
    mysql.get_db().commit()

    cursor.close()

    return 'Usuário atualizado com sucesso!', 200

# def create_new_user(dados_recebido):
#     for user in USERS:
#         if user['email'] == (dados_recebido['email']):
#             return 'Usuário já cadastrado',409

#     USERS.append(dados_recebido)
#     return {
#         'new_list':USERS
#     }