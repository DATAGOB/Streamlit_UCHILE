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
    st.header("📊 Modelo de datos")
    components.iframe("http://127.0.0.1:8502/static/AllTablesDetails_1_index.html", height=800)
