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

--ainda vou fazer


--Liste os clientes que já compraram mais de um tipo diferente de produto. 💡 Dica: COUNT(DISTINCT ProdutoID) > 1


--ainda vou fazer

--Mostre os pedidos cujo valor total foi acima de R$ 3000. 💡 Dica: Use a consulta do exercício 4 + HAVING

--ainda vou fazer


--Calcule o ticket médio dos clientes (média de valor gasto por pedido). 💡 Dica: AVG() da soma dos subtotais

--ainda vou fazer


--Liste os clientes que nunca fizeram pedidos. 💡 Dica: LEFT JOIN + WHERE campo IS NULL