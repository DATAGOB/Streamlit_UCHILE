import streamlit as st
from streamlit_image_zoom import image_zoom
from PIL import Image

def mostrar_mapa():
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
            img = Image.open("imagenes/MAPA_DOMINIOS.png")
            image_zoom(img, size=(800, 600), keep_aspect_ratio=False, zoom_factor=2.0, increment=0.1)
