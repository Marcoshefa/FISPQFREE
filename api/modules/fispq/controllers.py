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
        # 'cod_int': fispq_selecionada[6],
        # 'produto': fispq_selecionada[5],
        # 'onu': fispq_selecionada[69],
        # 'nome_embarque': fispq_selecionada[70],
        'created_at': fispq_selecionada[1],
        'update_at': fispq_selecionada[2],

        'produto': fispq_selecionada[5],
        'cod_int': fispq_selecionada[6],
        'uso': fispq_selecionada[7],
        'inalacao': fispq_selecionada[8],
        'cont_olhos': fispq_selecionada[9],
        'cont_pele': fispq_selecionada[10],
        'ingestao': fispq_selecionada[11],
        'sintomas': fispq_selecionada[12],
        'medico': fispq_selecionada[13],
        'extincao': fispq_selecionada[14],
        'perigo_esp': fispq_selecionada[15],
        'medidas_protecao': fispq_selecionada[16],
        'servico_emergencia': fispq_selecionada[17],
        'servico_emergencia2': fispq_selecionada[18],
        'precaucao_ambiente': fispq_selecionada[19],
        'metodos_materiais': fispq_selecionada[20],
        'manuseio_seguro': fispq_selecionada[21],
        'medidas_higiene': fispq_selecionada[22],
        'condicoes_armazenamento': fispq_selecionada[23],
        'limitexposicao': fispq_selecionada[24],
        'medcontroleng': fispq_selecionada[25],
        'polhos': fispq_selecionada[26],
        'ppele': fispq_selecionada[27],
        'prespiratoria': fispq_selecionada[28],
        'ptermicos': fispq_selecionada[29],
        'aspecto': fispq_selecionada[30],
        'odor': fispq_selecionada[31],
        'ph': fispq_selecionada[32], 
        'fusao': fispq_selecionada[33],
        'ebulicao': fispq_selecionada[34],
        'fulgor': fispq_selecionada[35],
        'evaporacao': fispq_selecionada[36],
        'inflamabilidade': fispq_selecionada[37],
        'explosividade': fispq_selecionada[38],
        'pvapor': fispq_selecionada[39],
        'dvapor': fispq_selecionada[80],
        'drelativa': fispq_selecionada[40],
        'solubilidade': fispq_selecionada[41],
        'particao': fispq_selecionada[42],
        'autoignicao': fispq_selecionada[43],
        'decomposicao': fispq_selecionada[44],
        'viscosidade': fispq_selecionada[45],
        'informacoes': fispq_selecionada[46],
        'reatividade': fispq_selecionada[47],
        'estabilidadeq': fispq_selecionada[48],
        'rperigosas': fispq_selecionada[49],
        'caseremevitadas': fispq_selecionada[50],
        'incompativeis': fispq_selecionada[51],
        'pdecomposicao': fispq_selecionada[52],
        'toxicidadea': fispq_selecionada[53],
        'cpele': fispq_selecionada[54],
        'srespiratoria': fispq_selecionada[55],
        'mutagenicidade': fispq_selecionada[56],
        'carcinogenicidade': fispq_selecionada[57],
        'reproducao': fispq_selecionada[58],
        'exposicaou': fispq_selecionada[59],
        'exposicaor': fispq_selecionada[60],
        'aspiracao': fispq_selecionada[61],
        'ecotoxidade': fispq_selecionada[62],
        'degradabilidade': fispq_selecionada[63],
        'bioacumulativo': fispq_selecionada[64],
        'mobilidade': fispq_selecionada[65],
        'outros_efeitos': fispq_selecionada[66],
        'destinacaofinal': fispq_selecionada[67],
        'terrestre': fispq_selecionada[68],
        'onu': fispq_selecionada[69],
        'nome_embarque': fispq_selecionada[70],
        'classe': fispq_selecionada[71],
        'n_risco': fispq_selecionada[72],
        'grupo_emb': fispq_selecionada[73],
        'hidroviario': fispq_selecionada[74],
        'aereo': fispq_selecionada[75],
        'regulamentacoes': fispq_selecionada[76],
        'outras_info': fispq_selecionada[77],
        'outras_info2': fispq_selecionada[78],
        'legenda': fispq_selecionada[79],
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
    limitexposicao = dados_recebido['limitexposicao']
    medcontroleng = dados_recebido['medcontroleng']
    polhos = dados_recebido['polhos']
    ppele = dados_recebido['ppele']
    prespiratoria = dados_recebido['prespiratoria']
    ptermicos  =dados_recebido['ptermicos']
    aspecto = dados_recebido['aspecto']
    odor = dados_recebido['odor']
    ph = dados_recebido['ph']
    fusao = dados_recebido['fusao']
    ebulicao = dados_recebido['ebulicao']
    fulgor = dados_recebido['fulgor']
    evaporacao = dados_recebido['evaporacao']
    inflamabilidade = dados_recebido['inflamabilidade']
    explosividade = dados_recebido['explosividade']
    pvapor = dados_recebido['pvapor']
    dvapor = dados_recebido['dvapor']
    drelativa = dados_recebido['drelativa']
    solubilidade = dados_recebido['solubilidade']
    particao = dados_recebido['particao']
    autoignicao = dados_recebido['autoignicao']
    decomposicao = dados_recebido['decomposicao']
    viscosidade = dados_recebido['viscosidade']
    informacoes = dados_recebido['informacoes']
    reatividade = dados_recebido['reatividade']
    estabilidadeq = dados_recebido['estabilidadeq']
    rperigosas = dados_recebido['rperigosas']
    caseremevitadas = dados_recebido['caseremevitadas']
    incompativeis = dados_recebido['incompativeis']
    pdecomposicao = dados_recebido['pdecomposicao']
    toxicidadea = dados_recebido['toxicidadea']
    cpele = dados_recebido['cpele']
    srespiratoria = dados_recebido['srespiratoria']
    mutagenicidade = dados_recebido['mutagenicidade']
    carcinogenicidade = dados_recebido['carcinogenicidade']
    reproducao = dados_recebido['reproducao']
    exposicaou = dados_recebido['exposicaou']
    exposicaor = dados_recebido['exposicaor']
    aspiracao = dados_recebido['aspiracao']
    ecotoxidade = dados_recebido['ecotoxidade']
    degradabilidade = dados_recebido['degradabilidade']
    bioacumulativo = dados_recebido['bioacumulativo']
    mobilidade = dados_recebido['mobilidade']
    outros_efeitos = dados_recebido['outros_efeitos']
    destinacaofinal = dados_recebido['destinacaofinal']
    terrestre = dados_recebido['terrestre']
    onu = dados_recebido['onu']
    nome_embarque = dados_recebido['nome_embarque']
    classe = dados_recebido['classe']
    n_risco = dados_recebido['n_risco']
    grupo_emb = dados_recebido['grupo_emb']
    hidroviario = dados_recebido['hidroviario']
    aereo = dados_recebido['aereo']
    regulamentacoes = dados_recebido['regulamentacoes']
    outras_info = dados_recebido['outras_info']
    outras_info2 = dados_recebido['outras_info2']
    legenda = dados_recebido['legenda']
    nome_embarque = dados_recebido['nome_embarque']

    # onu = dados_recebido.get('onu')
    # nome_embarque = dados_recebido.get('nome_embarque')

    # cria o SQL
    cursor.execute("SELECT * FROM Fispq WHERE cod_int = %s", [cod_int])
    fispq = cursor.fetchone()
    if fispq:
        return 'Fispq já existe no banco de dados', 409

    # insere as insformações no banco de dados
    cursor.execute("INSERT INTO Fispq (cod_int, produto, uso, limitexposicao, medcontroleng, polhos, ppele, prespiratoria, ptermicos, aspecto, odor, ph, fusao, ebulicao, fulgor, evaporacao, inflamabilidade, explosividade, pvapor, dvapor, drelativa, solubilidade, particao, autoignicao, decomposicao, viscosidade, informacoes, reatividade, estabilidadeq, rperigosas, caseremevitadas, incompativeis, pdecomposicao, toxicidadea, cpele, srespiratoria, mutagenicidade, carcinogenicidade, reproducao, exposicaou, exposicaor, aspiracao, ecotoxidade, degradabilidade, bioacumulativo, mobilidade, outros_efeitos, destinacaofinal, terrestre, onu, nome_embarque, classe, n_risco, grupo_emb, hidroviario, aereo, regulamentacoes, outras_info, outras_info2, legenda) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                  
        [cod_int, produto, uso, limitexposicao, medcontroleng, polhos, ppele, prespiratoria, ptermicos, aspecto, odor, ph, fusao, ebulicao, fulgor, evaporacao, inflamabilidade, explosividade, pvapor, dvapor, drelativa, solubilidade, particao, autoignicao, decomposicao, viscosidade, informacoes, reatividade, estabilidadeq, rperigosas, caseremevitadas, incompativeis, pdecomposicao, toxicidadea, cpele, srespiratoria, mutagenicidade, carcinogenicidade, reproducao, exposicaou, exposicaor, aspiracao, ecotoxidade, degradabilidade, bioacumulativo, mobilidade, outros_efeitos, destinacaofinal, terrestre, onu, nome_embarque, classe, n_risco, grupo_emb, hidroviario, aereo, regulamentacoes, outras_info, outras_info2, legenda])

    mysql.get_db().commit()

    #fecha a instancia do banco de dados
    cursor.close()

    return 'Fispq cadastrada com sucesso', 201