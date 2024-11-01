-- exercicio10

SELECT vendedor.nmvdd AS vendedor, 
SUM(vendas.qtd * vendas.vrunt) AS valor_total_vendas,
ROUND(SUM(vendas.qtd * vendas.vrunt) * COALESCE(vendedor.perccomissao, 0) / 100, 2) AS comissao
FROM tbvendas AS vendas
INNER JOIN tbvendedor AS vendedor 
ON vendas.cdvdd = vendedor.cdvdd
WHERE vendas.status = 'Concluído'
GROUP BY vendedor.nmvdd
ORDER BY comissao DESC;