import streamlit as st

st.set_page_config(page_title="Inicio", page_icon="🏠")

def main():
    st.title("🏠 Bienvenido al Mapa Doctrinario del Ejército")
    st.write("Usa los botones para navegar por las opciones.")
    
    # Centrar la imagen usando columnas
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image("cede.png", width=200)
    
    # Centrar los botones usando columnas
    col1, col2, col3, col4 = st.columns(4)
    with col2:
        if st.button("Mapa Doctrinario"):
            st.switch_page("pages/Mapa_Doctrinario.py")
    with col3:
        if st.button("Mapa de Publicaciones Militares"):
            st.switch_page("pages/Mapa_de_Publicaciones_Militares.py")
    # Configurar menú lateral
    st.sidebar.image("cede.png", use_container_width=True)
    st.sidebar.markdown("<h1>Menú</h1>", unsafe_allow_html=True)
    menu = ["Inicio", "Agregar Manual", "Ver Mapa", "Modificar Manual", "Generar Excel", "Borrar Manual"]
    choice = st.sidebar.radio("Seleccione una opción:", menu)

    db = DatabaseManager("firebase_credenciales.json")  # Solo la credencial

    # Navegar entre las opciones
    if choice == "Inicio":
        st.title("🏠 Bienvenido al Mapa Doctrinario del Ejército")
        st.write("Usa el menú de la izquierda para navegar por las opciones.")
    elif choice == "Agregar Manual":
        st.title("➕ Agregar Manual")
        ManualForm.agregar_manual_form(db)
    elif choice == "Ver Mapa":
        st.title("🗺️ Mapa Doctrinario Filtrado")
        Visualization.mostrar_mapa_filtrado(db)
    elif choice == "Modificar Manual":
        st.title("✏️ Modificar Manual")
        manual_id = st.text_input("ID del Manual a Modificar:")
        if manual_id:
            ManualForm.modificar_manual_form(db, manual_id)
    elif choice == "Generar Excel":
        st.title("📊 Generar Excel")
        st.write("Selecciona las opciones de filtro antes de generar el archivo Excel.")
        ExcelGenerator.generar_excel_filtrado(db)
    elif choice == "Borrar Manual":
        st.title("🗑️ Borrar Manual")
        ManualForm.borrar_manual_form(db)

if __name__ == "__main__":
    main()
