# import jwt
# import pytz
from datetime import datetime
from dateutil.relativedelta import relativedelta
from database import mysql

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

def get_user_id(id):
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM User WHERE id = %s", [id])
    usuario_selecionado = cursor.fetchone()

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404

    user = {
        'id': usuario_selecionado[0],
        'name': usuario_selecionado[1],
        'email': usuario_selecionado[2],
        'celular': usuario_selecionado[3],
        'created_at': usuario_selecionado[5],
        'updated_at': usuario_selecionado[6],
        'permission_id': usuario_selecionado[7]
    }

    cursor.close()
    return user


def delete_user(id_user):
    cursor = mysql.get_db().cursor()

    # verificar se existe o usuario com o ID X no banco
    cursor.execute("SELECT * FROM User WHERE ID = %s", [id_user])
    usuario_selecionado = cursor.fetchone()

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404
    
    cursor.execute("DELETE FROM User WHERE ID = %s", [id_user])

    mysql.get_db().commit()

    cursor.close()
    
    return 'Usuário deletado com sucesso!', 200

def update_user(id, dados_recebido_corpo):
    cursor = mysql.get_db().cursor()

    # verificar se existe o usuario com o ID X no banco
    cursor.execute("SELECT * FROM User WHERE id = %s", [id])
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

def create_new_user(dados_recebido):

    # instancia o banco de dados
    cursor = mysql.get_db().cursor()

    # Pega as informações do banco de dados
    name = dados_recebido['name']
    email = dados_recebido['email']
    celular = dados_recebido ['celular']
    password = dados_recebido['password']
    permission_id = dados_recebido ['permission_id']

    # cria o SQL
    cursor.execute("SELECT * FROM User WHERE email = %s", [email])
    user = cursor.fetchone()
    if user:
        return 'Usuário já existe no banco de dados', 409

    # insere as insformações no banco de dados
    cursor.execute("INSERT INTO User (name, email, celular, password, permission_id) VALUES (%s, %s, %s, %s, %s)", 
        [name, email, celular, password, permission_id])

    mysql.get_db().commit()

    #fecha a instancia do banco de dados
    cursor.close()

    return 'Usuário cadastrado com sucesso', 201

def change_password(user_id, new_password):
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM User WHERE id = %s", [user_id])
    user = cursor.fetchone()
    if not user:
        return 'Usuário não encontrado!', 404

    cursor.execute("UPDATE User SET password = %s WHERE id = %s", 
        [new_password, user_id])

    mysql.get_db().commit()

    cursor.close()

    return 'Senha alterada com sucesso!', 200
