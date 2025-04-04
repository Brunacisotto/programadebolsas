# Desafio - Sprint 2

Nesta sprint, o desafio foi aplicar as formas normais a uma base de dados e, posteriormente, converter o modelo relacional em dimensional. Confesso que todos esses conceitos são novos para mim, o que tornou a tarefa desafiadora. Contudo, dediquei-me para compreender e executar o desafio da melhor forma possível. A seguir, explico os passos que segui para sua realização e espero que minha explicação seja clara.

## Primeira Etapa: Normalização e modelagem Relacional

Para trabalhar nesse desafio usei o MySQL workbench.
Inicialmente, fiz um tratamento dos dados da tabela, pois alguns campos de data e hora não estavam configurados corretamente. Aproveitei essa etapa para revisar todos os campos e ajustá-los para garantir consistência. As imagens a seguir ilustram essas alterações:

![normalizacao](../Evidencias/Desafio-Relacional/tratamentodados.png)
![normalizacao](../Evidencias/Desafio-Relacional/tratamentodados2.png)

Após essa revisão, comecei a criar tabelas específicas para cada entidade — **cliente**, **veículo**, **combustível** e **vendedor** — e transferi para cada uma delas os dados correspondentes.

### 1. Tabela de Clientes

Para a tabela de clientes, criei uma estrutura onde o campo `idCliente` atua como chave primária. Todos os atributos relacionados aos clientes foram transferidos para esta tabela. Depois, eliminei os dados repetidos na tabela **locação**, conforme exigido no processo de normalização. Também defini `idCliente` como chave estrangeira na tabela **locação** para manter a integridade dos dados, como mostrado na imagem abaixo:

![codigocliente](../Evidencias/Desafio-Relacional/cliente.png)

tabela gerada após a execução do código: 

![resultadocliente](../Evidencias/Desafio-Relacional/tbcliente.png)

### 2. Tabela de Vendedores

Segui o mesmo procedimento para a tabela de vendedores: `idVendedor` foi definido como chave primária, e todos os atributos relacionados a vendedores foram transferidos para esta tabela. Após a transferência, removi os dados redundantes da tabela **locação** e estabeleci `idVendedor` como chave estrangeira na tabela **locação**, conforme ilustrado na imagem:

![codigovendedor](../Evidencias/Desafio-Relacional/vendedor.png)

tabela gerada após a execução do código: 

![resultadovendedor](../Evidencias/Desafio-Relacional/tbvendedor.png)

### 3. Tabela de Combustível e Tabela de Veículo

Para a tabela de **combustível**, criei uma estrutura que contém `idCombustivel` e `tipoCombustivel`. Em seguida, criei a tabela **veículo**, incluindo os atributos relacionados aos veículos, e estabeleci uma relação entre essas tabelas usando `idCombustivel`.

Na tabela de veículos, utilizei `idCarro` como chave primária e escolhi manter apenas a quilometragem mais alta registrada para cada carro, evitando duplicidade de dados. Depois disso, removi os dados redundantes da tabela **locação** e excluí `idCombustivel` dela, uma vez que **combustível** está relacionado apenas a **veículo** e não diretamente a **locação**.

As imagens a seguir ilustram essa estrutura:

![codigocombustivel](../Evidencias/Desafio-Relacional/combustivel.png)

tabela gerada após a execução do código: 

![resultadocombustivel](../Evidencias/Desafio-Relacional/tbcombustivel.png)

![codigoveiculo](../Evidencias/Desafio-Relacional/veiculo.png)
![codigoveiculo](../Evidencias/Desafio-Relacional/veiculo2.png)

tabela gerada após a execução do código: 
![resultadoveiculo](../Evidencias/Desafio-Relacional/tbcarro.png)
---

Esse processo de normalização ajudou a garantir uma estrutura de dados consistente e evitou a redundância de informações na base de dados.
Gerando a seguinte tabela locação:

![locacao](../Evidencias/Desafio-Relacional/tblocacao1.png)
![locacao](../Evidencias/Desafio-Relacional/tblocacao2.png)

## Resultado do Modelo Relacional

Por fim, o modelo relacional finalizado está representado na imagem abaixo.

![modelorelacional](../Evidencias/Desafio-Relacional/modelorelacional.png)


## Segunda Etapa: Criação do Modelo Dimensional

Na segunda etapa, optei por criar o modelo dimensional por meio de **views**, seguindo as orientações do vídeo disponibilizado na Udemy pelo instrutor Antonio Alex.

Primeiramente, criei a **view `dim_cliente`**, que contém exatamente os mesmos dados da tabela **cliente**, considerando que todos os atributos eram relevantes para o modelo.

![viewcliente](../Evidencias/Desafio-Dimensional/dim_cliente.png)

tabela gerada após a execução da view:

![viewclientetabela](../Evidencias/Desafio-Dimensional/dimcliente.png)

Em seguida, criei a **view `dim_vendedor`**, utilizando o mesmo raciocínio aplicado na etapa anterior.

![viewvendedor](../Evidencias/Desafio-Dimensional/dim_vendedor.png)

tabela gerada após a execução da view:

![viewvendedortabela](../Evidencias/Desafio-Dimensional/dimvendedor.png)

Depois disso, desenvolvi a **view `dim_veiculo`**, na qual trouxe a quilometragem do carro e o tipo de combustível, dados que anteriormente estavam na tabela **combustível**. Considerando a estrutura do modelo dimensional, esses dados foram agrupados na **dim_veiculo** para melhor organização.

![viewveiculo](../Evidencias/Desafio-Dimensional/dim_veiculo.png)

tabela gerada após a execução da view:

![viewveiculotabela](../Evidencias/Desafio-Dimensional/dimveiculo.png)

Por fim, criei a **tabela `fato_locacao`**, que contém todos os registros numéricos necessários para o modelo, e relacionei com as demais tabelas através do Join.

![viewfato](../Evidencias/Desafio-Dimensional/fatolocacao.png)

tabela gerada após a execução da view:

![viewfatotabela](../Evidencias/Desafio-Dimensional/fato1.png)
![viewfatotabela](../Evidencias/Desafio-Dimensional/fato2.png)


Como resultado, o modelo dimensional final ficou conforme a imagem abaixo:

![modelodimensional](../Evidencias/Desafio-Dimensional/modelodimensional.png)


# Arquivos Gerados

Os códigos gerados para a execução desse desafio estão salvos na extensão .sql e podem ser encontrados aqui:

![modelorelacional](../Desafio/modelorelacional/relacionalconcessionaria.sql)
![modelodimensional](../Desafio/modelodimensional/dimensionalconcessionaria.sql)

