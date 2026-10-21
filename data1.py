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
    st.write(f"Total de jugadores: {len(FC26_data)}")
    st.dataframe(FC26_data)

def filtrar_por_posicion(df, texto):
    return df[df["player_positions"].str.contains(texto, case=False, na=False, regex=False)]

titulo = st.sidebar.text_input("Posición del jugador:")
if st.sidebar.button("Buscar por posición"):
    resultado = filtrar_por_posicion(FC26_data, titulo)
    st.subheader("Resultado de la búsqueda")
    st.write(f"Total de jugadores: {resultado.shape[0]}")
    st.dataframe(resultado)

def filtrar_por_equipo(df, texto):
    return df[df["club_name"].str.contains(texto, case=False, na=False, regex=False)]

club = st.sidebar.text_input("Club del jugador:")
if st.sidebar.button("Buscar por club"):
    resultado = filtrar_por_equipo(FC26_data, club)
    st.subheader("Resultado de la búsqueda")
    st.write(f"Total de jugadores: {resultado.shape[0]}")
    st.dataframe(resultado)

def filtrar_por_edad(df, texto):
    return df[df["age"].astype(str) == texto]

edad = st.sidebar.text_input("Edad del jugador:")
if st.sidebar.button("Buscar por edad"):
    resultado = filtrar_por_edad(FC26_data, edad)
    st.subheader("Resultado de la búsqueda")
    st.write(f"Total de jugadores: {resultado.shape[0]}")
    st.dataframe(resultado)

def filtrar_por_pie(df, pie):
    return df[df["preferred_foot"] == pie]

pie = st.sidebar.radio("Pie preferido:", ["Right", "Left"])
if st.sidebar.button("Buscar por pie"):
    resultado = filtrar_por_pie(FC26_data, pie)
    st.subheader("Resultado de la búsqueda")
    st.write(f"Total de jugadores: {resultado.shape[0]}")
    st.dataframe(resultado)

fig, ax = plt.subplots()
ax.hist(FC26_data["overall"], bins=20)
ax.set_xlabel("Calificación global")
ax.set_ylabel("Cantidad de jugadores")
st.header("¿Qué tan buenos son la mayoría de los jugadores?")
st.pyplot(fig)

clubes = FC26_data.groupby("club_name")["overall"].agg(["mean", "count"])
clubes = clubes[clubes["count"] >= 10]
top_clubes = clubes["mean"].sort_values(ascending=False).head(10)

fig2, ax2 = plt.subplots()
ax2.barh(top_clubes.index, top_clubes.values)
ax2.invert_yaxis()
ax2.set_xlim(top_clubes.min() - 5, top_clubes.max() + 1)
ax2.set_xlabel("Calificación global promedio")
ax2.set_ylabel("Club")
st.header("Top 10 clubes con mejor calificación promedio")
st.pyplot(fig2)

fig3, ax3 = plt.subplots()
ax3.scatter(FC26_data["overall"], FC26_data["value_eur"] / 1_000_000, alpha=0.3)
ax3.set_xlabel("Calificación global")
ax3.set_ylabel("Valor (millones de euros)")
st.header("Calificación global vs. valor de mercado")
st.pyplot(fig3)