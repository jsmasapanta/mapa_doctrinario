import streamlit as st
import pandas as pd
from io import BytesIO

class ExcelGenerator:
    @staticmethod
    def generar_excel_filtrado(db):
        # Obtener los datos de la base de datos
        data = db.fetch_data()
        df = pd.DataFrame(data, columns=["ID", "Categoría", "Nombre", "Año", "Estado"])

        if df.empty:
            st.warning("No hay datos disponibles para generar el Excel.")
            return

        # Mostrar filtros directamente
        categorias = st.multiselect("Filtrar por Categoría:", df["Categoría"].unique())
        años = st.multiselect("Filtrar por Año:", df["Año"].unique())
        estados = st.multiselect("Filtrar por Estado:", df["Estado"].unique())

        # Aplicar los filtros seleccionados
        if categorias:
            df = df[df["Categoría"].isin(categorias)]
        if años:
            df = df[df["Año"].isin(años)]
        if estados:
            df = df[df["Estado"].isin(estados)]

        if df.empty:
            st.warning("No se encontraron datos con los filtros aplicados.")
            return

        # Crear un archivo Excel en memoria
        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="Manuales")
            workbook = writer.book
            worksheet = writer.sheets["Manuales"]

            # Ajustar las columnas automáticamente
            for column in df:
                col_idx = df.columns.get_loc(column)  # Índice de la columna
                max_len = df[column].astype(str).map(len).max() + 2  # Longitud máxima
                worksheet.set_column(col_idx, col_idx, max_len)

        # Botón para descargar el Excel generado
        st.download_button(
            label="📥 Descargar Excel",
            data=output.getvalue(),
            file_name="manuales_filtrados.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
