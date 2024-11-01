-- exercicio11

SELECT vendas.cdcli AS cdcli, vendas.nmcli AS nmcli,   
    SUM(vendas.qtd * vendas.vrunt) AS gasto 
FROM tbvendas AS vendas  
WHERE vendas.status = 'Concluído'  
GROUP BY vendas.cdcli, vendas.nmcli  
ORDER BY gasto DESC  
LIMIT 1;