/*
DROP TABLE IF EXISTS fato_venda;
DROP TABLE IF EXISTS dim_cliente;
DROP TABLE IF EXISTS dim_data;
DROP TABLE IF EXISTS dim_localizacao;
DROP TABLE IF EXISTS dim_produto;
*/

-- Implementação do modelo físico

CREATE TABLE dim_data (
	data_id DATE PRIMARY KEY,
	dia INT,
	mes INT,
	ano INT,
	dia_semana VARCHAR(20)
);


CREATE TABLE dim_cliente (
	customer_id VARCHAR(50) PRIMARY KEY,
	customer_name VARCHAR(100),
	segment VARCHAR(30)
);

CREATE TABLE dim_produto (
	product_id VARCHAR(50) PRIMARY KEY,
	product_name VARCHAR(200),
	sub_category VARCHAR(100),
	category VARCHAR(100)
);

/*

SERIAL em PostgreSQL é um atalho para criar uma coluna do tipo INTEGER ocm auto incremento. Ou seja,
o banco vai gerar automaticamente um ID incremental único para cada nova linha inserida na dim_localizacao.

*/


CREATE TABLE dim_localizacao (
	localizacao_id SERIAL PRIMARY KEY,
	country VARCHAR(50),
	city VARCHAR(50),
	state VARCHAR(50),
	postal_code VARCHAR(20),
	region VARCHAR(50)
);

CREATE TABLE fato_venda (
	row_id SERIAL PRIMARY KEY,
	order_id VARCHAR(50),
	order_date DATE,
	ship_date DATE,
	ship_mode VARCHAR(50),
	customer_id VARCHAR(50),
    product_id VARCHAR(50),
  	localizacao_id INT,
  	sales NUMERIC(10,2),

	FOREIGN KEY (order_date) REFERENCES dim_data(data_id),
	FOREIGN KEY (ship_date) REFERENCES dim_data(data_id),
	FOREIGN KEY (customer_id) REFERENCES dim_cliente(customer_id),
	FOREIGN KEY (product_id) REFERENCES dim_produto(product_id),
	FOREIGN KEY (localizacao_id) REFERENCES dim_localizacao(localizacao_id)
);



