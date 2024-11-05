-- exercicio9

SELECT cdpro, nmpro
FROM (SELECT tbvendas.cdpro, tbvendas.nmpro, 
        COUNT(tbvendas.nmpro) AS quantidadevendida
        FROM tbvendas
        WHERE tbvendas.dtven BETWEEN '2014-02-03' AND '2018-02-02' 
        AND tbvendas.status = 'Concluído'
        GROUP BY tbvendas.cdpro, tbvendas.nmpro) 
AS subconsulta
ORDER BY quantidadevendida desc
LIMIT 1;