import pandas as pd

def criando_fato_venda(dataframe, dim_localizacao, dim_data):

    df = dataframe.copy()

    # Padronizando nomes de colunas
    df.columns = df.columns.str.lower().str.replace('[ -]', '_', regex=True)

    # Convertendo campos de datas
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
    df['ship_date'] = pd.to_datetime(df['ship_date'], dayfirst=True, errors='coerce')

    # Merge com dim_data para obter IDs
    df = df.merge(dim_data, left_on='order_date', right_on='data_id', how='left') \
           .rename(columns={'data_id': 'order_date_id'})

    df = df.merge(dim_data, left_on='ship_date', right_on='data_id', how='left') \
           .rename(columns={'data_id': 'ship_date_id'})

    # Merge com dim_localizacao para obter localizacao_id
    df['postal_code'] = df['postal_code'].fillna('00000')
    df = df.merge(dim_localizacao, on=['country', 'state', 'postal_code', 'region'], how='left')

    df = df.drop(columns = ['order_date', 'ship_date'])

    # Renomear IDs finais para bater com o banco
    df = df.rename(columns={
        'order_date_id': 'order_date',
        'ship_date_id': 'ship_date'
    })

    # Selecionar colunas finais da fato_venda
    df_fato = df[['order_id', 'order_date', 'ship_date', 'customer_id', 'product_id', 'localizacao_id', 'ship_mode', 'sales']]

    return df_fato


