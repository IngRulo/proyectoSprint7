import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')

# boton_histograma = st.button('Construir histograma')
# boton_dispersion = st.button('Construir gráfico de dispersión')

# crear una casilla de verificación
build_histograma = st.checkbox('Construir un histograma')
build_dispersion = st.checkbox('Construir un gráfico de dispersión')

# Validamos si se ha presionado el botón de histograma
if build_histograma:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
# Validamos si se ha presionado el botón de gráfico de dispersión
if build_dispersion:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
