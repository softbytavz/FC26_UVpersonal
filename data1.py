import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt 
import numpy as np

@st.cache_data
def load_data(nrows=6820):
    return pd.read_csv("https://raw.githubusercontent.com/softbytavz/FC26dataset/refs/heads/main/FC26_Data.csv",nrows=nrows,encoding="latin-1")

FC26_data = load_data()

st.header("FC 26 data")
st.dataframe(FC26_data)

if st.sidebar.checkbox("Mostrar todos los datos"):
    st.subheader("Todos los datos")
    st.write(f"Total filmes: {len(FC26_data)}")
    st.dataframe(FC26_data)

def filtrar_por_posicion(df, texto):
    return df[df["name"].str.contains(texto, case=False, na=False, regex=False)]

titulo = st.sidebar.text_input("Posición del jugador:")
if st.sidebar.button("Buscar por posición"):
    resultado = filtrar_por_posicion(FC26_data, posiciones)
    st.subheader("Resultado de la busqueda")
    st.write(f"Total de posiciones,{resultado.shape[0]}")
    st.dataframe(resultado)


