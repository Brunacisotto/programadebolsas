--- exercicio3

Select Count (t1.editora) as quantidade, t2.nome as nome, t3.estado, t3.cidade
from livro as t1
join editora as t2
on t1.editora = t2.codeditora
left join endereco as t3
on t2.endereco = t3.codendereco
group by t2.nome, t3.estado, t3.cidade
Order by Quantidade desc
limit 5;
