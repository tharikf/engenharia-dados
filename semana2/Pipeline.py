import pandas as pd
from CriandoDimensoes import criando_dimensoes
from CriandoFatoVenda import criando_fato_venda
from CargaNoPostgres import criando_engine, carregando_tabela

if __name__ == "__main__":

    # Leitura
    dados = pd.read_csv('train.csv')

    # Dimensões
    dimClientes, dimProdutos, dimLocalizacao, dimData = criando_dimensoes(dados)

    # Fato
    fatoVenda = criando_fato_venda(dados, dimLocalizacao, dimData)

    # Conexão
    engine = criando_engine(
        usuario = 'postgres',
        senha = '123456',
        host = 'localhost',
        porta = 5432,
        banco = 'postgres'
    )

    with engine.connect() as conexao:
        print('Conexão bem-sucedida!')

    # Carga
    carregando_tabela(dimClientes, 'dim_cliente', engine)
    carregando_tabela(dimProdutos, 'dim_produto', engine)
    carregando_tabela(dimLocalizacao, 'dim_localizacao', engine)
    carregando_tabela(dimData, 'dim_data', engine)
    carregando_tabela(fatoVenda, 'fato_venda', engine)
