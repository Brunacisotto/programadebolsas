
--- os 10 livros mais caros
SELECT liv.cod AS Codlivro, liv.titulo AS Titulo, liv.autor AS CodAutor, aut.nome AS NomeAutor, liv.valor AS Valor, liv.editora AS CodEditora, edit.nome AS NomeEditora 
FROM livro AS liv
INNER JOIN editora AS edit
ON liv.editora = edit.codeditora 
INNER JOIN autor AS aut 
ON aut.codautor = liv.autor 
ORDER BY liv.valor DESC 
LIMIT 10

----- as cinco maiores editora 
SELECT edit.codeditora AS CodEditora, edit.nome AS NomeEditora, 
    COUNT(liv.cod) AS QuantidadeLivros
FROM editora AS edit
LEFT JOIN livro AS liv 
ON edit.codeditora = liv.editora
GROUP BY edit.codeditora, edit.nome
ORDER BY QuantidadeLivros DESC
LIMIT 5;
