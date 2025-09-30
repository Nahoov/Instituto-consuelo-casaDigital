# Exercícios semana 1

**Aluna**: Nahomi Lexamar Ribas Rodriguez

## 2. Script SQL Prático
```
-- CRIANDO TABELAS

CREATE TEABLE categorias(
id_categoria SERIAL PRIMARY KEY,
nome_categoria VARCHAR(25)
);

CREATE TABLE produtos (
id_produto SERIAL PRIMARY KEY,
nome_produto VARCHAR(25),
preco_produto DECIMAL(10,2),
estoque INT,
id_categoria INTEGER,
FOREIGN KEY(id_categoria) REFERENCES categorias(id_categoria)
);
-- INSERINDO VALORES NAS TABELAS

INSERT INTO categorias(nome_categoria) VALUES 
('Higiene'),
('Maquiagem'),
('Bebidas'),
('Remedio'),
('Doce');

INSERT INTO produtos(nome_produto, preco_produto, estoque, id_categoria) VALUES
('Agua', 3.99, 20, 3),
('Base', 20.99, 10, 2),
('Shampoo Elselve', 18.99, 10, 1),
('Dipirona', 11.99, 31, 4),
('Pasta Colgate', 12.99, 15, 1);

-- Aqui conferi se estava tudo correto com as tabelas.
SELECT * FROM produtos;

SELECT * FROM categorias;

--WHERE
-- Desta forma consultei na tabela "produtos", produtos com preço maior que 18 reais.
SELECT * FROM produtos WHERE preco_produto > 18;


-- Desta forma consultei na tabela "produtos", produtos que estão na categoria Higiene.
SELECT * FROM produtos WHERE id_categoria = 1;


-- Aqui estou consultando na tabela "produtos", todos os produtos que iniciam com a letra D.
SELECT * FROM produtos WHERE nome_produto LIKE 'D%';

--ORDER BY
--Com ORDER BY DESC, consigo conferir os últimos registro da lista, pois coloquei o ID em ordem descrescente.
SELECT * FROM produtos ORDER BY id_produto DESC;

--JOIN
-- Aqui selecionei a coluna do "nome_produto" e a coluna do "nome de categoria",
--de tabelas diferentes. Assim consigo visualizar somentes essas duas colunas, 
-- quando executar o INNER JOIN, visualizando os produtos e suas respectivas categorias.
SELECT p.nome_produto, c.nome_categoria 
FROM produtos p 
INNER JOIN categorias c ON p.id_categoria = c.id_categoria;
```