import streamlit as st
import pandas as pd

class Visualization:
    @staticmethod
    def mostrar_mapa(db):
        """
        Muestra un mapa doctrinario en formato de matriz con todos los datos ingresados.
        """
        # Obtener datos desde la base de datos
        data = db.fetch_data()

        # Si no hay datos, mostrar advertencia
        if not data:
            st.warning("No hay datos disponibles para mostrar.")
            return

        # Crear un DataFrame con las columnas correctas
        df = pd.DataFrame(data, columns=[
            "ID", "Categoría X", "Subcategoría X", "Categoría Y", 
            "Nombre del Manual", "Año", "Estado", "Subproceso Estado"
        ])

        # Crear una tabla pivotada
        df["Detalles"] = (
            "Nombre: " + df["Nombre del Manual"] + "<br>" +
            "Año: " + df["Año"].astype(str) + "<br>" +
            "Estado: " + df["Estado"] + "<br>" +
            "Subproceso: " + df["Subproceso Estado"].fillna("-")
        )

        matriz = df.pivot_table(
            index="Categoría Y",  # Filas: Eje Y
            columns="Categoría X",  # Columnas: Eje X
            values="Detalles",  # Mostrar los detalles en cada celda
            aggfunc="first",  # Mostrar el primer valor si hay duplicados
            fill_value="-"  # Mostrar "-" si no hay datos
        )

        # Mostrar la tabla pivotada con HTML para texto enriquecido
        st.write("### Mapa Doctrinario - Tabla General")
        st.write(
            matriz.to_html(escape=False, index=True),  # Deshabilitar el escape de HTML
            unsafe_allow_html=True
        )
