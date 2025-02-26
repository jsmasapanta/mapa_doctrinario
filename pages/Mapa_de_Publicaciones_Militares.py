import streamlit as st
from publicaciones.database import DoctrinarioDB
from publicaciones.publicacion_form import PublicacionForm
from visualization import Visualization
from excel_generator import ExcelGenerator

st.set_page_config(page_title="Mapa de Publicaciones militares")
# Estilo personalizado para los colores de la interfaz
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #d9d9d9 !important;
        color: black !important;
        z-index: 2;
        box-shadow: 2px 0px 5px rgba(0, 0, 0, 0.5);
    }
    [data-testid="stSidebar"] .css-1v3fvcr, [data-testid="stSidebar"] .css-qrbaxs {
        font-size: 20px !important;
        color: black !important;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #f5f5dc !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    # Configurar menú lateral
    st.sidebar.image("cede.png", use_container_width=True)
    st.sidebar.markdown("<h1>Menú</h1>", unsafe_allow_html=True)
    
    # Se agregan las opciones para Manuales y Publicaciones
    menu = [
        "Inicio",
        "Agregar Publicación",
        "Modificar Publicación",
        "Borrar Publicación",
        "Ver Publicaciones",
        "Generar Excel"
    ]
    choice = st.sidebar.radio("Seleccione una opción:", menu)

    db_file = "doctrina.db"  # Ruta al archivo de la base de datos SQLite
    db = DoctrinarioDB(db_file)

    # Navegar entre las opciones
    if choice == "Inicio":
        st.title("🏠 Mapa de Publicaciones Militares")
        st.write("Usa el menú de la izquierda para navegar por las opciones.")
        
    elif choice == "Agregar Publicación":
        st.title("➕ Agregar Publicación")
        PublicacionForm.agregar_publicacion_form(db)
        
    elif choice == "Modificar Publicación":
        st.title("✏️ Modificar Publicación")
        publicacion_id = st.text_input("ID de la Publicación a Modificar:")
        if publicacion_id:
            PublicacionForm.modificar_publicacion_form(db, publicacion_id)

    elif choice == "Ver Publicaciones":
        st.title("📚 Ver Publicaciones")
        PublicacionForm.ver_publicaciones(db)
            
    elif choice == "Borrar Publicación":
        st.title("🗑️ Borrar Publicación")
        PublicacionForm.borrar_publicacion_form(db)
        
    elif choice == "Generar Excel":
        st.title("📊 Generar Excel")
        ExcelGenerator.generar_excel_filtrado(db_file)

if __name__ == "__main__":
    main()
