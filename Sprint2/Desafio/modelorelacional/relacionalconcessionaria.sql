-- tratando o tipo de dados das colunas -----
alter table tb_locacao
modify dataEntrega date;
alter table tb_locacao
modify dataLocacao date;
alter table tb_locacao
modify horaEntrega time;
alter table tb_locacao
modify horaLocacao time;
alter table tb_locacao
modify nomeCliente varchar(100);
alter table tb_locacao
modify cidadeCliente varchar(40);
alter table tb_locacao
modify paisCliente varchar(40);
alter table tb_locacao
modify estadoCliente varchar(40);
alter table tb_locacao
modify vlrDiaria decimal(18,2);
alter table tb_locacao
modify nomeVendedor varchar(40);
alter table tb_locacao
modify estadoVendedor varchar(40);
alter table tb_locacao
modify idLocacao int;
alter table tb_locacao
modify idCliente int;
alter table tb_locacao
modify idCarro int;
alter table tb_locacao
modify kmCarro int;
alter table tb_locacao
modify marcaCarro varchar(30);
alter table tb_locacao
modify modeloCarro varchar(80);
alter table tb_locacao
modify idVendedor int;



-- consulta das tabelas 
select * from tb_locacao
select * from cliente
select * from veiculo
select * from combustivel
select * from vendedor





-- criando e normalizando tabela clientes ----
CREATE TABLE Cliente (idCliente INT PRIMARY KEY, nomeCliente VARCHAR(100), cidadeCliente VARCHAR(40), estadoCliente VARCHAR(40), paisCliente VARCHAR(40));
INSERT INTO Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;

ALTER TABLE tb_locacao -- deletando colunas relacionadas a cliente da tabela locacao
DROP COLUMN nomeCliente, 
DROP COLUMN cidadeCliente,
DROP COLUMN estadoCliente,
DROP COLUMN paisCliente;

ALTER TABLE tb_locacao -- identificando a chave estrangeira na tabela locacao  
ADD CONSTRAINT fk_cliente
FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente);







-- Criando e normalizando a tabela VENDEDOR ----
CREATE TABLE Vendedor (idVendedor INT PRIMARY KEY, nomeVendedor VARCHAR(40) NOT NULL, sexoVendedor Int(1), estadoVendedor VARCHAR(40));
INSERT INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;

ALTER TABLE tb_locacao -- deletando as colunas relacionadas a vendedor da tabela locacao
DROP COLUMN nomeVendedor,
DROP COLUMN sexoVendedor,
DROP COLUMN estadoVendedor;

ALTER TABLE tb_locacao -- identificando a chave estrangeira idvendedor na tabela loocacao
ADD CONSTRAINT fk_idVendedor
FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor);








-- criando e normalizando a tabela combustivel
CREATE TABLE Combustivel (idCombustivel tinyint AUTO_INCREMENT PRIMARY KEY, tipoCombustivel VARCHAR(8));
INSERT INTO Combustivel (tipoCombustivel)
SELECT DISTINCT tipoCombustivel
FROM tb_locacao










-- criando e normalizando a tabela Veiculo--

CREATE TABLE Veiculo (idCarro INT PRIMARY KEY, kmCarro INT, classiCarro VARCHAR(15), marcaCarro VARCHAR(30), modeloCarro VARCHAR(80), anoCarro smallint);
INSERT INTO Veiculo (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro)
SELECT t.idCarro, t.kmCarro, t.classiCarro, t.marcaCarro, t.modeloCarro, t.anoCarro
FROM tb_locacao 

JOIN -- trazer somente os registros que têm o valor máximo de kmCarro para cada idCarro, para não ficar com registros duplicados de carro
    (SELECT idCarro, MAX(kmCarro) AS maxKm  -- idCarro com o maior valor de kmCarro
     FROM tb_locacao
     GROUP BY idCarro) AS max_km
ON 
    t.idCarro = max_km.idCarro
    AND t.kmCarro = max_km.maxKm;

ALTER TABLE Veiculo -- criando a coluna idcombustivel (HAVIA ESQUECIDO DE CRIAR ESSA COLUNA NA CRIAÇAO DA TABELA VEICULO)
ADD idCombustivel tinyINT;
UPDATE Veiculo v
JOIN tb_locacao t ON v.idCarro = t.idCarro
AND v.kmCarro = t.kmCarro  
SET v.idCombustivel = t.idCombustivel;
 
ALTER TABLE Veiculo -- adicionando chave estrangeira a idcombustivel na tabela veiculo
ADD CONSTRAINT fk_idCombustivel 
FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel);

ALTER TABLE tb_locacao -- adicionando chave estrangeira na tabela locacao para referenciar ao id do carro
ADD CONSTRAINT fk_idCarro
FOREIGN KEY (idCarro) REFERENCES Veiculo(idCarro);

ALTER TABLE tb_locacao -- deletando as colunas repetidas da tabela locacao
DROP COLUMN kmCarro,
DROP COLUMN classiCarro,
DROP COLUMN marcaCarro,
DROP COLUMN modeloCarro,
DROP COLUMN anoCarro,
DROP COLUMN idCombustivel;
ALTER TABLE tb_locacao
DROP COLUMN tipoCombustivel;
