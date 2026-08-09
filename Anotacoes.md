# Resumo do Projeto: Data App de Lista de Compras Inteligente

Desenvolvimento de uma aplicação de dados voltada para prever a necessidade de recompra de itens com base no histórico de consumo do usuário, utilizando **Python** e **Streamlit**.

---

## 1. Configuração do Ambiente e Ferramentas

* **Conda:** Utilizado como gerenciador de ambientes virtuais para isolar as dependências do projeto.
  * *Comandos principais:*
    ```bash
    conda create --name lista-app python=3.13
    conda activate lista-app
    ```
  * **Nota de Inicialização:** Sempre que desligar e iniciar o computador novamente, é necessário reativar o ambiente virtual antes de rodar o projeto:
    ```bash
    conda activate lista-app
    ```
  * **Instalação de Dependências:** Caso necessário instalar o gerenciador de pacotes no ambiente:
    ```bash
    cd Data_App_LIsta_Compras
    conda install pip -y
    ```
* **VS Code:** Editor utilizado para estruturar o projeto e criar o script principal (`main.py`).
* **Streamlit:** Biblioteca em Python para criação de aplicações web interativas e data apps de forma rápida.
* **Pandas:** Biblioteca essencial para carregamento, manipulação e análise de dados tabulares.

---

## 2. Desenvolvimento da Aplicação

* **Interface de Importação:** Implementação de um componente para o usuário realizar o upload de arquivos CSV contendo o histórico de compras.
* **Exibição de Dados:** Apresentação interativa dos dados na tela para visualização e validação inicial.
* **Persistência de Dados (Banco de Dados Local):** 
  * Configuração de uma conexão com um banco de dados local (**SQLite** via **SQLAlchemy**).
  * Salvamento automático dos dados enviados via planilha para o banco relacional.
* **Integração de Consultas:** Importação e execução de queries SQL estruturadas para processar e exibir os dados dinamicamente na interface web.

---

## 3. Análise, Inteligência de Dados e Lógica de Compra

* **Análise de Recorrência:** Avaliação do padrão de compra por produto para determinar a frequência média de reposição.
* **Cálculo de Intervalos (`julianday`):** Uso de funções SQL para calcular a diferença em dias entre compras sucessivas de um mesmo produto (`dias_entre_compras`), permitindo prever o momento ideal de reposição.
* **Marcação Inteligente (Status de Compra):** 
  * Implementação de uma lógica condicional baseada na data da última compra versus a média de intervalo de consumo.
  * O sistema gera uma **marcação visual (flag)** que indica automaticamente se o item precisa ser comprado ou se o estoque atual é suficiente.
* **Integração Futura:** Planejamento para exportação e conexão com **Power BI** visando a construção de dashboards analíticos avançados sobre os padrões de consumo coletados.