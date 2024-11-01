--- exercicio5

SELECT 
DISTINCT nome.nome 
FROM endereco AS estado
INNER JOIN editora AS edit
ON edit.endereco = estado.codendereco
INNER JOIN livro AS AUTORcod
ON edit.codeditora = AUTORcod.editora 
INNER JOIN autor AS nome
ON nome.codautor = Autorcod.autor
WHERE ESTADO <> 'PARANÁ' OR 'SANTA CATARINA' OR 'RIO GRANDE DO SUL'
ORDER BY nome.nome ASC 