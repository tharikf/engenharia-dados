
import pandas as pd
from CriandoDimensoes import dimLocalizacao
from CriandoDimensoes import dimData

# Lendo dados brutos
dados_brutos_fato_venda = pd.read_csv('train.csv')


def tratando_dados_brutos(dataframe, dim_localizacao, dim_data):

    df = dataframe.copy()

    # Padronizando nomes de colunas
    df.columns = df.columns.str.lower().str.replace('[ -]', '_', regex = True)

    
    # Convertendo campos de datas
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst = True, errors = 'coerce')
    df['ship_date'] = pd.to_datetime(df['ship_date'], dayfirst = True, errors = 'coerce')

    # Merge com dim_data para pegar o ID da data
    df = df.merge(dim_data.rename(columns = {'data_id' : 'order_date'}), on = 'order_date', how = 'left')
    
    df = df.merge(dim_data.rename(columns = {'data_id' : 'ship_date'}), on = 'ship_date', how = 'left')
    
    # Merge com dim_localizacao para pegar o ID
    df['postal_code'] = df['postal_code'].fillna('00000')
    df = df.merge(dim_localizacao, on = ['country', 'state', 'postal_code', 'region'], how = 'left')


    # Selecionar colunas que vão compor a tabela
    df_fato = df[['order_id', 'order_date', 'ship_date', 'customer_id', 'product_id', 'localizacao_id', 'ship_mode', 'sales']]


    return df_fato

FatoVenda = tratando_dados_brutos(dados_brutos_fato_venda, dimLocalizacao, dimData)


