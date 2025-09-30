import dotenv
import os

import streamlit as st

import diseno
import mapa
import filtros
import dominios_data
import elementos_visuales
import conexion
import modelo_nuevo
from streamlit_option_menu import option_menu

dotenv.load_dotenv('.env')
user = os.getenv('user_mongodb')
password = os.getenv('password_mongodb')
host_puerto = os.getenv('host_puerto_mongodb')

db = os.getenv('db')
collection_dominios = os.getenv('collection_dominios')
collection_data = os.getenv('collection_data')

def main():
    diseno.configurar_pagina()
    diseno.aplicar_css()
    elementos_visuales.mostrar_logos()
    

    with st.sidebar:
        selected = option_menu(
            menu_title="Menú",  # título del menú
            options=["Catálogo de datos", "Modelos de datos"],  # opciones
            icons=["collection", "diagram-3"],  # íconos bootstrap
            menu_icon="cast",  
            default_index=0,  # página inicial
        )

      # 👇 dependiendo de la selección, llama al módulo correcto
    if selected == "Catálogo de datos":
        elementos_visuales.mostrar_titulo()
        elementos_visuales.mostrar_textos_intro()
        mapa.mostrar_mapa()

        client = conexion.cliente_mongodb(user, password, host_puerto)

        dominios = dominios_data.traer_dominios(client, db, collection_dominios)

        col1, col2 = st.columns(2)
        with col1:
            selected_domain = st.selectbox("Selecciona un dominio", list(dominios.keys()))
        with col2:
            selected_subdomain = st.selectbox("Selecciona un subdominio", dominios[selected_domain]) if selected_domain else None
        
        filtros.mostrar_filtros(selected_domain, selected_subdomain, client, db, collection_data)

    elif selected == "Modelos de datos":
        elementos_visuales.mostrar_titulo_modelo()
        elementos_visuales.mostrar_textos_modelo()
        modelo_nuevo.mostrar_modelo()

if __name__ == "__main__":
    main()


