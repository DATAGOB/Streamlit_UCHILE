from pymongo import MongoClient
import streamlit as st

@st.cache_resource(ttl=1200)
def cliente_mongodb(user, password, host_puerto):
    """
    Función que crea y retorna el cliente de MongoDB.
    """
    uri = f'mongodb://{user}:{password}@{host_puerto}/?authSource=datagob&authMechanism=SCRAM-SHA-256&replicaSet=rs0&readPreference=primary&ssl=false'
    client = MongoClient(uri)
    return client
            