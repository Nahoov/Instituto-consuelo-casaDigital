-- 🏠 Atividades Assíncronas (para casa)

--1. Normalizar a tabela abaixo, PedidosProblematicos até 3FN

CREATE TABLE PedidosProblematicos (
    PedidoID INT,
    ClienteNome VARCHAR(100),
    ClienteEmail VARCHAR(100),
    ClienteCidade VARCHAR(50),
    ClienteEstado VARCHAR(2),
    ClienteCEP VARCHAR(10),
    ProdutoNome VARCHAR(100),
    ProdutoCategoria VARCHAR(50),
    ProdutoPreco DECIMAL(10,2),
    Quantidade INT,
    DataPedido DATE,
    TelefonesContato VARCHAR(200), 
    NomeVendedor VARCHAR(100),     
    ComissaoVendedor DECIMAL(5,2), 
    EnderecoCompleto VARCHAR(300)
);


-- R e s p o s t a 1: tabela normalizada -------------------------------------------------------------------------------
CREATE TABLE cliente(
    clienteID SERIAL PRIMARY KEY,
    nome_cliente VARCHAR(40) NOT NULL,
    sobrenome_cliente VARCHAR(60),
    email_cliente VARCHAR(100) UNIQUE NOT NULL,
    cidade_cliente VARCHAR(60) NOT NULL,
    estado_cliente VARCHAR(60) NOT NULL,
    cep_cliente VARCHAR(10) NOT NULL
);

CREATE TABLE categoria(
    categoriaID SERIAL PRIMARY KEY,
    nome_categoria VARCHAR(60)

);

CREATE TABLE produto(
    produtoID SERIAL PRIMARY KEY,
    nome_produto VARCHAR(100) NOT NULL,
    preco_produto DECIMAL(10,2) NOT NULL,
    estoque INT NOT NULL,
    categoriaID INT,
    FOREIGN KEY(categoriaID) REFERENCES categoria(categoriaID)

);

CREATE TABLE vendedor(
    vendedorID SERIAL PRIMARY KEY,
    nome_vendedor VARCHAR(40),
    comissao_vendedor DECIMAL(5,2) NOT NULL,
    email_vendedor VARCHAR(100) UNIQUE NOT NULL,
    cidade_vendedor VARCHAR(60) NOT NULL,
    estado_vendedor VARCHAR(60) NOT NULL,
    cep_vendedor VARCHAR(10) NOT NULL   
);

CREATE TABLE pedido(
    pedidoID SERIAL PRIMARY KEY,
    data_pedido DATE NOT NULL,
    vendedorID INT,
    clienteID INT,
    FOREIGN KEY(vendedorID) REFERENCES vendedor(vendedorID),
    FOREIGN KEY(clienteID) REFERENCES cliente(clienteID)
);


CREATE TABLE item_pedido( 
    item_pedidoID SERIAL PRIMARY KEY,
    pedidoID INT,
    produtoID INT,
    quantidade_escolhida INT NOT NULL,
    preco_unitario DECIMAL (10,2) NOT NULL,
    FOREIGN KEY(pedidoID) REFERENCES pedido(pedidoID),
    FOREIGN KEY(produtoID) REFERENCES produto(produtoID)

)



CREATE TABLE telefone_cliente(
    telefone_clienteid SERIAL PRIMARY KEY,
    clienteID INT,
    primeiro_telefone VARCHAR(14) NOT NULL,
    segundo_telefone VARCHAR(14),
    FOREIGN KEY(clienteID) REFERENCES cliente(clienteID)
);


-- r e s p o s t a 2: desnormalização para relatórios----------------------------------------------

-- Para visualizar nome do cliente, pedido, produto e valor total
CREATE VIEW pedido_completo AS
SELECT 
    c.nome_cliente,
    p.pedidoid,
    prdt.nome_produto AS produto,
    SUM(ip.quantidade_escolhida) AS quantidade_vendida,
	SUM(ip.preco_unitario * ip.quantidade_escolhida) AS valor_total
FROM item_pedido ip
JOIN pedido p ON ip.pedidoID = p.pedidoID
JOIN cliente c ON p.clienteID = c.clienteID
JOIN produto prdt ON ip.produtoID = prdt.produtoID
GROUP BY c.nome_cliente,
         p.pedidoID,
         prdt.nome_produto;



-- visualizar estoque de cada produto
SELECT nome_produto, estoque FROM produto;



-- visualizar qual vendedor vendeu qual pedido
SELECT
    p.pedidoid,
    v.nome_vendedor,
    v.email_vendedor
FROM pedido p
JOIN vendedor v ON p.vendedorID = v.vendedorID


-- visualizar qual vendedor vendeu mais pedidos
CREATE VIEW ver_maior_vendedor AS
SELECT
    v.nome_vendedor,
    COUNT(p.pedidoID) AS total_vendas
FROM pedido p
JOIN vendedor v ON p.vendedorID = v.vendedorID
GROUP BY v.nome_vendedor
ORDER BY total_vendas DESC
LIMIT 3;


-- visualizar nome da categoria dos produtos
CREATE VIEW produtos_categorias AS
SELECT 
    p.nome_produto,
    c.nome_categoria
FROM produto p
JOIN categoria c ON p.categoriaID = c.categoriaID


-- qual produto é mais vendido
CREATE VIEW produto_mais_vendido AS
SELECT 
    p.nome_produto,
    SUM(ip.quantidade_escolhida) AS quantidade_vendida
FROM produto p
JOIN item_pedido ip ON ip.produtoID = p.produtoID
GROUP BY nome_produto 
ORDER BY quantidade_vendida DESC
LIMIT 3;


-- ver valor ganho nas vendas de um mês específico.
