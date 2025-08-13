import streamlit as st
import base64

def mostrar_logos():
    # Logos en la esquina superior izquierda
    st.markdown(
        """
        <div style="position: sticky; top: 0px; left: 0px; z-index: 100; display: flex; flex-direction: row; align-items: center; gap: 10px; background: #18191A; padding: 8px 0 0 10px;">
            <img src="data:image/png;base64,{datagob}" alt="datagob" style="height:60px; display:block;">
            <img src="data:image/png;base64,{vti}" alt="vti" style="height:40px; display:block;">
        </div>
        """.format(
            datagob=base64.b64encode(open("logo_datagob_claro.png", "rb").read()).decode(),
            vti=base64.b64encode(open("vti_claro.png", "rb").read()).decode()
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
        <div style='text-align: center; color: #F5F6F7; font-size: 1.1rem; margin-bottom: 20px;'>
        El objetivo del catálogo de datos es centralizar, organizar y visibilizar los activos de datos de la organización, 
        facilitando su acceso, comprensión y uso por parte de las distintas unidades, promoviendo la transparencia, la toma de decisiones informada y
        el cumplimiento de principios de gobernanza de datos.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Descripción de dominios y subdominios
    st.markdown(
        """
        <div style='text-align: center; color: #F5F6F7; font-size: 1.1rem; margin-bottom: 20px;'>
        En el contexto de gobierno de datos, un **dominio de datos** se define como un conjunto de datos que comparten características comunes, 
        se rigen por las mismas reglas de negocio y pueden ser gestionados de manera similar. La definición de dominios en una organización permite organizar y estructurar los datos, 
        de manera de facilitar su gobernanza. A su vez, un **subdominio** es un subconjunto de un dominio de datos. Se utiliza para dividir dominios en partes más pequeñas y específicas, facilitando así su gestión, análisis y gobernanza. 
        Permite abordar cada subdominio con enfoques particulares según sus características, sin perder la conexión con el dominio principal al que pertenece.
        </div>
        """,
        unsafe_allow_html=True
    )
