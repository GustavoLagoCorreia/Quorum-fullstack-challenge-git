### 1. Discuta sua estratégia e suas decisões ao implementar o aplicativo. Leve em consideração o tempo
complexidade, custo do esforço, tecnologias usadas e qualquer outra variável que você considere
importante em seu processo de desenvolvimento.

```bash
R: 
    Minha estratégia foi criar um aplicativo de forma rápida, mas eficiente, mostrando para o usuário o que ele procura de forma efetiva e sem muita complexidade.

    Usei o Python juntamente com o Flask, pois em questão de segundos posso fazer uma API. Utilize a biblioteca Pandas por ser uma ferramenta muito poderosa para manipulações de dados de forma rápida e leve, pois acredito que quanto menos o cliente esperar para carregar a página com os dados, melhor. Poderia ter utilizado outras linguagens mais robustas para o front-end e ter feito mais coisas para impressionar o cliente de forma visual, mas como prezei pela agilidade e facilidade, usei HTML com JavaScript e Jinja2 para poder exibir as informações de forma rápida, leve e fácil para o usuário.

    O design foi feito para não confundir o cliente que acessar, deixando-o o mais simples possível, para que ele possa se preocupar com outras coisas, ao invés de como chegar a um local para obter a resposta que precisa.
```

### 2. Como você mudaria sua solução para levar em conta futuras colunas que possam ser solicitadas, como “Bill Voted On Date” (Projeto de lei votado na data) ou “Co-Sponsors” (Co-patrocinadores)?

```bash
R: Mudaria o filtro do Pandas para que os novos campos não sejam excluídos e, de forma rápida e simples, os inseriria no código HTML usando o Jinja2.
```

### 3. Como você mudaria sua solução se, em vez de receber CSVs de dados, você recebesse uma lista de legisladores ou projetos de lei para os quais você deveria gerar um CSV?

```bash
R: Caso continuasse com a mesma regra de negócios, iria mesclar as listas de legisladores ou projetos de leis através do DataFrame para que fiquem em apenas uma variável e usaria a função to_csv do Pandas para gerar o CSV dessas listas. Caso precise gerar uma separada da outra, usaria o comando duas vezes.
```

### 4. Quanto tempo você gastou trabalhando na tarefa?

```bash
R: O tempo gasto pesquisando, codificando, pensando e testando a aplicação para que a tarefa chegasse ao final, de forma a responder a todos os requisitos propostos e perguntas do desafio, foi, ao todo, de 8 horas de trabalho ao longo de 2 dias.
```
