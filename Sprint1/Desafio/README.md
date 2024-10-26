# Desafio

O desafio proposto era, com base em um relatório de vendas fornecido, criar um **arquivo executável** que, todos os dias, por 4 dias seguidos às 15:27, criasse dentro da pasta `vendas/backup`:

1. Um arquivo chamado **backup dados**, que deveria ser **zipado**. Esse arquivo conteria a **lista base** nele.
2. Na mesma pasta, deveria ser criado um arquivo chamado **relatório** procedido pela **data do dia da execução**.

## O arquivo relatório precisava conter:
- A **data e o horário da execução**.
- As **datas do primeiro e do último registro de vendas**.
- A **quantidade de itens diferentes vendidos**.
- As **10 primeiras linhas** do relatório original.

### Detalhes Adicionais:
- Todos os dias, era necessário **mudar manualmente o relatório de vendas original** para ter itens diferentes do relatório do dia anterior.  
- Após os 4 dias de execução, era necessário criar **um segundo script** para **unificar os 4 relatórios** gerados em um só, com o nome de **relatório final**.

---

## Etapas do Desenvolvimento

### **Etapa 1**  
Criação do diretório e cópia do arquivo original:  
![Criação do Diretório](https://github.com/Brunacisotto/programadebolsas/blob/main/Sprint1/Evidencias/printsexecucao/01criacaodiretorio.png)

---

### **Etapa 2**  
Criação dos diretórios e arquivos, e renomeação conforme solicitado:  
![Criação e Renomeação](https://github.com/Brunacisotto/programadebolsas/blob/main/Sprint1/Evidencias/printsexecucao/scriptdetalhado/detalhescript.png)

---

### **Etapa 3**  
Renomeação dos arquivos de **backup** e **relatório** com a data.  
Programação para exibir:
- Data do primeiro e último registro de vendas.
- As 10 primeiras linhas do relatório original.
- A quantidade de itens diferentes vendidos.  

![Estruturando Relatório](https://github.com/Brunacisotto/programadebolsas/blob/main/Sprint1/Evidencias/printsexecucao/scriptdetalhado/estruturandorelatorio.png)

---

### **Etapa 4**  
Compactação dos arquivos e exclusão dos arquivos desnecessários:  
![Compactação e Limpeza](https://github.com/Brunacisotto/programadebolsas/blob/main/Sprint1/Evidencias/printsexecucao/scriptdetalhado/final.png)

---

### **Etapa 5**  
Concessão de permissões de execução:  
![Permissões](https://github.com/Brunacisotto/programadebolsas/blob/main/Sprint1/Evidencias/printsexecucao/03permissoes.png)

---

### **Etapa 6**  
Programação do **Crontab** para execução automática:  
![Crontab Programado](https://github.com/Brunacisotto/programadebolsas/blob/main/Sprint1/Evidencias/printsexecucao/04crontab.png)

---

### **Etapa 7**  
Execução do **Crontab**:  
![Execução do Crontab](https://github.com/Brunacisotto/programadebolsas/blob/main/Sprint1/Evidencias/printsexecucao/05execucaocrontab.png)

---

### **Etapa 8**  
Criação do script para **consolidar os relatórios** gerados e ajustando permissões:  
![Script Consolidador](https://github.com/Brunacisotto/programadebolsas/blob/main/Sprint1/Evidencias/printsexecucao/06scriptconsolidador.png)
![Consolidador](https://github.com/Brunacisotto/programadebolsas/blob/main/Sprint1/Evidencias/printsexecucao/07gerandoconsolidador.png)

### Etapa 9 (Final)

Após rodar por 4 dias e ter o consolidador executado, este foi o resultado:

![Estrutura Ecommerce](https://github.com/Brunacisotto/programadebolsas/blob/main/Sprint1/Evidencias/printdaestruturadiretorios/1ecommerce.png)  
![Estrutura Vendas](https://github.com/Brunacisotto/programadebolsas/blob/main/Sprint1/Evidencias/printdaestruturadiretorios/2vendas.png)  
![Estrutura Backup](https://github.com/Brunacisotto/programadebolsas/blob/main/Sprint1/Evidencias/printdaestruturadiretorios/3backup.png)  
![Arquivos de Backup e Relatórios](https://github.com/Brunacisotto/programadebolsas/blob/main/Sprint1/Evidencias/printdaestruturadiretorios/4arquivosbackuperelatorios.png)

### Relatórios Gerados
Os relatórios gerados podem ser acessados no link abaixo:  
[Relatórios Gerados](https://github.com/Brunacisotto/programadebolsas/tree/main/Sprint1/Evidencias/arquivosgerados)


## Acesso aos Arquivos

Os **scripts** (arquivos `.sh`) e os **relatórios gerados** nas execuções (relatórios e backups) estão disponíveis para correção na pasta abaixo, nela segui a estrutura de diretórios proposto no desafio:  
[Relatórios e Backups](https://github.com/Brunacisotto/programadebolsas/tree/main/Sprint1/Desafio/ecommerce)


## Observação
No primeiro dia, tive um problema com o **Crontab**, e por isso o horário do relatório foi gerado com alguns minutos de atraso.



