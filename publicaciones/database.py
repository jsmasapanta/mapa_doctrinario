import sqlite3
import os

class DoctrinarioDB:
    def __init__(self, db_path=None):
        """
        Inicializa la conexión a la base de datos 'doctrinario.db' 
        y crea la tabla 'publicaciones' si no existe.
        """
        if db_path is None:
            # Ajustar la ruta para que apunte a una carpeta anterior
            self.db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "doctrina.db")
        else:
            self.db_path = db_path
        self._create_table_publicaciones()

    def _create_table_publicaciones(self):
        """
        Crea la tabla 'publicaciones' si no existe.
        Ajusta el esquema a tu gusto.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS publicaciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                categoria_x TEXT NOT NULL,
                subcategoria_x TEXT,
                categoria_y TEXT NOT NULL,
                nombre TEXT NOT NULL,
                anio TEXT NOT NULL,
                estado TEXT NOT NULL,
                subproceso_estado TEXT
            );
        """)
        conn.commit()
        conn.close()

    # ------------------- CRUD Publicaciones ------------------- #
    def add_publicacion(self, categoria_x, subcategoria_x, categoria_y, 
                        nombre, anio, estado, subproceso_estado):
        """
        Inserta una nueva publicación en la tabla 'publicaciones'.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO publicaciones (
                categoria_x, subcategoria_x, categoria_y, 
                nombre, anio, estado, subproceso_estado
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (categoria_x, subcategoria_x, categoria_y, nombre, anio, estado, subproceso_estado))
        conn.commit()
        conn.close()

    def fetch_publicacion_by_id(self, publicacion_id):
        """
        Devuelve un diccionario con los datos de la publicación según su ID.
        Retorna None si no se encuentra.
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Para devolver diccionarios
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM publicaciones WHERE id = ?", (publicacion_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return dict(row)
        return None

    def fetch_all_publicaciones(self):
        """
        Devuelve una lista de diccionarios con todas las publicaciones.
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Para devolver diccionarios
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM publicaciones")
        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    def update_publicacion(self, publicacion_id, categoria_x, subcategoria_x, 
                           categoria_y, nombre, anio, estado, subproceso_estado):
        """
        Actualiza una publicación existente por su ID.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE publicaciones
            SET categoria_x = ?,
                subcategoria_x = ?,
                categoria_y = ?,
                nombre = ?,
                anio = ?,
                estado = ?,
                subproceso_estado = ?
            WHERE id = ?
        """, (categoria_x, subcategoria_x, categoria_y, nombre, anio, 
              estado, subproceso_estado, publicacion_id))
        conn.commit()
        conn.close()

    def delete_publicacion(self, publicacion_id):
        """
        Elimina una publicación según su ID.
        Retorna True si se borró, False si no existía.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM publicaciones WHERE id = ?", (publicacion_id,))
        conn.commit()
        rows_deleted = cursor.rowcount
        conn.close()

        return rows_deleted > 0