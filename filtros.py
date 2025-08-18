import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import buscador
import dominios_data

pd.options.mode.copy_on_write = True

# Función de callback para el botón "Limpiar"
def resetear_filtros(selected_domain, selected_subdomain):
    st.session_state.query_busqueda = ""
    st.session_state.valor_filtro = "Todos"
    st.session_state.df_base = dominios_data.obtener_df_mongodb_cached(
        st.session_state.client, 
        st.session_state.db, 
        st.session_state.collection_data, 
        selected_domain, 
        selected_subdomain
    )

def mostrar_filtros(selected_domain, selected_subdomain, client, db, collection_data):
    # Inicio de estado
    if "df_base" not in st.session_state or \
       st.session_state.get("selected_domain") != selected_domain or \
       st.session_state.get("selected_subdomain") != selected_subdomain:
        
        st.session_state.selected_domain = selected_domain
        st.session_state.selected_subdomain = selected_subdomain
        st.session_state.query_busqueda = ""
        st.session_state.valor_filtro = "Todos"
        st.session_state.df_base = dominios_data.obtener_df_mongodb_cached(client, db, collection_data, selected_domain, selected_subdomain)

    st.session_state.client = client
    st.session_state.db = db
    st.session_state.collection_data = collection_data
    
    # Dataframe que trae cuando se selecciona el dominio y subdominio
    df_to_display = st.session_state.df_base
    
    if df_to_display.empty:
        st.info("Selecciona un dominio y un subdominio para ver los datos.")
        return
    
    st.subheader(f"Datos de {selected_subdomain}")

    # Campo de busqueda
    query_busqueda = st.text_input("Ingresa tu búsqueda aquí:", value=st.session_state.query_busqueda, key="input_busqueda")

    button_col1, button_col3 = st.columns(2) 
    with button_col1:
        boton_busqueda = st.button("Aplicar Búsqueda")
    with button_col3:
        st.button("Limpiar Todos los Filtros", on_click=resetear_filtros, args=(selected_domain, selected_subdomain))

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

    # Filtrado
    if "Objeto de Datos" in df_to_display.columns:
        objetos_opciones = ["Todos"] + df_to_display["Objeto de Datos"].unique().tolist()
        
        # Valor seleccionado aún exista en las opciones
        selected_index = 0
        if st.session_state.valor_filtro in objetos_opciones:
            selected_index = objetos_opciones.index(st.session_state.valor_filtro)

        filtro_seleccionado = st.selectbox(
            'Filtra por valor en "Objeto de Datos"',
            options=objetos_opciones,
            index=selected_index,
            key=f"objeto_filter_selectbox_{selected_domain}_{selected_subdomain}_{st.session_state.query_busqueda}"
        )
        st.session_state.valor_filtro = filtro_seleccionado

        # Se aplica el filtro al DataFrame después de la búsqueda
        if st.session_state.valor_filtro != "Todos":
            df_to_display = df_to_display[df_to_display["Objeto de Datos"] == st.session_state.valor_filtro]
            if df_to_display.empty:
                st.warning("No hay datos para el filtro de 'Objeto de Datos' seleccionado.")
    else:
        st.info("La columna 'Objeto de Datos' no está disponible para aplicar filtros en este subdominio o no hay datos después de la búsqueda.")

 
    # AgGrid
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
    elif st.session_state.query_busqueda or st.session_state.valor_filtro != "Todos":
        pass
    else:
        st.info("No hay datos disponibles para este subdominio.")