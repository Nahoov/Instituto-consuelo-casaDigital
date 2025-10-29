--Liste todos os clientes cadastrados. 💡 Dica: SELECT simples na tabela Clientes
SELECT * FROM cliente;

--Liste todos os produtos da categoria "Acessórios". 💡 Dica: WHERE com filtro de categoria
SELECT 
    p.nome_produto,
    c.nome_categoria
FROM produto p
JOIN categoria c ON p.categoriaID = c.categoriaID
WHERE c.nome_categoria = 'Acessórios'


--Mostre todos os pedidos feitos por Ana Silva. 💡 Dica: JOIN entre Clientes e Pedidos + filtro no nome
SELECT 
    c.nome_cliente,
    p.pedidoid
FROM pedido p
JOIN cliente c ON p.clienteID = c.clienteID
WHERE c.nome_cliente = 'Ana Silva';


--Liste os clientes que já compraram mais de um tipo diferente de produto. 💡 Dica: COUNT(DISTINCT ProdutoID) > 1
SELECT
    c.nome_cliente,
    COUNT(p.pedidoID) AS quantidade_pedidos,
    COUNT(DISTINCT ip.produtoID) > 1 AS produtos_diferentes
FROM produto prdt
JOIN item_pedido ip ON ip.produtoID = prdt.produtoID
JOIN pedido p ON ip.pedidoID = p.pedidoID
JOIN cliente c ON p.clienteID = c.clienteID
GROUP BY nome_cliente

--Mostre os pedidos cujo valor total foi acima de R$ 3000. 💡 Dica: Use a consulta do exercício 4 + HAVING

SELECT
    p.pedidoID,
    SUM(ip.preco_unitario * ip.quantidade_escolhida) AS valor_total
FROM pedido p
JOIN item_pedido ip ON ip.pedidoID = p.pedidoID
GROUP BY p.pedidoid
HAVING SUM (ip.preco_unitario * ip.quantidade_escolhida) >= 3000

--Calcule o ticket médio dos clientes (média de valor gasto por pedido). 💡 Dica: AVG() da soma dos subtotais

--Maneira que fiz e não deu muito certo /////////////////
SELECT 
    c.nome_cliente,
    p.pedidoID,
    SUM(ip.preco_unitario * ip.quantidade_escolhida) AS valor_total
    AVG(valor_total) AS media_por_pedido
FROM cliente c
JOIN pedido p ON p.clienteID = c.clienteID
JOIN item_pedido ip ON ip.pedidoID = p.pedidoID
GROUP BY c.nome_cliente

-- maneira melhor e assertiva ////////////////

WITH total_por_pedido AS (
    SELECT 
        p.clienteID,
        p.pedidoID,
        SUM(ip.preco_unitario * ip.quantidade_escolhida) AS valor_total_pedido
    FROM pedido p
    JOIN item_pedido ip ON ip.pedidoID = p.pedidoID
    GROUP BY p.clienteID, p.pedidoID
)
SELECT 
    c.nome_cliente,
    ROUND(AVG(tpp.valor_total_pedido), 2) AS ticket_medio
FROM cliente c
JOIN total_por_pedido tpp ON tpp.clienteID = c.clienteID
GROUP BY c.nome_cliente
ORDER BY ticket_medio DESC;
         
    

--Liste os clientes que nunca fizeram pedidos. 💡 Dica: LEFT JOIN + WHERE campo IS NULL
SELECT 
    c.nome_cliente,
    p.pedidoID
FROM cliente c
LEFT JOIN pedido p ON p.clienteID = c.clienteID
WHERE p.pedidoID IS NULL