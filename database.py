import sqlite3 

class DatabaseManager:
    def __init__(self, db_name="mapa_doctrinario.db"):
        # Inicializar la conexión y el cursor
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def create_table(self):
        # Crear la tabla solo si no existe
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS manuales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria_x TEXT NOT NULL,
            subcategoria_x TEXT NOT NULL,
            categoria_y TEXT NOT NULL,
            nombre TEXT NOT NULL,
            anio INTEGER NOT NULL,
            estado TEXT NOT NULL,
            subproceso_estado TEXT
        )
        ''')
        self.conn.commit()

    # Otros métodos de la clase DatabaseManager se mantienen sin cambios
    def add_manual(self, categoria_x, subcategoria_x, categoria_y, nombre, anio, estado, subproceso_estado):
        print(f"Insertando manual: {categoria_x}, {subcategoria_x}, {categoria_y}, {nombre}, {anio}, {estado}, {subproceso_estado}")
        self.cursor.execute(
        '''
        INSERT INTO manuales (categoria_x, subcategoria_x, categoria_y, nombre, anio, estado, subproceso_estado)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''',
        (categoria_x, subcategoria_x, categoria_y, nombre, anio, estado, subproceso_estado)
        )
        self.conn.commit()

    def fetch_data(self):
        # Obtener todos los registros de la tabla
        self.cursor.execute("SELECT * FROM manuales")
        return self.cursor.fetchall()

    def close_connection(self):
        # Cerrar conexión con la base de datos
        self.conn.close()
