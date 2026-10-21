import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt 
import numpy as np

@st.cache_data
def load_data(nrows=6820):
    return pd.read_csv("https://raw.githubusercontent.com/softbytavz/FC26dataset/refs/heads/main/FC26_Data.csv",nrows=nrows,encoding="latin-1")

FC26_data = load_data()

st.header("FC 26 data")

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

def filtrar_por_liga(df, liga):
    return df[df["league_name"] == liga]

ligas = sorted(FC26_data["league_name"].dropna().unique())
liga = st.sidebar.selectbox("Liga:", ligas)
if st.sidebar.button("Buscar por liga"):
    resultado = filtrar_por_liga(FC26_data, liga)
    st.subheader("Resultado de la búsqueda")
    st.write(f"Total de jugadores: {resultado.shape[0]}")
    st.dataframe(resultado) 

def filtrar_por_calificacion(df, minimo, maximo):
    return df[(df["overall"] >= minimo) & (df["overall"] <= maximo)]

cal_min, cal_max = st.sidebar.slider("Calificación global:", 40, 99, (40, 99))
if st.sidebar.button("Buscar por calificación"):
    resultado = filtrar_por_calificacion(FC26_data, cal_min, cal_max)
    st.subheader("Resultado de la búsqueda")
    st.write(f"Total de jugadores: {resultado.shape[0]}")
    st.dataframe(resultado)   

fig, ax = plt.subplots()
ax.hist(FC26_data["overall"], bins=20)
ax.set_xlabel("Calificación global")
ax.set_ylabel("Cantidad de jugadores")
st.header("Cantidad de jugadores y su  calificación global")
st.pyplot(fig)

fig2, ax2 = plt.subplots()
y_pos = FC26_data['short_name'].head(10)
x_pos = FC26_data['overall'].head(10)
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Jugador")
ax2.set_xlabel("Calificación global")
ax2.set_title("Calificación global de 10 jugadores")
st.header("Top 10 jugadores")
st.pyplot(fig2)

fig3, ax3 = plt.subplots()
ax3.scatter(FC26_data.age, FC26_data.potential)
ax3.set_xlabel("Edad")
ax3.set_ylabel("Potencial")
st.header("Edad y Potencial")
st.pyplot(fig3)


st.title("Antonio Yaset Calderón Aquino")
st.header("Matrícula: S26004634")
st.header("Mapa aquí abajo 👇")

map_data = pd.DataFrame(
  np.random.randn(1, 2) / [500, 500] + [18.8033, -97.1808],
  columns=['lat', 'lon'])

st.title("Ciudad Mendoza, Ver.")
st.header("Mendozayork 🗽")
st.header("CP: 94740")

st.map(map_data)