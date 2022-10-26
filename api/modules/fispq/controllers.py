# import jwt
# import pytz
from datetime import datetime
from dateutil.relativedelta import relativedelta
from database import mysql

def list_all_fispqs():
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Fispq")

    fispqs_db = cursor.fetchall()

    all_fispqs = []

    for fispq in fispqs_db:
        new_fispq = {
            'id_Fispq': fispq[0],
            'produto': fispq[1],
            'onu': fispq[46],
            'nome_embarque': fispq[47],
            'created_at': fispq[48],
            'update_at': fispq[49],
            
        }

        all_fispqs.append(new_fispq)

    cursor.close()

    return all_fispqs

def fispq_id(id):
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Fispq WHERE id = %s", [id])
    fispq_selecionado = cursor.fetchone()

    if not fispq_selecionado:
        return 'Fispq não encontrada', 404

    fispq = {
        'id_Fispq': fispq[0],
        'produto': fispq[1],
        'onu': fispq[46],
        'nome_embarque': fispq[47],
        'created_at': fispq[48],
        'update_at': fispq[49],
    }

    cursor.close()
    return fispq


def delete_fispq(id_fispq):
    cursor = mysql.get_db().cursor()

    # verificar se existe o usuario com o ID X no banco
    cursor.execute("SELECT * FROM Fispq WHERE ID = %s", [id_fispq])
    fispq_selecionado = cursor.fetchone()

    if not fispq_selecionado:
        return 'Fispq não encontrada', 404
    
    cursor.execute("DELETE FROM Fispq WHERE ID = %s", [id_fispq])

    mysql.get_db().commit()

    cursor.close()
    
    return 'Fispq deletada com sucesso!', 200

def update_fispq(id, dados_recebido_corpo):
    cursor = mysql.get_db().cursor()

    # verificar se existe o usuario com o ID X no banco
    cursor.execute("SELECT * FROM Fispq WHERE ID = %s", [id])
    fispq_selecionado = cursor.fetchone()

    if not fispq_selecionado:
        return 'Fispq não encontrada', 404

    # organizar as novas informacoes
    novo_nome = dados_recebido_corpo['name']
    novo_email = dados_recebido_corpo['email']
    novo_celular = dados_recebido_corpo['celular']
    data_atual = datetime.now()

    # atualizar no banco de dados com as novas informacoes para o usuario
    cursor.execute("UPDATE Fispq SET name = %s, email = %s, celular = %s, update_at = %s WHERE ID = %s", 
        [novo_nome, novo_email, novo_celular, data_atual, id])
    
    mysql.get_db().commit()

    cursor.close()

    return 'Fispq atualizada com sucesso!', 200

def create_new_fispq(dados_recebido):

    # instancia o banco de dados
    cursor = mysql.get_db().cursor()

    # Pega as informações do banco de dados
    name = dados_recebido['name']
    email = dados_recebido['email']
    celular = dados_recebido ['celular']
    password = dados_recebido['password']
    permission_id = dados_recebido ['permission_id']

    # cria o SQL
    cursor.execute("SELECT * FROM Fispq WHERE email = %s", [email])
    fispq = cursor.fetchone()
    if fispq:
        return 'Fispq já existe no banco de dados', 409

    # insere as insformações no banco de dados
    cursor.execute("INSERT INTO Fispq (name, email, celular, password, permission_id) VALUES (%s, %s, %s, %s, %s)", 
        [name, email, celular, password, permission_id])

    mysql.get_db().commit()

    #fecha a instancia do banco de dados
    cursor.close()

    return 'Fispq cadastrada com sucesso', 201