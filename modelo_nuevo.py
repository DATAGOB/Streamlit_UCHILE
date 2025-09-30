# -*- coding: utf-8 -*-
import streamlit as st

def mostrar_modelo():
    st.title("📊 Modelos de Datos")
    st.write("Aquí puedes documentar, visualizar o cargar tus modelos de datos.")
    
    uploaded_file = st.file_uploader("Sube tu modelo de datos (ej. .csv, .json, .png)", type=["csv", "json", "png"])
    if uploaded_file:
        st.success(f"Archivo cargado: {uploaded_file.name}")