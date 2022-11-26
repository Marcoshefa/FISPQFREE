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
            'idFispq': fispq[0],
            'produto': fispq[5],
            'onu': fispq[69],
            'nome_embarque': fispq[70],
            'created_at': fispq[1],
            'update_at': fispq[2],
            
        }

        all_fispqs.append(new_fispq)

    cursor.close()

    return all_fispqs

def fispq_id(id):
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Fispq WHERE idFispq = %s", [id])
    fispq_selecionada = cursor.fetchone()

    if not fispq_selecionada:
        return 'Fispq não encontrada', 404

    fispq = {
        'idFispq': fispq_selecionada[0],
        'produto': fispq_selecionada[5],
        'onu': fispq_selecionada[69],
        'nome_embarque': fispq_selecionada[70],
        'created_at': fispq_selecionada[1],
        'update_at': fispq_selecionada[2],
    }

    cursor.close()
    return fispq


def delete_fispq(id_fispq):
    cursor = mysql.get_db().cursor()

    # verificar se existe o usuario com o ID X no banco
    cursor.execute("SELECT * FROM Fispq WHERE idFispq = %s", [id_fispq])
    fispq_selecionado = cursor.fetchone()

    if not fispq_selecionado:
        return 'Fispq não encontrada', 404
    
    cursor.execute("DELETE FROM Fispq WHERE idFispq = %s", [id_fispq])

    mysql.get_db().commit()

    cursor.close()
    
    return 'Fispq deletada com sucesso!', 200

def update_fispq(id, dados_recebido_corpo):
    cursor = mysql.get_db().cursor()

    # verificar se existe o usuario com o ID X no banco
    cursor.execute("SELECT * FROM Fispq WHERE idFispq = %s", [id])
    fispq_selecionado = cursor.fetchone()

    if not fispq_selecionado:
        return 'Fispq não encontrada', 404

    # organizar as novas informacoes
    novo_produto = dados_recebido_corpo['produto']
    novo_onu = dados_recebido_corpo['onu']
    novo_nome_embarque = dados_recebido_corpo['nome_embarque']
    data_atual = datetime.now()

        #     'id_Fispq': fispq[0],
        # 'produto': fispq[1],
        # 'onu': fispq[46],
        # 'nome_embarque': fispq[47],
        # 'created_at': fispq[48],
        # 'update_at': fispq[49],

    # atualizar no banco de dados com as novas informacoes para o usuario
    cursor.execute("UPDATE Fispq SET produto = %s, onu = %s, nome_embarque = %s, update_at = %s WHERE idFispq = %s", 
        [novo_produto, novo_onu, novo_nome_embarque, data_atual, id])
    
    mysql.get_db().commit()

    cursor.close()

    return 'Fispq atualizada com sucesso!', 200

def create_new_fispq(dados_recebido):

    # instancia o banco de dados
    cursor = mysql.get_db().cursor()

    # Pega as informações do banco de dados
    cod_int = dados_recebido['cod_int']
    produto = dados_recebido['produto']
    uso = dados_recebido['uso']
    onu = dados_recebido['onu']

    # onu = dados_recebido.get('onu')
    # nome_embarque = dados_recebido.get('nome_embarque')

    # cria o SQL
    cursor.execute("SELECT * FROM Fispq WHERE cod_int = %s", [cod_int])
    fispq = cursor.fetchone()
    if fispq:
        return 'Fispq já existe no banco de dados', 409

    # insere as insformações no banco de dados
    cursor.execute("INSERT INTO Fispq (cod_int, produto, uso, onu) VALUES (%s, %s, %s, %s)", 
        [cod_int, produto, uso, onu])

    mysql.get_db().commit()

    #fecha a instancia do banco de dados
    cursor.close()

    return 'Fispq cadastrada com sucesso', 201