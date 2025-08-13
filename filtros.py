import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import buscador

def mostrar_filtros(data_catalog, selected_subdomain):
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
