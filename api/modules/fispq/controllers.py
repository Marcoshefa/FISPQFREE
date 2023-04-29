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
            'onu': fispq[68],
            'nome_embarque': fispq[69],
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

    # cursor.execute("SELECT * FROM Tab_composicao INNER JOIN Fispq on Tab_composicao.cod_int_comp = Fispq.cod_int WHERE Fispq.idFispq = %s",[id])
    
    # cursor.execute("INSERT INTO Tab_composicao (cod_int_comp, substancia, cas, formula_mol, peso_mol, concentracao) VALUES (%s, %s, %s, %s, %s, %s)",
        # [substancia["cod_int_comp"], substancia["substancia"], substancia["cas"],substancia["fm"],substancia["pm"],substancia["cmm"] ])
    
    # substancias_selecionada = cursor.fetchall()

    # substancias = []

    # for substancia1 in substancias_selecionada:
    #     new_substancia1 = {
            
    #         'substancia': substancia1[2],
    #         'cas': substancia1[3],
    #         'fm': substancia1[4],
    #         'pm': substancia1[5],
    #         'cmm': substancia1[6],
    #     }
    #     substancias.append(new_substancia1)

    if not fispq_selecionada:
        return 'Fispq não encontrada', 404

    fispq = {
        'idFispq': fispq_selecionada[0],
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
        'dvapor': fispq_selecionada[77],
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
        'ecotoxidade': fispq_selecionada[79],
        'degradabilidade': fispq_selecionada[62],
        'bioacumulativo': fispq_selecionada[63],
        'mobilidade': fispq_selecionada[64],
        'outros_efeitos': fispq_selecionada[65],
        'destinacaofinal': fispq_selecionada[66],
        'terrestre': fispq_selecionada[67],
        'onu': fispq_selecionada[68],
        'nome_embarque': fispq_selecionada[69],
        'classe': fispq_selecionada[70],
        'n_risco': fispq_selecionada[71],
        'grupo_emb': fispq_selecionada[72],
        'hidroviario': fispq_selecionada[73],
        'aereo': fispq_selecionada[74],
        'regulamentacoes': fispq_selecionada[75],
        'outras_info': fispq_selecionada[76],
        'loculares': fispq_selecionada[80],
        'todas_frases_Perigo':fispq_selecionada[81],
        'todas_frases_Precaucao':fispq_selecionada[82],
        'frase_Advertencia':fispq_selecionada[83],

        # 'substancias':substancias,
    }

    # cursor.execute("INSERT INTO Tab_composicao (cod_int_comp, substancia, cas, formula_mol, peso_mol, concentracao) VALUES (%s, %s, %s, %s, %s, %s)",
        # [substancia["cod_int_comp"], substancia["substancia"], substancia["cas"],substancia["fm"],substancia["pm"],substancia["cmm"] ])


    mysql.get_db().commit()
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

    data_atual = datetime.now()
    novo_produto = dados_recebido_corpo['produto']
    novo_cod_int = dados_recebido_corpo['cod_int']
    novo_uso = dados_recebido_corpo['uso']
    novo_inalacao = dados_recebido_corpo['inalacao']
    novo_cont_olhos = dados_recebido_corpo['cont_olhos']
    novo_cont_pele = dados_recebido_corpo['cont_pele']
    novo_ingestao = dados_recebido_corpo['ingestao']
    novo_sintomas = dados_recebido_corpo['sintomas']
    novo_medico = dados_recebido_corpo['medico']
    novo_extincao = dados_recebido_corpo['extincao']
    novo_perigo_esp = dados_recebido_corpo['perigo_esp']
    novo_medidas_protecao = dados_recebido_corpo['medidas_protecao']
    novo_servico_emergencia = dados_recebido_corpo['servico_emergencia']
    novo_servico_emergencia2 = dados_recebido_corpo['servico_emergencia2']
    novo_precaucao_ambiente = dados_recebido_corpo['precaucao_ambiente']
    novo_metodos_materiais = dados_recebido_corpo['metodos_materiais']
    novo_manuseio_seguro = dados_recebido_corpo['manuseio_seguro']
    novo_medidas_higiene = dados_recebido_corpo['medidas_higiene']
    novo_condicoes_armazenamento = dados_recebido_corpo['condicoes_armazenamento']
    novo_limitexposicao = dados_recebido_corpo['limitexposicao']
    novo_medcontroleng = dados_recebido_corpo['medcontroleng']
    novo_polhos = dados_recebido_corpo['polhos']
    novo_ppele = dados_recebido_corpo['ppele']
    novo_prespiratoria = dados_recebido_corpo['prespiratoria']
    novo_ptermicos = dados_recebido_corpo['ptermicos']
    novo_aspecto = dados_recebido_corpo['aspecto']
    novo_odor = dados_recebido_corpo['odor']
    novo_ph = dados_recebido_corpo['ph']
    novo_fusao = dados_recebido_corpo['fusao']
    novo_ebulicao = dados_recebido_corpo['ebulicao']
    novo_fulgor = dados_recebido_corpo['fulgor']
    novo_evaporacao = dados_recebido_corpo['evaporacao']
    novo_inflamabilidade = dados_recebido_corpo['inflamabilidade']
    novo_explosividade = dados_recebido_corpo['explosividade']
    novo_pvapor = dados_recebido_corpo['pvapor']
    novo_dvapor = dados_recebido_corpo['dvapor']
    novo_drelativa = dados_recebido_corpo['drelativa']
    novo_solubilidade = dados_recebido_corpo['solubilidade']
    novo_particao = dados_recebido_corpo['particao']
    novo_autoignicao = dados_recebido_corpo['autoignicao']
    novo_decomposicao = dados_recebido_corpo['decomposicao']
    novo_viscosidade = dados_recebido_corpo['viscosidade']
    novo_informacoes = dados_recebido_corpo['informacoes']
    novo_reatividade = dados_recebido_corpo['reatividade']
    novo_estabilidadeq = dados_recebido_corpo['estabilidadeq']
    novo_rperigosas = dados_recebido_corpo['rperigosas']
    novo_caseremevitadas = dados_recebido_corpo['caseremevitadas']
    novo_incompativeis = dados_recebido_corpo['incompativeis']
    novo_pdecomposicao = dados_recebido_corpo['pdecomposicao']
    novo_toxicidadea = dados_recebido_corpo['toxicidadea']
    novo_cpele = dados_recebido_corpo['cpele']
    novo_srespiratoria = dados_recebido_corpo['srespiratoria']
    novo_mutagenicidade = dados_recebido_corpo['mutagenicidade']
    novo_carcinogenicidade = dados_recebido_corpo['carcinogenicidade']
    novo_reproducao = dados_recebido_corpo['reproducao']
    novo_exposicaou = dados_recebido_corpo['exposicaou']
    novo_exposicaor = dados_recebido_corpo['exposicaor']
    novo_aspiracao = dados_recebido_corpo['aspiracao']
    novo_ecotoxidade = dados_recebido_corpo['ecotoxidade']
    novo_degradabilidade = dados_recebido_corpo['degradabilidade']
    novo_bioacumulativo = dados_recebido_corpo['bioacumulativo']
    novo_mobilidade = dados_recebido_corpo['mobilidade']
    novo_outros_efeitos = dados_recebido_corpo['outros_efeitos']
    novo_destinacaofinal = dados_recebido_corpo['destinacaofinal']
    novo_terrestre = dados_recebido_corpo['terrestre']
    novo_onu = dados_recebido_corpo['onu']
    novo_nome_embarque = dados_recebido_corpo['nome_embarque']
    novo_classe = dados_recebido_corpo['classe']
    novo_n_risco = dados_recebido_corpo['n_risco']
    novo_grupo_emb = dados_recebido_corpo['grupo_emb']
    novo_hidroviario = dados_recebido_corpo['hidroviario']
    novo_aereo = dados_recebido_corpo['aereo']
    novo_regulamentacoes = dados_recebido_corpo['regulamentacoes']
    novo_outras_info = dados_recebido_corpo['outras_info']
    novo_loculares = dados_recebido_corpo['loculares']

    # novo_substancia = dados_recebido_corpo['substancias']


    # atualizar no banco de dados com as novas informacoes para o usuario

    cursor.execute("UPDATE Fispq SET produto = %s, cod_int = %s, uso = %s, inalacao = %s, cont_olhos = %s, cont_pele = %s, ingestao = %s,sintomas = %s, medico = %s, extincao = %s, perigo_esp = %s, medidas_protecao = %s, servico_emergencia = %s, servico_emergencia2 = %s, precaucao_ambiente = %s, metodos_materiais = %s, manuseio_seguro = %s, medidas_higiene = %s, condicoes_armazenamento = %s, limitexposicao = %s, medcontroleng = %s, polhos = %s, ppele = %s, prespiratoria = %s, ptermicos = %s, aspecto = %s, odor = %s, ph = %s, fusao = %s, ebulicao = %s, fulgor = %s, evaporacao = %s, inflamabilidade = %s, explosividade = %s, pvapor = %s, dvapor= %s, drelativa = %s, solubilidade = %s, particao = %s, autoignicao = %s, decomposicao = %s, viscosidade = %s, informacoes = %s, reatividade = %s, estabilidadeq = %s, rperigosas = %s, caseremevitadas = %s, incompativeis = %s, pdecomposicao = %s, toxicidadea = %s, cpele = %s, srespiratoria = %s, mutagenicidade = %s, carcinogenicidade = %s, reproducao = %s, exposicaou = %s, exposicaor = %s, aspiracao = %s, ecotoxidade = %s, degradabilidade = %s, bioacumulativo = %s, mobilidade = %s, outros_efeitos = %s, destinacaofinal = %s, terrestre = %s, onu = %s, nome_embarque = %s, classe = %s, n_risco = %s, grupo_emb = %s, hidroviario = %s, aereo = %s, regulamentacoes = %s, outras_info = %s, loculares = %s, update_at = %s WHERE idFispq = %s",

    [novo_produto, novo_cod_int, novo_uso, novo_inalacao, novo_cont_olhos, novo_cont_pele, novo_ingestao, novo_sintomas, novo_medico, novo_extincao, novo_perigo_esp, novo_medidas_protecao, novo_servico_emergencia, novo_servico_emergencia2, novo_precaucao_ambiente, novo_metodos_materiais, novo_manuseio_seguro, novo_medidas_higiene, novo_condicoes_armazenamento, novo_limitexposicao, novo_medcontroleng, novo_polhos, novo_ppele, novo_prespiratoria, novo_ptermicos, novo_aspecto, novo_odor, novo_ph, novo_fusao, novo_ebulicao, novo_fulgor, novo_evaporacao, novo_inflamabilidade, novo_explosividade, novo_pvapor, novo_dvapor, novo_drelativa, novo_solubilidade, novo_particao, novo_autoignicao, novo_decomposicao, novo_viscosidade, novo_informacoes, novo_reatividade, novo_estabilidadeq, novo_rperigosas, novo_caseremevitadas, novo_incompativeis, novo_pdecomposicao, novo_toxicidadea, novo_cpele, novo_srespiratoria, novo_mutagenicidade, novo_carcinogenicidade, novo_reproducao, novo_exposicaou, novo_exposicaor, novo_aspiracao, novo_ecotoxidade, novo_degradabilidade, novo_bioacumulativo, novo_mobilidade, novo_outros_efeitos, novo_destinacaofinal, novo_terrestre, novo_onu, novo_nome_embarque, novo_classe, novo_n_risco, novo_grupo_emb, novo_hidroviario, novo_aereo, novo_regulamentacoes, novo_outras_info, novo_loculares, data_atual, id])

    # cursor.execute("UPDATE Tab_composicao INNER JOIN Fispq on Tab_composicao.cod_int_comp = Fispq.cod_int WHERE Fispq.idFispq = %s",[id])
    # cursor.execute("UPDATE Tab_composicao SET substancia = %s, cas = %s, formula_mol = %s, peso_mol = %s, concentracao = %s) WHERE idFispq = %s",
    # [novo_substancia["substancia"], novo_substancia["cas"],novo_substancia["fm"],novo_substancia["pm"],novo_substancia["cmm"] ])
    # [novo_substancia[0], novo_substancia[1],novo_substancia[2],novo_substancia[3],novo_substancia[4] ])

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
    inalacao = dados_recebido['inalacao']
    cont_olhos = dados_recebido['cont_olhos']
    cont_pele = dados_recebido['cont_pele']
    ingestao = dados_recebido['ingestao']
    sintomas = dados_recebido['sintomas']
    medico = dados_recebido['medico']
    extincao = dados_recebido['extincao']
    perigo_esp = dados_recebido['perigo_esp']
    medidas_protecao = dados_recebido['medidas_protecao']
    servico_emergencia = dados_recebido['servico_emergencia']
    servico_emergencia2 = dados_recebido['servico_emergencia2']
    precaucao_ambiente = dados_recebido['precaucao_ambiente']
    metodos_materiais = dados_recebido['metodos_materiais']
    manuseio_seguro = dados_recebido['manuseio_seguro']
    medidas_higiene = dados_recebido['medidas_higiene']
    condicoes_armazenamento = dados_recebido['condicoes_armazenamento']
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
    loculares = dados_recebido['loculares']
    nome_embarque = dados_recebido['nome_embarque']
    substancias = dados_recebido['substancias']
    todas_frases_Perigo = dados_recebido['todas_frases_Perigo']
    todas_frases_Precaucao = dados_recebido['todas_frases_Precaucao']
    frase_Advertencia = dados_recebido['frase_Advertencia']
    pictogramas = dados_recebido['pictogramas']

    # cria o SQL
    cursor.execute("SELECT * FROM Fispq WHERE cod_int = %s", [cod_int])
    fispq = cursor.fetchone()
    if fispq:
        return 'Fispq já existe no banco de dados', 409

    # insere as insformações no banco de dados
    cursor.execute("INSERT INTO Fispq (cod_int, produto, uso, inalacao, cont_olhos, cont_pele, ingestao, sintomas, medico, extincao, perigo_esp, medidas_protecao, servico_emergencia, servico_emergencia2, precaucao_ambiente, metodos_materiais, manuseio_seguro, medidas_higiene, condicoes_armazenamento, limitexposicao, medcontroleng, polhos, ppele, prespiratoria, ptermicos, aspecto, odor, ph, fusao, ebulicao, fulgor, evaporacao, inflamabilidade, explosividade, pvapor, dvapor, drelativa, solubilidade, particao, autoignicao, decomposicao, viscosidade, informacoes, reatividade, estabilidadeq, rperigosas, caseremevitadas, incompativeis, pdecomposicao, toxicidadea, cpele, srespiratoria, mutagenicidade, carcinogenicidade, reproducao, exposicaou, exposicaor, aspiracao, ecotoxidade, degradabilidade, bioacumulativo, mobilidade, outros_efeitos, destinacaofinal, terrestre, onu, nome_embarque, classe, n_risco, grupo_emb, hidroviario, aereo, regulamentacoes, outras_info, loculares, todas_frases_Perigo, todas_frases_Precaucao, frase_Advertencia, pictogramas) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                  
        [cod_int, produto, uso, inalacao, cont_olhos, cont_pele, ingestao, sintomas, medico, extincao, perigo_esp, medidas_protecao, servico_emergencia, servico_emergencia2, precaucao_ambiente, metodos_materiais, manuseio_seguro, medidas_higiene, condicoes_armazenamento, limitexposicao, medcontroleng, polhos, ppele, prespiratoria, ptermicos, aspecto, odor, ph, fusao, ebulicao, fulgor, evaporacao, inflamabilidade, explosividade, pvapor, dvapor, drelativa, solubilidade, particao, autoignicao, decomposicao, viscosidade, informacoes, reatividade, estabilidadeq, rperigosas, caseremevitadas, incompativeis, pdecomposicao, toxicidadea, cpele, srespiratoria, mutagenicidade, carcinogenicidade, reproducao, exposicaou, exposicaor, aspiracao, ecotoxidade, degradabilidade, bioacumulativo, mobilidade, outros_efeitos, destinacaofinal, terrestre, onu, nome_embarque, classe, n_risco, grupo_emb, hidroviario, aereo, regulamentacoes, outras_info, loculares, todas_frases_Perigo, todas_frases_Precaucao, frase_Advertencia, pictogramas])

    mysql.get_db().commit()
    for substancia in substancias:
        cursor.execute("INSERT INTO Tab_composicao (cod_int, substancia, cas, formula_mol, peso_mol,concentracao) VALUES (%s, %s, %s, %s, %s, %s)",
        [cod_int, substancia["substancia"], substancia["cas"],substancia["fm"],substancia["pm"],substancia["cmm"] ])
  
        mysql.get_db().commit()

    #fecha a instancia do banco de dados
    cursor.close()

    return 'Fispq cadastrada com sucesso', 201

def create_new_fispq_comp(dados_recebido):

    # instancia o banco de dados
    cursor = mysql.get_db().cursor()

    # Pega as informações do banco de dados
    cod_int_comp = dados_recebido['cod_int_comp']
    substancia = dados_recebido['substancia']
    cas = dados_recebido['cas']
    formula_mol = dados_recebido['fm']
    peso_mol = dados_recebido['pm']
    concentracao = dados_recebido['cmm']
   

    # cria o SQL
    cursor.execute("SELECT * FROM Tab_composicao WHERE cod_int_comp = %s", [cod_int_comp])
    fispq = cursor.fetchone()
    if fispq:
        return 'Fispq já existe no banco de dados', 409

    # insere as insformações no banco de dados
    cursor.execute("INSERT INTO Tab_composicao (cod_int_comp, substancia, cas, formula_mol, peso_mol, concentracao) VALUES (%s, %s, %s, %s, %s, %s)", 
                  
        [cod_int_comp, substancia, cas, formula_mol, peso_mol, concentracao])

    mysql.get_db().commit()

    #fecha a instancia do banco de dados
    cursor.close()

    return 'Fispq cadastrada com sucesso', 201

def get_frases_by_onu(n_onu):
    cursor = mysql.get_db().cursor()

    cursor.execute("""
        SELECT * 
        FROM Tab_onu_none_aprop as onu
        INNER JOIN Tab_info as info ON onu.N_Guia = info.Num_guia
        WHERE onu.N_ONU = %s
    """, [n_onu])

    frases_onu = cursor.fetchall()

    if not frases_onu:
        return 'Não encontramos frases para esse numero ONU', 404

    resposta = {
        'numero_onu': n_onu,
        'numero_guia': frases_onu[0][1],
        'Nome_aprop': frases_onu[2],
        'frases': {}
    }

    for frase in frases_onu:
        resposta['frases'][frase[4]] = frase[5]

    return resposta

def list_all_categoria():
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM relacao_frases")

    frasesprecs_db = cursor.fetchall()

    all_categorias = []

    for categoria in frasesprecs_db:
        new_categoria = {
            'Num': categoria[0],
            'Categoria': categoria[3],
        }

        all_categorias .append(new_categoria )

    cursor.close()

    return all_categorias 


def list_all_categoria_frases(nums):
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM relacao_frases WHERE Num in %(Nums)s", {"Nums":nums.split(",")})

    frases_db = cursor.fetchall()

    all_frases_perigo = []
    all_frases_precaucao = []
    all_frases_advertencia = ""
    all_pictograma = []

    for frase in frases_db:
        if frase[4] not in all_frases_perigo:
            all_frases_perigo.append(frase[4])

        if frase[7] not in all_frases_advertencia and 'Perigo' not in all_frases_advertencia:
            all_frases_advertencia = frase[7]
           
        if frase[6] not in all_pictograma:
            all_pictograma.append(frase[6])

        cursor.execute("SELECT * FROM Tab_frase_precaucao WHERE cod_precaucao in %(Nums)s", {"Nums":frase[5].split(", ")})
        frases_precaucao = cursor.fetchall()
        for frase_precaucao in frases_precaucao:
            if frase_precaucao[0] not in all_frases_precaucao:
                all_frases_precaucao.append(frase_precaucao[0] +' '+ frase_precaucao[1])

    cursor.close()

    return {
        'frases_perigo': all_frases_perigo,
        'frases_precaucao': all_frases_precaucao,
        'frases_advertencia': all_frases_advertencia,
        'pictogramas': all_pictograma
    }