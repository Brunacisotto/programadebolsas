--- exercicio6

SELECT LIVRO.autor AS codautor, AUT.nome AS nome, COUNT(LIVRO.autor) AS quantidade_publicacoes 
FROM AUTOR AS AUT
INNER JOIN LIVRO AS LIVRO
ON AUT.codautor = LIVRO.autor
GROUP BY AUT.nome, LIVRO.autor
ORDER BY quantidade_publicacoes DESC
LIMIT 1;