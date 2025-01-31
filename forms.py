import streamlit as st

class ManualForm:
    @staticmethod
    def agregar_manual_form(db):
        

        # Categorías principales del eje X
        categorias_x = [
            "Esencial",
            "Acción Decisiva",
            "Sistemas Operativos en el Campo de Batalla",
            "Complementarios al Desarrollo de Doctrina"
        ]

        # Subcategorías dependientes del eje X
        subcategorias = {
            "Esencial": ["Ejército"],
            "Acción Decisiva": ["Maniobra", "AIE", "Operaciones Especiales"],
            "Sistemas Operativos en el Campo de Batalla": [
                "Inteligencia", "Mando Tipo Misión", "Apoyo de Fuegos", "Ingeniería", "Sostenimiento"
            ],
            "Complementarios al Desarrollo de Doctrina": [
                "Doctrina", "Términos y Símbolos Militares", "Proceso de Operaciones", "Liderazgo", "Entrenamiento de Unidades"
            ]
        }

        # Selección dinámica de categoría y subproceso en el eje X
        categoria_x = st.selectbox("Codificación Eje X:", categorias_x)
        subprocesos_x = subcategorias.get(categoria_x, [])
        subcategoria_x = st.selectbox("Codificación Eje Y:", subprocesos_x)

        # Categorías del eje Y
        categorias_y = [
            "Manuales Fundamentales del Ejército",
            "Manuales Fundamentales de Referencia del Ejército",
            "Manuales de Campaña del Ejército",
            "Manuales de Técnicas del Ejército"  
        ]
        categoria_y = st.selectbox("Subcodificación Eje Y:", categorias_y)

       
        # Otros campos
        nombre = st.text_input("Nombre del Manual:")
        anio = st.number_input("Año de Publicación:", min_value=2018, max_value=2030, step=1)

         # Estado del Manual y Subprocesos
        estados = ["Publicado", "Actualización", "En Generación"]
        estado = st.selectbox("Estado del Manual:", estados)

        subprocesos_estado = []
        if estado == "En Generación":
            subprocesos_estado = ["Investigación", "Experimentación", "Edición y Difusión"]
            subproceso_estado = st.selectbox("Subproceso del Estado:", subprocesos_estado)
        else:
            subproceso_estado = None  # Si no es "En Generación", no hay subproceso.

        # Botón para enviar
        if st.button("Agregar Manual"):
            if categoria_x and subcategoria_x and categoria_y and nombre and anio and estado:
                db.add_manual(categoria_x, subcategoria_x, categoria_y, nombre, anio, estado, subproceso_estado)
                st.success(f"✅ Manual '{nombre}' agregado correctamente en '{categoria_x} -> {subcategoria_x}', '{categoria_y}', estado '{estado}' y subproceso '{subproceso_estado}'.")
            else:
                st.error("❌ Todos los campos son obligatorios. Por favor, completa la información.")
