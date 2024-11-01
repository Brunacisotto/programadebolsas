-- exercicio14

SELECT estado, 
    ROUND(AVG(qtd * vrunt), 2) AS gastomedio
FROM tbvendas
WHERE status = 'Concluído' 
GROUP BY estado 
order by gastomedio DESC 