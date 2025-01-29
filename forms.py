import streamlit as st

class ManualForm:
    @staticmethod
    def agregar_manual_form(db):
        with st.form("Agregar Manual", clear_on_submit=True):
            categorias_opciones = ["Operaciones", "Estrategia", "Táctica", "Logística", "Inteligencia"]
            categoria = st.selectbox("Categoría:", categorias_opciones)
            nombre = st.text_input("Nombre del Manual:")
            anio = st.number_input("Año:", min_value=2019, max_value=2030, step=1)
            estado = st.selectbox("Estado:", ["Publicado", "En Generación", "Actualización", "Por Generar", "Archivado"])
            submitted = st.form_submit_button("Agregar")

            if submitted:
                if categoria and nombre.strip() and anio and estado:
                    db.add_manual(categoria, nombre, anio, estado)
                    st.success(f"Manual '{nombre}' agregado correctamente.")
                else:
                    st.error("Todos los campos son obligatorios.")

    @staticmethod
    def modificar_manual_form(db, manual_id):
        if not db.manual_exists(manual_id):
            st.error(f"No existe un manual con ID {manual_id}.")
            return

        with st.form("Modificar Manual"):
            categorias_opciones = ["Operaciones", "Estrategia", "Táctica", "Logística", "Inteligencia"]
            categoria = st.selectbox("Nueva Categoría:", categorias_opciones)
            nombre = st.text_input("Nuevo Nombre del Manual:")
            anio = st.number_input("Nuevo Año:", min_value=2019, max_value=2030, step=1)
            estado = st.selectbox("Nuevo Estado:", ["Publicado", "En Generación", "Actualización", "Por Generar", "Archivado"])
            submitted = st.form_submit_button("Actualizar")

            if submitted:
                if categoria and nombre.strip() and anio and estado:
                    db.update_manual(manual_id, categoria, nombre, anio, estado)
                    st.success(f"Manual con ID {manual_id} actualizado correctamente.")
                else:
                    st.error("Todos los campos son obligatorios para la actualización.")
