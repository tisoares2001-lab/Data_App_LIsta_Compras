import streamlit as st
import pandas as pd
import sqlalchemy 
import datetime

# 1. Primeiro criamos o engine e lemos a query
engine = sqlalchemy.create_engine("sqlite:///database.db")

with open("query_inteligente.sql") as query_file:
    query = query_file.read()

try:
    col, _ = st.columns(2)

    numero_dias_adiante = col.number_input("Dias sem voltar ao mercado adiante",
                                          min_value=0,
                                          max_value=60,
                                          step=1)


    df_stats = pd.read_sql(query, engine)
    df_stats["comprar"] = df_stats["dias_desde_ultima_compra"] + numero_dias_adiante > df_stats["avg_dias_entre_compras"]   

    df_compra = df_stats[df_stats["comprar"]]

except Exception as err:
    print(f"Erro ao executar a query;DF vazio: {err}")
    df_stats = pd.DataFrame()  # Cria um DataFrame vazio em caso de erro



# 2. Depois configuramos a página e mostramos os dados na tela
st.set_page_config(page_title="Lista Inteligente")
st.markdown("# Lista de Compras Inteligente!")
st.markdown("## Importar histórico de compras")

if df_stats.shape[0] == 0:
    st.warning("Nenhum dado historico suficiente para gerar estatísticas. Por favor, registre alguns dados primeiro.")
else:   
    st.dataframe(df_compra)

produtos = df_compra["produto"].unique().tolist() 
st.markdown("##Adicionar Compra")
produtos.sort()
produto = st.selectbox("Produto", options=["Novo Produto"] + produtos)
valor = st.number_input("Valor", min_value=0.01)

if st.button("Registrar Compra"):
    data = {
        "dt_compra": datetime.datetime.now().strftime("%Y-%m-%d"),
        "produto": produto.title(),
        "valor_produto": valor,
    }

    df_insert = pd.DataFrame([data])
    df_insert.to_sql("compras", engine, if_exists="append", index=False)
    st.success("Compra do produto registrada com sucesso!")



if produto == "Novo Produto":
    produto_novo = st.text_input("Novo Produto")
    produto = produto_novo

open_file = st.file_uploader("Escolha um arquivo CSV/histórico", type="csv")

if open_file:
    df = pd.read_csv(open_file)
    df = st.data_editor(df, use_container_width=True)

    if st.button("Registrar Dados"):
        df.to_sql("compras", engine, if_exists="append", index=False)
        st.success("Dados registrados com sucesso!")