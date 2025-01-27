import streamlit as st
import pandas as pd

# Cargar los datos
titanic = pd.read_csv("titanic.csv")

# Título de la aplicación
st.title("Titanic: Supervivencia y Datos")

# 1. Mostrar un resumen estadístico de las edades de los pasajeros
st.header("Resumen Estadístico de las Edades")
st.write(titanic["Age"].describe())

# 2. Filtrar pasajeros por sexo y clase
st.header("Filtrar Pasajeros por Sexo y Clase")
sex = st.selectbox("Selecciona el sexo:", ["male", "female"])
pclass = st.selectbox("Selecciona la clase:", [1, 2, 3])

filtered_data = titanic[(titanic["Sex"] == sex) & (titanic["Pclass"] == pclass)]
st.write(f"Pasajeros filtrados: {len(filtered_data)}")
st.dataframe(filtered_data[["Name", "Age", "Sex", "Pclass", "Survived"]])

# 3. Mostrar la tasa de supervivencia por clase
st.header("Tasa de Supervivencia por Clase")
survival_rate = titanic.groupby("Pclass")["Survived"].mean()
st.bar_chart(survival_rate)
