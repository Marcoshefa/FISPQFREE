import jwt
import pytz
from datetime import datetime
from dateutil.relativedelta import relativedelta
from database import mysql

def login(dados_recebido):
        
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM User WHERE email = %s", [dados_recebido['email']])
    usuario_selecionado = cursor.fetchone()
    
    if not usuario_selecionado:
        return 'Usuário não encontrado', None, 404

    # cursor.execute("SELECT Empresa_ID_empresa FROM User_has_Empresa WHERE User_ID = %s", usuario_selecionado[0])
    # empresa_selecionada = cursor.fetchall()


    if usuario_selecionado[4] != dados_recebido['password']:
        return 'Senha Incorreta', usuario_selecionado[0], 403

    data_hora_atual = datetime.now(tz=pytz.timezone('America/Sao_Paulo'))
    dados = {
        'id': usuario_selecionado[0],
        'name': usuario_selecionado[1],
        'permission_id': usuario_selecionado[7],
        'iat': data_hora_atual,
        'exp': data_hora_atual + relativedelta(years=1),
        # 'idcompany':empresa_selecionada[0]
    }

    token = jwt.encode(dados, "SENHA_TOKEN", algorithm="HS256")
    cursor.close()

    return token, usuario_selecionado[0], 200


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

def create_new_company(dados_recebido):
    cursor = mysql.get_db().cursor()

    nome = dados_recebido['nome']
    endereco = dados_recebido['endereco']
    telefone = dados_recebido['telefone']
    telefone_emergencia = dados_recebido['telefone_emergencia']
    email = dados_recebido['email']
    cnpj = dados_recebido['cnpj']

    cursor.execute("SELECT * FROM Empresa WHERE cnpj = %s", [cnpj])
    user = cursor.fetchone()
    if user:
        return 'Empresa já existe no banco de dados', 409

    cursor.execute("INSERT INTO Empresa (nome, endereco, telefone, telefone_emergencia, email, cnpj) VALUES (%s, %s, %s, %s, %s,%s)", 
        [nome, endereco, telefone, telefone_emergencia, email, cnpj])

    mysql.get_db().commit()

    cursor.close()

    return 'Empresa cadastrada com sucesso', 201

def empresa_cnpj(cnpj):
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Empresa WHERE cnpj = %s", [cnpj])
    empresa_selecionada = cursor.fetchone()

    if not empresa_selecionada:
        return 'Empresa não encontrada', 404

    empresa = {
        'nome': empresa_selecionada[0],
        'endereco': empresa_selecionada[1],
        'telefone': empresa_selecionada[2],
        'telefone_emergencia': empresa_selecionada[3],
        'email': empresa_selecionada[4],
        'cnpj': empresa_selecionada[5],
    }

    cursor.close()
    return empresa

def list_all_company():
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Empresa")

    empresa_db = cursor.fetchall()

    all_company = []

    for empresa in empresa_db:
        new_empresa = {
        'nome': empresa[1],
        'endereco': empresa[2],
        'telefone': empresa[3],
        'telefone_emergencia': empresa[4],
        'email': empresa[5],
        'cnpj': empresa[6],
        }

        all_company.append(new_empresa)

    cursor.close()

    return all_company

def delete_company(cnpj):
    cursor = mysql.get_db().cursor()

    # verificar se existe o usuario com o cnpj X no banco
    cursor.execute("SELECT * FROM Empresa WHERE cnpj = %s", [cnpj])
    empresa_selecionada = cursor.fetchone()

    if not empresa_selecionada:
        return 'Empresa não encontrado', 404
    
    cursor.execute("DELETE FROM Empresa WHERE cnpj = %s", [cnpj])

    mysql.get_db().commit()

    cursor.close()
    
    return 'Empresa deletada com sucesso!', 200

def update_company(cnpj, dados_recebido_corpo):
    cursor = mysql.get_db().cursor()

    # verificar se existe a empresa com o cnpj X no banco
    cursor.execute("SELECT * FROM Empresa WHERE cnpj = %s", [cnpj])
    empresa_selecionada = cursor.fetchone()

    if not empresa_selecionada:
        return 'Empresa não encontrada', 404

    # organizar as novas informacoes
    novo_nome = dados_recebido_corpo['nome']
    novo_endereco = dados_recebido_corpo['endereco']
    novo_telefone = dados_recebido_corpo['telefone']
    novo_telefone_emergencia = dados_recebido_corpo['telefone_emergencia']
    novo_email = dados_recebido_corpo['email']
    

    # atualizar no banco de dados com as novas informacoes para a empresa
    cursor.execute("UPDATE Empresa SET nome = %s, endereco = %s, telefone = %s, telefone_emergencia = %s, email = %s WHERE cnpj = %s", 
        [novo_nome, novo_endereco, novo_telefone, novo_telefone_emergencia, novo_email, cnpj])
    
    mysql.get_db().commit()

    cursor.close()

    return 'Empresa atualizado com sucesso!', 200

def create_new_usercompany(dados_recebido):
    cursor = mysql.get_db().cursor()

    userID= dados_recebido['User_ID']
    empresaID = dados_recebido['Empresa_ID_empresa']

    # cursor.execute("SELECT * FROM User_has_Empresa WHERE User_ID = %s", and [userID])
    # user = cursor.fetchone()
    # if user:
    #     return 'Permissão de usuário e ampresa já existe no banco de dados', 409

    cursor.execute("INSERT INTO User_has_Empresa(User_ID, Empresa_ID_empresa) VALUES (%s, %s)", 
        [userID, empresaID])

    mysql.get_db().commit()

    cursor.close()

    return 'Permissão do usuário e empresa cadastrada com sucesso', 201

def list_permission(id):
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT Empresa_ID_empresa FROM User_has_Empresa WHERE User_ID = %s",[id]) 

    usuario_empresa = cursor.fetchall()

    if not usuario_empresa:
        return 'Usuário não encontrado', 404
    all_company = []

    for empresa in usuario_empresa:
        new_empresa = {
        'id_empresa': empresa[0],
        }

        all_company.append(new_empresa)

    cursor.close()

    return all_company

def delele_access(dados_recebido):
    cursor = mysql.get_db().cursor()

    id = dados_recebido['User_ID']
    empresa = dados_recebido['id_company']

    # verificar se existe o usuario com o cnpj X no banco
    cursor.execute("SELECT * FROM User_has_Empresa WHERE User_ID = %s and Empresa_ID_empresa = %s", [id, empresa])
    empresa_selecionada = cursor.fetchone()
   

    if not empresa_selecionada:
        return 'Empresa não encontrado', 404
    
    cursor.execute("DELETE FROM User_has_Empresa WHERE User_ID = %s and Empresa_ID_empresa = %s", [id, empresa])

    mysql.get_db().commit()

    cursor.close()
    
    return 'Empresa deletada com sucesso!', 200
