-- exercicio13

SELECT tbvendas.cdpro, tbvendas.nmcanalvendas, tbvendas.nmpro, 
sum (qtd) AS quantidade_vendas
FROM tbvendas
WHERE tbvendas.status = 'Concluído' 
GROUP BY tbvendas.cdpro, tbvendas.nmcanalvendas, tbvendas.nmpro
ORDER BY quantidade_vendas ASC