
from numpy import var
import pandas as pd
from flaskext.mysql import MySQL

from flask import Flask

app = Flask(__name__)


app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Marcos21111984!'
app.config['MYSQL_DATABASE_DB'] = 'DB_FISPQ'

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
#     file_path = '/home/marcos/Desktop/FISPQ/FISPQFREE/scripts/arquivos_example/Tab_onu_none_aprop.xlsx'
#     arquivo = pd.read_excel(file_path, sheet_name='Sheet1')

#     # pegar os headers da planilha
#     print(arquivo.columns)
#     # pegar os valores da planilha
#     print(arquivo.values)

#     values = arquivo.values

#     for linha in values:
#         # for coluna in arquivo.columns:
#             cursor.execute("INSERT INTO Tab_onu_none_aprop (N_ONU, N_Guia, Nome_aprop) VALUES (%s, %s, %s)", [linha[0], linha[1], linha[2]])
#             mysql.get_db().commit()

#     cursor.close()

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
#         for coluna in arquivo.columns:
#             cursor.execute("INSERT INTO Tab_frase_precaucao (cod_precaucao, frase_precaucao) VALUES (%s, %s)", [linha[0], linha[1]])
#             mysql.get_db().commit()

#     cursor.close()

with app.app_context():
    # cursor = mysql.get_db().cursor()
    file_path = '/home/marcos/Desktop/FISPQ/FISPQFREE/scripts/arquivos_example/text.xlsx'
   
    arquivo = pd.read_excel(file_path, sheet_name='Sheet1')

    # # pegar os headers da planilha
    # print(arquivo.columns)
    # # pegar os valores da planilha
    # print(arquivo.values)

    values = arquivo.values


    for a in arquivo.iterrows():
        
        
        print(a)

  

    
    # for linha in values:
    #     # for coluna in arquivo.columns:
    #         cursor.execute("INSERT INTO text(codigo, frases_perigo) VALUES (%s, %s)", [linha[0], linha[1]])
    #         mysql.get_db().commit()

    # cursor.close()

