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
    quantidade INT NOT NULL,
    categoriaID INT,
    FOREIGN KEY(categoriaID) REFERENCES categoria(categoriaID)

);

CREATE TABLE vendedor(
    vendedorID SERIAL PRIMARY KEY,
    nome_vendedor VARCHAR(40)
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
    quantidade INT NOT NULL,
    preco_unitario DECIMAL (5,2) NOT NULL,
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

-- Para visualizar nome do cliente, pedido e produto

-- visualizar estoque de cada producto

-- visualizar qual vendedor fez qual venda

-- visualizar nome da categoria dos produtos

-- qual produto é mais vendido

-- ver valor ganho nas vendas de um mês específico