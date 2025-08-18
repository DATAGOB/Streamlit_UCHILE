
import pandas as pd
from pymongoarrow.monkey import patch_all
import streamlit as st

patch_all()

def traer_dominios(cliente, db, collection):
    
    db = cliente[db]
    collection = db[collection]
    dict = collection.find_one()
    dict.pop(next(iter(dict)))
    return dict

def obtener_df_mongodb(client, db, collection, dominio, subdominio):
    try:
       db = client[db]
       coll = db[collection]
       df = coll.find_polars_all({'Dominio': dominio, 'Subdominio': subdominio}).drop('_id', 'Dominio', 'Subdominio').to_pandas(use_pyarrow_extension_array=True)
       return df
    except:
       return pd.DataFrame()
    
@st.cache_data(ttl=500)
def obtener_df_mongodb_cached(_client, db, collection_data, selected_domain, selected_subdomain):
    """
    Función para obtener datos de MongoDB
    """
    return obtener_df_mongodb(
        _client,
        db,
        collection_data,
        selected_domain,
        selected_subdomain
    )
