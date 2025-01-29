import sqlite3

class DatabaseManager:
    def __init__(self, db_name="mapa_doctrinario.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS manuales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT NOT NULL,
            nombre TEXT NOT NULL,
            anio INTEGER NOT NULL,
            estado TEXT NOT NULL
        )
        ''')
        self.conn.commit()

    def add_manual(self, categoria, nombre, anio, estado):
        self.cursor.execute("INSERT INTO manuales (categoria, nombre, anio, estado) VALUES (?, ?, ?, ?)",
                            (categoria, nombre, anio, estado))
        self.conn.commit()

    def update_manual(self, manual_id, categoria, nombre, anio, estado):
        self.cursor.execute("UPDATE manuales SET categoria = ?, nombre = ?, anio = ?, estado = ? WHERE id = ?",
                            (categoria, nombre, anio, estado, manual_id))
        self.conn.commit()

    def delete_manual(self, manual_id):
        self.cursor.execute("DELETE FROM manuales WHERE id = ?", (manual_id,))
        self.conn.commit()

    def fetch_data(self):
        return self.cursor.execute("SELECT * FROM manuales").fetchall()

    def manual_exists(self, manual_id):
        result = self.cursor.execute("SELECT 1 FROM manuales WHERE id = ?", (manual_id,)).fetchone()
        return result is not None

    def close_connection(self):
        self.conn.close()

    def __del__(self):
        self.close_connection()
