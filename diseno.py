import streamlit as st

def configurar_pagina():
    st.set_page_config(layout="wide")

def aplicar_css():
    st.markdown(
        """
        <style>
        body, .stApp {
            background-color: #ffffff !important;  /* Fondo blanco */
            color: #000000 !important;              /* Texto negro */
        }
        .block-container {
            padding-top: 20px !important;
        }
        header, [data-testid="stHeader"], [data-testid="stToolbar"] {
            display: none !important;
        }
        label, .stSelectbox label {
            color: #000000 !important;              /* Etiquetas negras */
            font-size: 1.3rem !important;
            font-weight: 600 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
