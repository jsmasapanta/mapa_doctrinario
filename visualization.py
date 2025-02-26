import streamlit as st
import pandas as pd
import numpy as np
from database import DatabaseManager

class Visualization:
    @staticmethod
    def mostrar_mapa_filtrado(db_file):
        # Inicializar la conexión con la base de datos SQLite
        db = DatabaseManager(db_file)

        # Obtener datos desde la base de datos
        data = db.fetch_data()

        if not data:
            st.warning("No hay datos disponibles para mostrar.")
            return

        # Crear DataFrame con las columnas necesarias
        columnas = [
            "ID", "id_categoria", "categoria_x", "subcategoria_x", "categoria_y", 
            "nombre", "anio", "estado", "subproceso_estado"
        ]

        # Convertir los datos en un DataFrame y manejar valores que falten
        df = pd.DataFrame(data)
        for columna in columnas:
            if columna not in df.columns:
                df[columna] = "Desconocido"  # Llena las columnas faltantes con un valor predeterminado
            else:
                df[columna] = df[columna].replace({np.nan: "Desconocido", None: "Desconocido"})  # Reemplaza NaN o None

        # Renombrar columnas para mostrarlas de forma clara en Streamlit
        df.rename(columns={
            "categoria_x": "Categoría X",
            "subcategoria_x": "Subcategoría X",
            "categoria_y": "Categoría Y",
            "nombre": "Nombre del Manual",
            "anio": "Año",
            "estado": "Estado",
            "subproceso_estado": "Subproceso Estado"
        }, inplace=True)

        # Formatear correctamente el año (eliminar la coma en valores numéricos)
        df["Año"] = df["Año"].astype(str).str.replace(",", "")

        # Reemplazar "Desconocido" en "Subproceso Estado" por "No Aplica"
        df["Subproceso Estado"] = df["Subproceso Estado"].replace("Desconocido", "No Aplica")

        # Eliminar las columnas "ID" y "id_categoria"
        df = df.drop(columns=["ID", "id_categoria"], errors='ignore')

        # 🔹 Mostrar la tabla
        st.write("### 🗺️ Mapa Doctrinario")
        st.dataframe(df)

# Uso de la visualización
if __name__ == "__main__":
    db_file = "doctrina.db"  # Ruta al archivo de la base de datos SQLite
    Visualization.mostrar_mapa_filtrado(db_file)