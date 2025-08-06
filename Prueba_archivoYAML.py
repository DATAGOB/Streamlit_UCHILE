from librerias import * # Importa todas las librerías externas desde librerias.py
from dominios_data import dominios, data_catalog
import buscador
import streamlit as st
from streamlit_image_zoom import image_zoom
from PIL import Image


def main():
    st.set_page_config(layout="wide")

    # Forzar modo oscuro visual usando CSS (tu CSS se mantiene)
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
        En el contexto de gobierno de datos, un **dominio de datos** se define como un conjunto de datos que comparten características comunes, 
        se rigen por las mismas reglas de negocio y pueden ser gestionados de manera similar. La definición de dominios en una organización permite organizar y estructurar los datos, 
        de manera de facilitar su gobernanza. A su vez, un **subdominio** es un subconjunto de un dominio de datos. Se utiliza para dividir dominios en partes más pequeñas y específicas, facilitando así su gestión, análisis y gobernanza. 
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

    if selected_subdomain and selected_subdomain in data_catalog:
        st.subheader(f"Datos de {selected_subdomain}")

        if "df_base" not in st.session_state or st.session_state.get("selected_subdomain") != selected_subdomain:
            st.session_state.df_base = data_catalog[selected_subdomain] 
            st.session_state.selected_subdomain = selected_subdomain
            st.session_state.query_busqueda = "" 
            st.session_state.valor_filtro = "Todos" 

        query_busqueda = st.text_input("Ingresa tu búsqueda aquí:", value=st.session_state.query_busqueda, key="input_busqueda")

        button_col1, button_col3 = st.columns(2) 
        with button_col1:
            boton_busqueda = st.button("Aplicar Búsqueda")
        with button_col3:
            resetear_filtros = st.button("Limpiar Todos los Filtros") 

        if resetear_filtros:
            st.session_state.query_busqueda = ""
            st.session_state.valor_filtro = "Todos"
            st.session_state.df_base = data_catalog[selected_subdomain]
            st.rerun() 

        df_to_display = st.session_state.df_base

        if boton_busqueda:
            st.session_state.query_busqueda = query_busqueda 
            if st.session_state.query_busqueda: 
                df_to_display = buscador.busqueda_dataframe(df_to_display, st.session_state.query_busqueda)
                if df_to_display.empty:
                    st.warning("No se encontraron resultados para tu búsqueda.")
            else:
                st.info("Ingresa un término de búsqueda para aplicar la búsqueda.")
        
        elif st.session_state.query_busqueda:
             df_to_display = buscador.busqueda_dataframe(df_to_display, st.session_state.query_busqueda)

        if "valor_filtro" not in st.session_state:
            st.session_state.valor_filtro = "Todos" 
        
        if "Unnamed: 0" in df_to_display.columns:
            unnamed_options = ["Todos"] + df_to_display["Unnamed: 0"].unique().tolist()
            
            if st.session_state.valor_filtro not in unnamed_options:
                st.session_state.valor_filtro = "Todos" 

            filtro_seleccionado = st.selectbox(
                'Filtra por valor en "Unnamed: 0"', 
                options=unnamed_options, 
                index=unnamed_options.index(st.session_state.valor_filtro),
                key="unnamed_filter_selectbox" 
            )
            
            if filtro_seleccionado != st.session_state.valor_filtro:
                st.session_state.valor_filtro = filtro_seleccionado
            
            if st.session_state.valor_filtro != "Todos":
                df_to_display = df_to_display[df_to_display["Unnamed: 0"] == st.session_state.valor_filtro]
                if df_to_display.empty:
                    st.warning("No hay datos para el filtro de 'Unnamed: 0' seleccionado.")
        else:
            st.info("La columna 'Unnamed: 0' no está disponible para aplicar filtros en este subdominio o no hay datos después de la búsqueda.")

        if not df_to_display.empty:
            gb = GridOptionsBuilder.from_dataframe(df_to_display)
            gb.configure_default_column(wrapText=True, autoHeight=True)
            if "Descripción" in df_to_display.columns: 
                gb.configure_column("Descripción", wrapText=True, autoHeight=True)
            grid_options = gb.build()
            AgGrid(
                df_to_display,
                gridOptions=grid_options,
                height=500,
                fit_columns_on_grid_load=True,
                key=f"aggrid_{selected_subdomain}_{st.session_state.query_busqueda}_{st.session_state.valor_filtro}" 
            )
            pd.set_option('display.max_colwidth', 100)
            pd.set_option('display.width', 200)
        elif st.session_state.query_busqueda or st.session_state.valor_filtro != "Todos": # Solo advertir si hay filtros aplicados
            pass # Mensaje ya manejado por los st.warning anteriores, evitamos duplicidad
        else: # Si no hay filtros y el DF base está vacío
            st.info("No hay datos disponibles para este subdominio.")
            
    else:
        st.info("Selecciona un dominio y un subdominio para ver los datos.")

if __name__ == "__main__":
    main()

