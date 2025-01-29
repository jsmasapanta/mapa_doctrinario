import streamlit as st
from graphviz import Digraph
import pandas as pd

class Visualization:
    @staticmethod
    def mostrar_mapa(db):
        # Obtener los datos de la base de datos
        data = db.fetch_data()
        if not data:
            st.warning("No hay datos disponibles para mostrar.")
            return

        # Opciones para seleccionar el tipo de mapa
        st.sidebar.subheader("Opciones de Mapa")
        tipo_mapa = st.sidebar.radio("Seleccione el tipo de representación:", ["Mapa Conceptual", "Cuadro Sinóptico"])
        
        # Filtrar datos por categoría si se selecciona "Mapa por Categoría"
        st.sidebar.subheader("Opciones de Filtro")
        tipo_mapa_datos = st.sidebar.radio("Seleccione el tipo de datos:", ["Mapa Completo", "Mapa por Categoría"])
        if tipo_mapa_datos == "Mapa por Categoría":
            categorias_disponibles = list(set(row[1] for row in data))
            categoria_seleccionada = st.sidebar.selectbox("Seleccione la Categoría:", categorias_disponibles)
            data = [row for row in data if row[1] == categoria_seleccionada]

        if not data:
            st.warning("No hay datos disponibles para la selección realizada.")
            return

        if tipo_mapa == "Mapa Conceptual":
            Visualization.mostrar_mapa_conceptual(data)
        elif tipo_mapa == "Cuadro Sinóptico":
            Visualization.mostrar_cuadro_sinoptico(data)

    @staticmethod
    def mostrar_mapa_conceptual(data):
        # Colores asignados a categorías
        colores_categorias = {
            "Operaciones": "lightblue",
            "Estrategia": "lightgreen",
            "Táctica": "lightpink",
            "Logística": "lightyellow",
            "Inteligencia": "lightcoral",
        }

        # Crear un grafo dirigido para el mapa conceptual
        dot = Digraph()
        dot.attr(rankdir="TB")  # Orientación de arriba hacia abajo
        dot.attr("node", fontname="Arial", style="filled")

        # Nodo principal del mapa doctrinario
        dot.node("Mapa", "MAPA DOCTRINARIO DEL EJÉRCITO", shape="box", color="blue", fontcolor="white")

        # Nodos de categorías y manuales
        categorias = {}
        for id_manual, categoria, nombre, anio, estado in data:
            # Asignar color a la categoría
            color_categoria = colores_categorias.get(categoria, "lightgrey")

            # Crear nodo de categoría si no existe
            if categoria not in categorias:
                dot.node(f"Categoria_{categoria}", categoria, shape="box", color=color_categoria)
                dot.edge("Mapa", f"Categoria_{categoria}")  # Conectar categoría al nodo principal
                categorias[categoria] = color_categoria

            # Crear nodo del manual con el color de la categoría
            manual_label = f"{nombre}\n(Año: {anio}, Estado: {estado})"
            dot.node(f"Manual_{id_manual}", manual_label, shape="box", color=categorias[categoria])
            dot.edge(f"Categoria_{categoria}", f"Manual_{id_manual}")  # Conectar manual a la categoría

        # Renderizar el mapa conceptual
        st.graphviz_chart(dot, use_container_width=True)

    @staticmethod
    def mostrar_cuadro_sinoptico(data):
        # Crear un DataFrame para la representación en tabla
        df = pd.DataFrame(data, columns=["ID", "Categoría", "Nombre", "Año", "Estado"])

        # Asignar colores a las categorías
        colores_categorias = {
            "Operaciones": "background-color: lightblue",
            "Estrategia": "background-color: lightgreen",
            "Táctica": "background-color: lightpink",
            "Logística": "background-color: lightyellow",
            "Inteligencia": "background-color: lightcoral",
        }

        # Aplicar estilo basado en la categoría
        def aplicar_colores(row):
            color = colores_categorias.get(row["Categoría"], "")
            return [color] * len(row)

        # Mostrar el cuadro sin óptico con estilos
        styled_table = df.style.apply(aplicar_colores, axis=1)
        st.table(styled_table)
