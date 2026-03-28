import requests
"""
pt-BR (Brazilian Portuguese)
"""


URL_API = 'https://fix-sql.onrender.com/{}'


def query_otimizada(script_sql: str) -> str:
    url = URL_API.format('optimize')
    res = requests.post(url, params={
        'text': script_sql
    })
    if res.status_code != 200:
        return res.json()['detail'] # ----- ERRO!
    return res.json()['result']

def traduz_para_mongo(script_sql: str) -> str:
    url = URL_API.format('translate')
    res = requests.post(url, params={
        'text': script_sql, 'language': 'mongoDB'
    })
    if res.status_code != 200:
        return res.json()['detail'] # ----- ERRO!
    return res.json()['result']

def faz_join(script: str) -> str:
    """
    O script deve estar no seguinte formato:
    > tabela1(campo1, campo2, chave) -> tabela2(chave, campo1, campo2)
    """
    url = URL_API.format('join')
    res = requests.post(url, params={'cypher_script': script})
    if res.status_code != 200:
        return res.json()['detail'] # ----- ERRO!
    return res.json()['result']

def separa_queries(script_sql: str) -> dict:
    url = URL_API.format('split')
    res = requests.post(url, params={
        'text': script_sql
    })
    if res.status_code != 200:
        return res.json()['detail'] # ----- ERRO!
    return res.json()


if __name__ == '__main__':
    sql = query_otimizada('''
        Select * FROM Venda 
            AND year(dt_ref) = 2023
        ordER BY cliente_id DESC
    ''')
    print('Query otimizada:'.center(50, '='))
    print(sql)
    mongo = traduz_para_mongo(sql)
    print('Tradução para MongoDB'.center(50, '='))
    print(mongo)
    print('Junta 2 tabelas'.center(50, '='))
    sql = faz_join('produto(nome ?valor > 500, id) <- venda(pro_id ^dt_ref)')
    print(sql)
    print('Queries separadas:'.center(50, '='))
    TUDO_JUNTO = '''
        SELECT c.nome, v.quantidade, v.dt_ref
        FROM Cliente c JOIN Venda v ON (c.id = v.cli_d)
        WHERE c.regiao = 'sul' ORDER BY v.dt_ref
    '''
    for tabela, query in separa_queries(TUDO_JUNTO).items():
        print(tabela.center(50, '-'))
        print(query)
    print('#'*50)
