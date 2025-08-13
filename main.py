import streamlit as st
from diseno import configurar_pagina, aplicar_css
from mapa import mostrar_mapa
from filtros import mostrar_filtros
from dominios_data import dominios, data_catalog
from elementos_visuales import mostrar_logos, mostrar_titulo, mostrar_textos_intro

def main():
    configurar_pagina()
    aplicar_css()
    mostrar_logos()
    mostrar_titulo()
    mostrar_textos_intro()
    mostrar_mapa()

    col1, col2 = st.columns(2)
    with col1:
        selected_domain = st.selectbox("Selecciona un dominio", list(dominios.keys()))
    with col2:
        selected_subdomain = st.selectbox("Selecciona un subdominio", dominios[selected_domain]) if selected_domain else None

    mostrar_filtros(data_catalog, selected_subdomain)

if __name__ == "__main__":
    main()


