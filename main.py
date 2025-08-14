import dotenv
import os

import streamlit as st

import diseno
import mapa
import filtros
import dominios_data
import elementos_visuales
import conexion

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

if __name__ == "__main__":
    main()


