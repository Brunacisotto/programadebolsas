-- exercicio8

SELECT vendedor.cdvdd, vendedor.nmvdd
FROM tbvendas AS vendas
INNER JOIN tbvendedor AS vendedor 
ON vendas.cdvdd = vendedor.cdvdd
WHERE vendas.status = 'Concluído'
GROUP BY vendedor.cdvdd, vendedor.nmvdd
ORDER BY COUNT(vendas.cdvdd) DESC
LIMIT 1;
