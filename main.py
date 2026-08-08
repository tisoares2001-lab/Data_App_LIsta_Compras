import streamlit as st
import pandas as pd
import sqlalchemy 

engine = sqlalchemy.create_engine("sqlite:///database.db")

st.set_page_config(page_title="Lista Inteligente")
st.markdown("# Lista de Compras Inteligente!")
st.markdown("## Importar histórico de compras")

open_file = st.file_uploader("Escolha um arquivo CSV/histórico", type="csv")

if open_file:
    df = pd.read_csv(open_file)
    df = st.data_editor(df, use_container_width=True)

    if st.button("Registrar Dados"):
        df.to_sql("compras", engine, if_exists="append", index=False)
        st.success("Dados registrados com sucesso!")