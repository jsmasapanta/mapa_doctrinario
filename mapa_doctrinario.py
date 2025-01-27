import streamlit as st
import sqlite3
import pandas as pd

# Database setup
def init_db():
    conn = sqlite3.connect("mapa_doctrinario.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS manuales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        categoria TEXT NOT NULL,
        nombre TEXT NOT NULL,
        anio INTEGER NOT NULL
    )
    ''')
    conn.commit()
    return conn

# Fetch data from the database
def fetch_data(conn):
    query = "SELECT * FROM manuales"
    df = pd.read_sql_query(query, conn)
    return df

# Add a manual to the database
def add_manual(conn, categoria, nombre, anio):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO manuales (categoria, nombre, anio) VALUES (?, ?, ?)", (categoria, nombre, anio))
    conn.commit()

# Main application
def main():
    st.title("Mapa Doctrinario del Ejército")
    st.sidebar.title("Menú")

    conn = init_db()

    menu = ["Inicio", "Agregar Manual", "Ver Mapa", "Exportar Listado"]
    choice = st.sidebar.selectbox("Opciones", menu)

    if choice == "Inicio":
        st.subheader("Bienvenido al Mapa Doctrinario del Ejército")
        st.write("Utiliza el menú de la izquierda para navegar por las opciones.")

    elif choice == "Agregar Manual":
        st.subheader("Agregar un Nuevo Manual")
        with st.form("Agregar Manual"):
            categoria = st.text_input("Categoría:")
            nombre = st.text_input("Nombre del Manual:")
            anio = st.number_input("Año:", min_value=1900, max_value=2100, step=1)
            submitted = st.form_submit_button("Agregar")

            if submitted:
                if categoria and nombre and anio:
                    add_manual(conn, categoria, nombre, anio)
                    st.success(f"Manual '{nombre}' agregado correctamente.")
                else:
                    st.error("Todos los campos son obligatorios.")

    elif choice == "Ver Mapa":
        st.subheader("Mapa Doctrinario")
        df = fetch_data(conn)
        if not df.empty:
            counts = df["categoria"].value_counts()
            st.bar_chart(counts)
        else:
            st.warning("No hay datos disponibles para mostrar.")

    elif choice == "Exportar Listado":
        st.subheader("Exportar Listado de Manuales")
        df = fetch_data(conn)
        if not df.empty:
            st.download_button(
                label="Descargar Listado en Excel",
                data=df.to_excel(index=False, engine='openpyxl'),
                file_name="listado_manuales.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        else:
            st.warning("No hay datos para exportar.")

if __name__ == "__main__":
    main()
