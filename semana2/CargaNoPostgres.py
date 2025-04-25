
from sqlalchemy import create_engine
import psycopg2
import pandas as pd


# Conectando com o banco
def criando_engine(usuario, senha, host, porta, banco):

    url = f'postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}'

    return create_engine(url)


# Carregando a tabela
def carregando_tabela(dados, nome_tabela, engine):

    df = dados.copy()

    # Carregar tabela
    try:
        df.to_sql(nome_tabela, con = engine, if_exists = 'append', index = False)
        print(f"Tabela '{nome_tabela}' carregada com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar '{nome_tabela}': {e}")



