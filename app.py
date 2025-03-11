
import streamlit as st
import pandas as pd
from datetime import datetime

# Cargar la base de datos de usuarios (DNI registrados)
def cargar_dnis(ruta_excel):
    return pd.read_excel(ruta_excel)

# Guardar el registro del pedido
def registrar_pedido(dni, archivo_salida):
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nuevo_registro = pd.DataFrame([[dni, hora_actual]], columns=["DNI", "Hora"])
    
    try:
        pedidos = pd.read_excel(archivo_salida)
        pedidos = pd.concat([pedidos, nuevo_registro], ignore_index=True)
    except FileNotFoundError:
        pedidos = nuevo_registro
    
    pedidos.to_excel(archivo_salida, index=False)

# App en Streamlit
st.title("Registro de Pedido de Almuerzo 🍽️")

dni_ingresado = st.text_input("Ingresa tu número de DNI:")

if st.button("Registrar Pedido"):
    if dni_ingresado:
        # Ruta al archivo Excel con los DNIs válidos
        archivo_dnis = "usuarios.xlsx"
        # Ruta donde se guardarán los pedidos
        archivo_pedidos = "pedidos.xlsx"
        
        dnis = cargar_dnis(archivo_dnis)
        
        if int(dni_ingresado) in dnis['DNI'].values:
            registrar_pedido(dni_ingresado, archivo_pedidos)
            st.success("✅ Pedido ingresado exitosamente.")
        else:
            st.error("❌ DNI no encontrado. Verifica tu número.")
    else:
        st.warning("Por favor, ingresa tu DNI.")
