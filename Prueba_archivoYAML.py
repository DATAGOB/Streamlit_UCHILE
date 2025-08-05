from librerias import *  # Importa todas las librerías externas desde librerias.py
from dominios_data import dominios, data_catalog
import base64
import streamlit as st
from streamlit_image_zoom import image_zoom
from PIL import Image


def main():
    st.set_page_config(layout="wide")

    # Forzar modo oscuro visual usando CSS
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

    # Título 
    st.markdown("""
        <div style="position: relative; text-align: center; margin-bottom: 50px;">
        <hr style="border: none; height: 2px; background-color: #5f9ea0; position: absolute; top: 50%; width: 100%; z-index: 1;">
        <h1 style="position: relative; display: inline-block; padding: 0 20px; z-index: 2;">Catalogo de datos UCHILE</h1>
        </div>
        """, unsafe_allow_html=True)

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
        En el contexto de gobierno de datos, un dominio de datos se define como un conjunto de datos que comparten características comunes, 
        se rigen por las mismas reglas de negocio y pueden ser gestionados de manera similar. La definición de dominios en una organización permite organizar y estructurar los datos, 
        de manera de facilitar su gobernanza. A su vez, un subdominio es un subconjunto de un dominio de datos. Se utiliza para dividir dominios en partes más pequeñas y específicas, facilitando así su gestión, análisis y gobernanza. 
        Permite abordar cada subdominio con enfoques particulares según sus características, sin perder la conexión con el dominio principal al que pertenece.
        </div>
        """,
        unsafe_allow_html=True
    )


    # Estado del mapa
    if 'show_mapa' not in st.session_state:
        st.session_state['show_mapa'] = False

    # Botón de mostrar/ocultar mapa con rerun
    if st.button("Ocultar mapa" if st.session_state['show_mapa'] else "Ver mapa dominio de datos"):
        st.session_state['show_mapa'] = not st.session_state['show_mapa']
        st.rerun()
    
    # Mostrar mapa de dominios

    if st.session_state.get('show_mapa', False):
        st.write("🔍 Usa scroll para hacer zoom y click-drag para mover:")

        col1, col2, col3 = st.columns([1, 3, 1])  # Columna central 3 veces más ancha

        with col2:
            img = Image.open("MAPA_DOMINIOS.png")
            image_zoom(img, size=(800, 600), keep_aspect_ratio=False, zoom_factor=2.0, increment=0.1)

    
    # Selección de dominio y subdominio
    col1, col2 = st.columns(2)
    with col1:
        selected_domain = st.selectbox("Selecciona un dominio", list(dominios.keys()))
    with col2:
        if selected_domain:
            selected_subdomain = st.selectbox("Selecciona un subdominio", dominios[selected_domain])
        else:
            selected_subdomain = None

    # Mostrar la tabla del subdominio seleccionado
    if selected_subdomain and selected_subdomain in data_catalog:
        st.subheader(f"Datos de {selected_subdomain}")
        df = data_catalog[selected_subdomain]

        # Mostrar tabla AgGrid
        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_default_column(wrapText=True, autoHeight=True, filter=True, sortable=True, resizable=True)
        gb.configure_column("Descripción", wrapText=True, autoHeight=True)
        grid_options = gb.build()

        AgGrid(
            df,
            gridOptions=grid_options,
            height=500,
            fit_columns_on_grid_load=True,
            enable_enterprise_modules=True,
            allow_unsafe_jscode=True
        )
    else:
        st.info("No hay datos disponibles para este subdominio.")

if __name__ == "__main__":
    main()

