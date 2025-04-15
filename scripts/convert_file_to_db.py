
from numpy import var
import pandas as pd
from flaskext.mysql import MySQL

from flask import Flask

app = Flask(__name__)


app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Marcos21111984!'
app.config['MYSQL_DATABASE_DB'] = 'db_fispq'

# app.config['MYSQL_DATABASE_HOST'] = 'fispqfree.com.br'
# app.config['MYSQL_DATABASE_PORT'] = 3306
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'serverdb'
# app.config['MYSQL_DATABASE_DB'] = 'DB_FISPQ'

mysql = MySQL()
mysql.init_app(app)

# with app.app_context():
#     cursor = mysql.get_db().cursor()
#     file_path = '/home/marcos/Desktop/FISPQ/FISPQFREE/scripts/arquivos_example/frases_perigo.xlsx'
#     # file_path = 'C:/Users/adrie/OneDrive/Documentos/Beto/toroinvestimentos/pessoal/projects/float-academy/github/float_news/scripts/arquivos_example/teste.xlsx'
#     arquivo = pd.read_excel(file_path, sheet_name='Sheet1')

#     # pegar os headers da planilha
#     print(arquivo.columns)
#     # pegar os valores da planilha
#     print(arquivo.values)

#     values = arquivo.values

#     for linha in values:
#         # for coluna in arquivo.columns:
#             cursor.execute("INSERT INTO Frases_perigo (codigo, frases_perigo) VALUES (%s, %s)", [linha[0], linha[1]])
#             mysql.get_db().commit()

#     cursor.close()

# with app.app_context():
#     cursor = mysql.get_db().cursor()
#     file_path = '/home/marcos/Desktop/FISPQ/FISPQFREE/scripts/arquivos_example/Tab_ONU_nome_aprop_IATA.xlsx'
#     arquivo = pd.read_excel(file_path, sheet_name='Sheet1')

#     # pegar os headers da planilha
#     print(arquivo.columns)
#     # pegar os valores da planilha
#     print(arquivo.values)

#     values = arquivo.values

#     for linha in values:
#         # for coluna in arquivo.columns:
#             cursor.execute("INSERT INTO Tab_nome_aprop_aereo(N_ONU_A, N_Guia_a, Nome_aprop_a) VALUES (%s, %s, %s)", [linha[0], linha[1], linha[2]])
#             mysql.get_db().commit()

#     cursor.close()

with app.app_context():
    cursor = mysql.get_db().cursor()
    file_path = '/home/marcos/Desktop/FISPQ/FISPQFREE/scripts/arquivos_example/Tab_ONU_nome_aprop_IMDG.xlsx'
    arquivo = pd.read_excel(file_path, sheet_name='Sheet1')

    # pegar os headers da planilha
    print(arquivo.columns)
    # pegar os valores da planilha
    print(arquivo.values)

    values = arquivo.values

    for linha in values:
        # for coluna in arquivo.columns:
            cursor.execute("INSERT INTO Tab_nome_aprop_hidroviario(N_ONU_H, N_Guia_h, Nome_aprop_h) VALUES (%s, %s, %s)", [linha[0], linha[1], linha[2]])
            mysql.get_db().commit()

    cursor.close()


# with app.app_context():
#     cursor = mysql.get_db().cursor()
#     file_path = '/home/marcos/Desktop/FISPQ/FISPQFREE/scripts/arquivos_example/Tab_frase_precaucao.xlsx'
#     arquivo = pd.read_excel(file_path, sheet_name='Sheet1')

#     # pegar os headers da planilha
#     print(arquivo.columns)
#     # pegar os valores da planilha
#     print(arquivo.values)

#     values = arquivo.values

#     for linha in values:
#             cursor.execute("INSERT INTO Tab_frase_precaucao (cod_precaucao, frase_precaucao) VALUES (%s, %s)", [linha[0], linha[1]])
#             mysql.get_db().commit()

#     cursor.close()



# Script para inserir a tabela Tab_info
# with app.app_context():
#     cursor = mysql.get_db().cursor()
#     file_path = '/home/marcos/Desktop/FISPQ/FISPQFREE/scripts/arquivos_example/Tab_info.xlsx'
   
#     arquivo = pd.read_excel(file_path, sheet_name='Sheet1')

#     values = arquivo.values

#     for a,linha in arquivo.iterrows():
#         elemento = linha[0]

#         for indice_coluna in range(len(arquivo.columns)-1):
#             coluna = arquivo.columns[indice_coluna+1]
#             valor = linha[indice_coluna+1]

#             print(elemento, coluna, valor)

#             cursor.execute("INSERT INTO Tab_info (Num_guia, Num_ref, Frase) VALUES (%s, %s, %s)", [elemento, coluna, valor])
#             mysql.get_db().commit()

#     cursor.close()

# with app.app_context():
#     cursor = mysql.get_db().cursor()
#     file_path = '/home/marcos/Desktop/FISPQ/FISPQFREE/scripts/arquivos_example/relacao_frases.xlsx'
#     arquivo = pd.read_excel(file_path, sheet_name='Sheet1')

#     # pegar os headers da planilha
#     print(arquivo.columns)
#     # pegar os valores da planilha
#     print(arquivo.values)

#     values = arquivo.values

#     for linha in values:
#         # for coluna in arquivo.columns:
#             cursor.execute("INSERT INTO relacao_frases (Num, N_ORD, Seq, Categoria, Frase_de_perigo, Frase_de_precaucao, Pictograma, Palavra_de_advertencia, Outros_perigos) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", [linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8]])
#             mysql.get_db().commit()

#     cursor.close()

