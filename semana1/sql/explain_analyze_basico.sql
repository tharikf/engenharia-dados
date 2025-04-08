
-- Utilizando EXPLAIN e ANALYZE

/*
EXPLAIN mostra o plano de execução de uma query — ou seja, como o PostgreSQL pretende buscar os dados.
EXPLAIN ANALYZE executa de fato a query e mostra.

Se sua query está lenta, EXPLAIN ANALYZE ajuda a entender o motivo exato. Com ele você vê:
	* Se o PostgreSQL está usando ou ignorando índices.
	* Se está lendo linhas demais (Scan completo).
	* Onde está o gargalo.

SET enable_seqscan = off; Pode forçar a utilizar o index scan mesmo em poucas linhas. (Nunca use em produção, apenas testes).

*/


EXPLAIN ANALYZE
SELECT * FROM pedidos
WHERE cliente_id = 1;

/*
Sequential Scan, ou varredura completa da tabela - mesmo sendo poucos dados, isso pode ser ruim em bases grandes.
*/

-- Criando índice para utilizar ele na consulta
DROP INDEX idx_pedidos_cliente_id;
CREATE INDEX idx_pedidos_cliente_id ON pedidos(cliente_id);

-- Para forçar a execução do index scan.
SET enable_seqscan = OFF;

EXPLAIN ANALYZE
SELECT * FROM pedidos
WHERE cliente_id = 1;

/*
Index Scan é mais rápido pois o POsgreSQL vai direto nas linhas certas.
*/

EXPLAIN ANALYZE
SELECT
	c.nome,
	p.valor
FROM pedidos p
JOIN clientes c ON p.cliente_id = c.id
WHERE c.cidade = 'São Paulo';


-- Otimizando
CREATE INDEX idx_clientes_cidade ON clientes(cidade);

EXPLAIN ANALYZE
SELECT
  cliente_id,
  data_pedido,
  valor,
  AVG(valor) OVER (PARTITION BY cliente_id ORDER BY data_pedido ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS media_movel
FROM pedidos;











