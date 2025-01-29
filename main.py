import streamlit as st
from database import DatabaseManager
from forms import ManualForm
from visualization import Visualization
from excel_generator import ExcelGenerator

# Estilo personalizado para los colores de la interfaz
st.markdown(
    """
    <style>
    /* Estilo del menú lateral */
    [data-testid="stSidebar"] {{
        background-color: #d9d9d9 !important; /* Gris claro */
        color: black !important; /* Texto negro */
        z-index: 2; /* Asegura que el menú esté al frente */
        box-shadow: 2px 0px 5px rgba(0, 0, 0, 0.5); /* Sombra para destacar */
    }}

    /* Ajuste del color del texto dentro del menú */
    [data-testid="stSidebar"] .css-1v3fvcr, [data-testid="stSidebar"] .css-qrbaxs {{
        font-size: 20px !important;
        color: black !important;
    }}

    /* Fondo del contenedor principal (lado derecho) */
    [data-testid="stAppViewContainer"] {{
        background-color: #f5f5dc !important; /* Blanco hueso */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    # Configurar menú lateral
    st.sidebar.image("cede.png", use_container_width=True)
    st.sidebar.markdown("<h1>Menú</h1>", unsafe_allow_html=True)
    menu = ["Inicio", "Agregar Manual", "Ver Mapa", "Modificar Manual", "Generar Excel"]
    choice = st.sidebar.radio("Seleccione una opción:", menu)

    # Inicializar la base de datos
    db = DatabaseManager()
    db.create_table()

    # Navegar entre las opciones
    if choice == "Inicio":
        st.title("🏠 Bienvenido al Mapa Doctrinario del Ejército")
        st.write("Usa el menú de la izquierda para navegar por las opciones.")
    elif choice == "Agregar Manual":
        st.title("➕ Agregar Manual")
        ManualForm.agregar_manual_form(db)
    elif choice == "Ver Mapa":
        st.title("🗺️ Representaciones del Mapa Doctrinario")
        Visualization.mostrar_mapa(db)

    elif choice == "Modificar Manual":
        st.title("✏️ Modificar Manual")
        manual_id = st.number_input("ID del Manual a Modificar:", min_value=1, step=1)
        ManualForm.modificar_manual_form(db, manual_id)
    elif choice == "Generar Excel":
        st.title("📊 Generar Excel")
        # Mostrar las opciones de filtro directamente en esta sección
        st.write("Selecciona las opciones de filtro antes de generar el archivo Excel.")
        ExcelGenerator.generar_excel_filtrado(db)

if __name__ == "__main__":
    main()
