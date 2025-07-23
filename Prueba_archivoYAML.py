from librerias import *  # Importa todas las librerías externas desde librerias.py
from dominios_data import dominios, data_catalog #olaerfrfr

def main():
    st.set_page_config(layout="wide")
    st.title("Tablero de Dominios y Subdominios")

    col1, col2 = st.columns(2)
    with col1:
        selected_domain = st.selectbox("Selecciona un dominio", list(dominios.keys()))
    with col2:
        if selected_domain:
            selected_subdomain = st.selectbox("Selecciona un subdominio", dominios[selected_domain])
        else:
            selected_subdomain = None

    # Mostrar la tabla de datos del subdominio seleccionado
    if selected_subdomain and selected_subdomain in data_catalog:
        st.subheader(f"Datos de {selected_subdomain}")
        gb = GridOptionsBuilder.from_dataframe(data_catalog[selected_subdomain])
        gb.configure_default_column(wrapText=True, autoHeight=True)
        gb.configure_column("Descripción", wrapText=True, autoHeight=True)
        grid_options = gb.build()
        AgGrid(
            data_catalog[selected_subdomain],
            gridOptions=grid_options,
            height=500,
            fit_columns_on_grid_load=True,
        )
        pd.set_option('display.max_colwidth', 100)
        pd.set_option('display.width', 200)
    else:
        st.info("No hay datos disponibles para este subdominio.")

if __name__ == "__main__":
    main()
