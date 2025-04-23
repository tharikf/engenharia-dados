

import pandas as pd
import sqlalchemy
import psycopg2

dados_brutos = pd.read_csv('train.csv')


# Criando as dimensões
def criando_dimensoes(dados):

    df = dados.copy()

    # Padronizando nomes de colunas
    df.columns = df.columns.str.lower().str.replace('[ -]', '_', regex = True)

    # Dimensao cliente -> Selecionando colunas e selecionando valores únicos
    df_clientes = df[['customer_id', 'customer_name', 'segment']]
    df_clientes = df_clientes.drop_duplicates(subset = ['customer_id']).sort_values(by = 'customer_id')

    # Dimensao produto -> Selecionando colunas e selecionando valores únicos
    df_produtos = df[['product_id', 'product_name', 'category', 'sub_category']]
    df_produtos = df_produtos.drop_duplicates(subset = ['product_id']).sort_values(by = 'product_id')

    # Dimensao localização -> Selecionando colunas e selecionando valores únicos
    df_localizacao = df[['country', 'state', 'postal_code', 'region']].drop_duplicates().reset_index(drop=True)
    df_localizacao['localizacao_id'] = df_localizacao.index + 1
    df_localizacao = df_localizacao[['localizacao_id', 'country', 'state', 'postal_code', 'region']].sort_values(by = 'localizacao_id')

    # Dimensao data -> Selecionando colunas e selecionando valores únicos
    datas = pd.concat([df['order_date'], df['ship_date']]).drop_duplicates()
    datas = pd.to_datetime(datas, dayfirst = True, errors = 'coerce')
    df_data = pd.DataFrame({'data_id': datas})
    df_data['ano'] = df_data['data_id'].dt.year
    df_data['mes'] = df_data['data_id'].dt.month
    df_data['dia'] = df_data['data_id'].dt.day
    dias = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
    df_data['dia_semana'] = df_data['data_id'].dt.weekday.map(lambda x: dias[x])
    df_data = df_data.sort_values(by = 'data_id')

    return df_clientes, df_produtos, df_localizacao, df_data


dimClientes, dimProdutos, dimLocalizacao, dimData = criando_dimensoes(dados_brutos)


