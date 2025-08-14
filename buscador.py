import unicodedata

import polars as pl
import pandas as pd

pd.options.mode.copy_on_write = True

def normalizar_query(text: str) -> str:
    text = text.lower()
    text = unicodedata.normalize("NFKD", text)
    return ''.join(c for c in text if not unicodedata.combining(c))

def busqueda_dataframe(df, query):
    query_buena = normalizar_query(query)
    df_search = (
       pl.from_pandas(df)
       .filter(
           pl.any_horizontal(pl.col(pl.String).str.to_lowercase()
                                              .str.normalize("NFKD")                 
                                              .str.replace_all(r"\p{M}", "")
                                              .str.contains(query_buena))
       )
    )   
    return df_search.to_pandas(use_pyarrow_extension_array=True)