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
* **VS Code:** Editor utilizado para estruturar o projeto e criar o script principal (`main.py`).
* **Streamlit:** Biblioteca em Python que permite criar aplicações web interativas e data apps de forma rápida, sem a necessidade de escrever código em HTML, CSS ou JavaScript.
* **Pandas:** Biblioteca essencial para carregamento, manipulação e análise de dados tabulares.

---

## 2. Desenvolvimento da Aplicação

* **Interface de Importação:** Implementação de um componente para o usuário fazer o upload de arquivos CSV contendo o histórico de compras.
* **Exibição de Dados:** Apresentação interativa dos dados na tela para visualização e validação inicial pelo usuário.
* **Persistência de Dados (Banco de Dados Local):** 
  * Configuração de uma conexão com um banco de dados local (**SQLite** via **SQLAlchemy**).
  * Salvamento automático dos dados enviados pelas planilhas para o banco relacional.

---

## 3. Análise e Inteligência de Dados

* **Análise de Recorrência:** Avaliação do padrão de compra por produto para entender a frequência de reposição.
* **Cálculo de Intervalos (`julianday`):** Uso de funções SQL para calcular a diferença em dias entre as compras de um mesmo produto (`dias_entre_compras`), permitindo prever o momento ideal de recompra.
* **Integração Futura:** Planejamento de uso do **Power BI** para a construção de dashboards analíticos avançados sobre os dados coletados.
