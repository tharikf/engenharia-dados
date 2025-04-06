


-- Exercício 1: Top 2 clientes que mais gastaram
SELECT
	c.nome,
	SUM(p.valor) AS valor_gasto
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id -- p.client_id pois id é a PK e cliente_id é FK.
GROUP BY
	nome
ORDER BY valor_gasto DESC
LIMIT 2;

-- Exercício 2: Pedidos acima da média (usando CTE (Common Table Expression)
-- Uma CTE é uma tabela temporária nomeada só para a determinada query.
WITH media AS (
	SELECT AVG(valor) AS valor_medio FROM pedidos
)
SELECT
	c.nome,
	p.valor
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id
JOIN media m ON p.valor > m.valor_medio;

-- Exercício 3: Ranking de clientes por total gasto
SELECT
	c.nome,
	SUM(p.valor) AS valor_gasto,
	RANK() OVER (ORDER BY SUM(p.valor) DESC) AS ranking
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.nome;

-- Exercício 4: Média móvel de pedidos por cliente
-- Utilizando funções janela (OVER()), não precisa de GROUP BY.
SELECT
	c.nome,
	p.data_pedido,
	p.valor,
	AVG(p.valor) OVER(PARTITION BY p.cliente_id ORDER BY p.data_pedido ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS media_movel
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id
ORDER BY c.nome, p.data_pedido;

-- Exercício 5: Último pedido de cada cliente
WITH ordenado AS (
	SELECT
		c.nome,
		p.valor,
		p.data_pedido,
		ROW_NUMBER() OVER (
			PARTITION BY c.id
			ORDER BY p.data_pedido DESC
	) AS ordem
	FROM clientes c
	JOIN pedidos p ON c.id = p.cliente_id
)
SELECT
	o.nome,
	o.data_pedido,
	o.valor
FROM ordenado o
WHERE ordem = 1;





