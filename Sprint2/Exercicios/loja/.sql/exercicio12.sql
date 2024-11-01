-- exercicio12

SELECT dependente.cddep, dependente.nmdep, dependente.dtnasc, total_vendas.valor_total_vendas
FROM tbdependente AS dependente
JOIN tbvendedor AS vendedor ON dependente.cdvdd = vendedor.cdvdd
JOIN (SELECT vendas.cdvdd, 
        SUM(vendas.qtd * vendas.vrunt) AS valor_total_vendas
    FROM tbvendas AS vendas
    WHERE vendas.status = 'Concluído'
    GROUP BY vendas.cdvdd
    ORDER BY valor_total_vendas ASC
    LIMIT 1) 
AS total_vendas ON vendedor.cdvdd = total_vendas.cdvdd;