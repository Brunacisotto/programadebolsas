-- visualizacoes
select * from dim_cliente
select * from dim_veiculo
select * from dim_vendedor
select * from fato_locacao


-- dim_cliente
CREATE VIEW dim_cliente AS
SELECT idCliente AS idCliente,
       nomeCliente AS nomeCliente,
       cidadeCliente AS cidadeCliente,
       estadoCliente as estadoCliente,
       paisCliente AS paisCliente
FROM cliente;

-- dim_vendedor
CREATE VIEW dim_vendedor AS
SELECT idVendedor AS idVendedor,
       nomeVendedor AS nomeVendedor,
       estadoVendedor as estadoVendedor,
       sexoVendedor as sexoVendedor
       FROM vendedor;

-- dim_veiculo     
CREATE VIEW dim_veiculo AS
SELECT v.idCarro AS idCarro,
       v.kmCarro AS kmCarro,
       v.classiCarro AS classiCarro,
       v.marcaCarro AS marcaCarro,
       v.modeloCarro AS modeloCarro,
       v.anoCarro AS anoCarro,
       v.idCombustivel AS idCombustivel,
       c.tipoCombustivel AS tipoCombustivel
FROM veiculo v
JOIN combustivel c ON v.idCombustivel = c.idCombustivel;
      
-- tabelafato
create view fato_locacao as
select idLocacao as idLocacao,
	   idCliente as idCliente,
       idCarro as idCarro,
       idVendedor as idVendedor,
       dataLocacao as dataLocacao,
       horaLocacao as horaLocacao,
       qtdDiaria as qtdDiaria,
       vlrDiaria as vlrDiaria, 
       dataEntrega as dataEntrega,
       horaEntrega as horaEntrega
       from tb_locacao
       
    

      