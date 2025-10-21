import streamlit as st
import base64
import os

def mostrar_logos():
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_datagob = os.path.join(dir_actual, "imagenes", "logoweb.webp")
    ruta_vti = os.path.join(dir_actual, "imagenes", "logo_vti_negro.png")

    datagob_b64 = base64.b64encode(open(ruta_datagob, "rb").read()).decode()
    vti_b64 = base64.b64encode(open(ruta_vti, "rb").read()).decode()

    st.markdown(
        """
        <style>
        .top-bar {{
            position: sticky;
            top: 0;
            z-index: 999;
            background: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 6px 25px 4px 25px; /* un poco menos de alto */
            margin-bottom: 30px;        /* separa del título */
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            width: 100%;
            border-radius: 8px;
        }}

        .block-container {{
            padding-top: 15px !important;
        }}

        [data-testid="stAppViewBlockContainer"] > div:first-child {{
            margin-left: auto;
            margin-right: auto;
            max-width: 95%;
        }}
        </style>

        <div class="top-bar">
            <img src="data:image/png;base64,{datagob}" alt="datagob" style="height:58px;">
            <img src="data:image/png;base64,{vti}" alt="vti" style="height:42px;">
        </div>
        """.format(
            datagob=datagob_b64,
            vti=vti_b64
        ),
        unsafe_allow_html=True
    )


def mostrar_titulo():
    # Título 
    st.markdown("""
        <div style="position: relative; text-align: center; margin-bottom: 50px;">
        <hr style="border: none; height: 2px; background-color: #5f9ea0; position: absolute; top: 50%; width: 100%; z-index: 1;">
        <h1 style="position: relative; display: inline-block; padding: 0 20px; z-index: 2;">Catálogo de datos UCHILE</h1>
        </div>
        """, unsafe_allow_html=True)

def mostrar_textos_intro():
    # Objetivo del catalogo de datos
    st.markdown(
        """
        <div style='text-align: center; color: #000000; font-size: 1.1rem; margin-bottom: 20px;'>
        El Catálogo de Datos UCHILE tiene como objetivo centralizar, organizar y visibilizar los activos de datos de la Universidad de Chile, facilitando su acceso, comprensión y uso por parte de las distintas unidades universitarias. De esta forma, 
        se promueve la transparencia, la toma de decisiones informada y el cumplimiento de los principios de gobernanza de datos institucionales.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Descripción de dominios y subdominios
    st.markdown(
        """
        <div style='text-align: center; color: #000000; font-size: 1.1rem; margin-bottom: 20px;'>
        En el contexto del gobierno de datos, un dominio de datos se entiende como un conjunto de datos que comparten características comunes, se rigen por reglas de negocio similares y
        pueden ser gestionados de manera coordinada. La definición de dominios 
        permite estructurar y organizar los datos institucionales, favoreciendo su administración, interoperabilidad y análisis.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Descripción de dominios y subdominios
    st.markdown(
        """
        <div style='text-align: center; color: #000000; font-size: 1.1rem; margin-bottom: 20px;'>
        A su vez, un subdominio de datos corresponde a un subconjunto más específico dentro de un dominio, que permite abordar con mayor detalle los procesos y temáticas particulares que lo componen. 
        Esta estructura facilita la gestión de los datos de manera más granular, manteniendo la conexión con el dominio principal.
        </div>
        """,
        unsafe_allow_html=True
    )

      # Descripción de dominios y subdominios
    st.markdown(
        """
        <div style='text-align: center; color: #000000; font-size: 1.1rem; margin-bottom: 20px;'>
        Para tener una visión general de la organización de los datos en la Universidad, puedes acceder al Mapa de Dominios de Datos, donde se visualiza la estructura de los distintos dominios y subdominios definidos. 
        Este mapa constituye una herramienta de apoyo para comprender cómo se agrupan y relacionan los datos institucionales.
        </div>
        """,
        unsafe_allow_html=True
    )

      # Descripción de dominios y subdominios
    st.markdown(
        """
        <div style='text-align: center; color: #000000; font-size: 1.1rem; margin-bottom: 20px;'>
        A través de este catálogo, las unidades y organismos de la Universidad pueden identificar, explorar y comprender los datos disponibles, fortaleciendo 
        una cultura de gestión basada en evidencia y alineada con las políticas institucionales de gobernanza y protección de datos.
        </div>
        """,
        unsafe_allow_html=True
    )



def mostrar_titulo_modelo():
    # Título 
    st.markdown("""
        <div style="position: relative; text-align: center; margin-bottom: 50px;">
        <hr style="border: none; height: 2px; background-color: #5f9ea0; position: absolute; top: 50%; width: 100%; z-index: 1;">
        <h1 style="position: relative; display: inline-block; padding: 0 20px; z-index: 2;">Modelos de datos UCHILE</h1>
        </div>
        """, unsafe_allow_html=True)
    
def mostrar_textos_modelo():
    # Objetivo del catalogo de datos
    st.markdown(
        """
        <div style='text-align: center; color: #000000; font-size: 1.1rem; margin-bottom: 20px;'>
        En esta sección podrás explorar los distintos modelos de datos que utilizamos sobre nuestros datos transaccionales.
        </div>
        """,
        unsafe_allow_html=True
    )

def mostrar_titulo():
    # Título 
    st.markdown("""
        <div style="position: relative; text-align: center; margin-bottom: 50px;">
        <hr style="border: none; height: 2px; background-color: #5f9ea0; position: absolute; top: 50%; width: 100%; z-index: 1;">
        <h1 style="position: relative; display: inline-block; padding: 0 20px; z-index: 2;">Catálogo de datos UCHILE</h1>
        </div>
        """, unsafe_allow_html=True)

def mostrar_titulo_modelo():
    # Título 
    st.markdown("""
        <div style="position: relative; text-align: center; margin-bottom: 50px;">
        <hr style="border: none; height: 2px; background-color: #5f9ea0; position: absolute; top: 50%; width: 100%; z-index: 1;">
        <h1 style="position: relative; display: inline-block; padding: 0 20px; z-index: 2;">Modelos de datos UCHILE</h1>
        </div>
        """, unsafe_allow_html=True)
    
def mostrar_textos_modelo():
    # Objetivo del catalogo de datos
    st.markdown(
        """
        <div style='text-align: center; color: #000000; font-size: 1.1rem; margin-bottom: 20px;'>
        En esta sección podrás explorar los distintos modelos de datos que utilizamos sobre nuestros datos transaccionales.
        </div>
        """,
        unsafe_allow_html=True
    )