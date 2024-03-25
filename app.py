import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
title_app = st.header('App de vehiculos') # crear titulo general
    
if hist_button: # al hacer clic en el botón
    # escribir encabezado
    st.header('Venta de coches') 

    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

    # crear segundo botton

dis_button = st.button('Construir gráfico dispersión') # crear un botón

if dis_button: # al hacer clic en el botón
    # escribir encabezado
    st.header('Modelos de autos') 
    
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para los modelos por año de coches')

    # crear un gráfico de dispersión
    fig_dis = px.scatter(car_data, x="model_year", y="price") 

    # mostrar un gráfico de dispersión Plotly interactivo
    st.plotly_chart(fig_dis, use_container_width=True)
