


-- Limpeza
DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS clientes;

-- Criação de clientes
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    cidade VARCHAR(50)
);

-- Criação de pedidos com FK
CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(id),
    data_pedido DATE,
    valor NUMERIC(10,2)
);


INSERT INTO clientes (nome, cidade) VALUES
('Ana', 'São Paulo'),
('Bruno', 'Rio de Janeiro'),
('Carla', 'Belo Horizonte'),
('Diego', 'São Paulo');

INSERT INTO pedidos (cliente_id, data_pedido, valor) VALUES
(1, '2024-03-01', 250.00),
(1, '2024-03-15', 300.00),
(2, '2024-03-10', 180.00),
(3, '2024-03-17', 500.00),
(4, '2024-03-20', 150.00),
(4, '2024-03-25', 400.00);





