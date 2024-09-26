'''
1 - Objetivo - 
    1. Build a web application (ex. a Django web application)
    2. Provide the information that the client needs
    3. Choose the best way to display this information.
        a. For example, both questions can be answered with simple tables.
        b. You to decide how much creativity and effort you would like to put into the solution. You are free to use any UI elements that you want.      
2 - URL Base - LocalHost
3 - Endpoints
        localhost/bills (GET)
        localhost/legislators (GET)
        localhost/votes (GET)
        localhost/vote_results (GET)
        localhost/upload_new_datas (POST)

4 - Quais Recursos
        votos
'''


# Challenge Full Stack - Quorum

![Quorum](.templates/src/images/Quorum_full_color_dark.png)

Este repositório contém a solução para o desafio de [Full stack da Quorum] Eu utilizei o Framework Python e Html para desenvolver a aplicação

## 📖 Sobre o desafio

A Quorum, atuando no segmento de Legislaçoes, passou por várias mudanças desde de sua fundação. Foi necessário desenvolver metodos mais ageis e de facil consulta para seus clientes conseguirem ver sobre as ultimas votas e quais os assuntos sobre elas. 

Neste desafio, foi implementado as seguintes funcionalidades de acordo com as regras de negócio definidas:

### Funcionalidades
[x] Carrega massa de dados através dos arquivos CSV.
[x] Fazer a manipulação e a contagem votos para cada lei e para cada lesgilador.
[x] filtrar por tabelas que queiram ver.
[x] Listagem das leis, lesgiladores e votos em cada lei.

### Regras de negócio
- Para cada legislador disponível, quantos projetos de lei o legislador apoiou (votou a favor do projeto de lei).
- Quantos projetos de lei o legislador se opôs.
- Para cada projeto de lei disponível, quantos legisladores apoiaram o projeto de lei.
- Quantos legisladores se opuseram ao projeto de lei.
- Quem foi o patrocinador principal do projeto de lei.

## 🎨 Layout

O layout da aplicação foi baseado nos materiais disponibilizados, incluindo designs para dispositivos móveis e desktop, cores, imagens e fontes. A aplicação é responsiva para dispositivos móveis, tablets e desktops.

## ⚙️ Como Executar

Para executar a aplicação localmente, siga os passos abaixo:

1. Clone este repositório:

```bash
  git clone https://github.com/Fernanda-Kipper/smartfit-frontend-challenge.git
  cd Quorum-fullstack-challenge-git

```

2. Instale as dependências

```bash
  pip install -r requerinments.txt
```

3. Inicie a aplicação

```bash
  python app.py
```
