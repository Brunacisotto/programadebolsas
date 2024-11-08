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
CREATE VIEW fato_locacao AS
SELECT 
    l.idLocacao AS idLocacao,
    l.idCliente AS idCliente,
    l.idCarro AS idCarro,
    l.idVendedor AS idVendedor,
    l.dataLocacao AS dataLocacao,
    l.horaLocacao AS horaLocacao,
    l.qtdDiaria AS qtdDiaria,
    l.vlrDiaria AS vlrDiaria, 
    l.dataEntrega AS dataEntrega,
    l.horaEntrega AS horaEntrega
FROM 
    tb_locacao l
JOIN 
    dim_veiculo ve ON l.idCarro = ve.idCarro
JOIN 
    dim_cliente c ON l.idCliente = c.idCliente
JOIN 
    dim_vendedor vdr ON l.idVendedor = vdr.idVendedor;

      