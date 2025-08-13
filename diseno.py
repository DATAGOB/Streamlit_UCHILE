import streamlit as st

def configurar_pagina():
    st.set_page_config(layout="wide")

def aplicar_css():
    st.markdown(
        """
        <style>
        body, .stApp {
            background-color: #18191A !important;
            color: #F5F6F7 !important;
        }
        .block-container {
            padding-top: 20px !important;
        }
        header, [data-testid="stHeader"], [data-testid="stToolbar"] {
            display: none !important;
        }
        label, .stSelectbox label {
            color: #F5F6F7 !important;
            font-size: 1.3rem !important;
            font-weight: 600 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
