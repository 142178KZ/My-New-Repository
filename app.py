import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
dis_button = st.button('Construir grafico de dispersión') # crear otro botón
    
#st.header('Vehicles')

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if dis_button: # al hacer clic en el botón # Para hacer otro boton 
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión')





        
# crear un histograma
#fig_dis = px.histogram(car_data, x="model") #grafico de dispersión
    
# mostrar un gráfico Plotly interactivo
st.plotly_chart(fig_dis, use_container_width=True)

