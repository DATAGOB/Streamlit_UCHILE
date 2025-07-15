import json
import pandas as pd

try:
    with open("data_catalog.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    print("Error al cargar data_catalog.json:", e)
    print("Verifica que el archivo sea un JSON válido y no tenga comentarios ni líneas vacías.")
    exit(1)

# Procesar solo "Datos Personales"
if "Datos Personales" in data:
    df = pd.DataFrame(data["Datos Personales"])
    df.to_json("data_catalog_fixed.json", orient="records", force_ascii=False, indent=4)
else:
    print('No se encontró el subdominio "Datos Personales" en el JSON.')