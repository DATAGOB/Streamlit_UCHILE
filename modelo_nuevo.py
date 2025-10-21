from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import threading
import streamlit as st
import streamlit.components.v1 as components
import uvicorn

# Montar FastAPI en un hilo aparte
app = FastAPI()
app.mount("/static", StaticFiles(directory="static/reports"), name="static")

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8502)

thread = threading.Thread(target=run_server, daemon=True)
thread.start()

def mostrar_modelo():
    st.header("📊 Modelos de datos institucionales UCHILE")
    st.markdown("""
    En este apartado podrás explorar los distintos **modelos de datos institucionales** que utilizamos para describir, organizar y documentar la estructura de nuestros sistemas transaccionales.  
    Cada modelo permite comprender cómo se relacionan las distintas entidades y tablas que conforman la base de datos universitaria, facilitando la interoperabilidad, la gobernanza y la trazabilidad de la información.  

    **Definición de componentes:**  
    - **Objetos:** representan las distintas entidades de datos (por ejemplo, personas, unidades académicas, programas, asignaturas), junto con sus atributos y relaciones.  
    - **Diagramas:** muestran visualmente las interrelaciones entre las entidades, ofreciendo una visión estructurada del modelo de datos que respalda los sistemas institucionales.  

    **Objetivo del apartado:**  
    Entregar una vista consolidada y actualizada de los modelos de datos de la Universidad de Chile, promoviendo la transparencia, la comprensión técnica y la correcta gestión de la información institucional.
    """)
    
    st.markdown("---")
    components.iframe("http://127.0.0.1:8502/static/AllTablesDetails_1_index.html", height=800)
