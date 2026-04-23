"""
Módulo de definición del esquema de la base de datos.

Contiene las funciones necesarias para crear las tablas
del sistema de expedientes académicos.
"""

from src.database.connection import obtener_conexion


def crear_tablas():
    """
    Crea las tablas principales de la base de datos si no existen.

    Tablas creadas:
    - estudiantes
    - asignaturas
    - calificaciones
    """

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # --------------------------------------------------
    # Tabla: estudiantes
    # --------------------------------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    """)

    # --------------------------------------------------
    # Tabla: asignaturas
    # --------------------------------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS asignaturas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        codigo TEXT UNIQUE NOT NULL,
        creditos INTEGER NOT NULL CHECK(creditos > 0)
    )
    """)

    # --------------------------------------------------
    # Tabla: calificaciones
    # --------------------------------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS calificaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        estudiante_id INTEGER NOT NULL,
        asignatura_id INTEGER NOT NULL,
        nota REAL NOT NULL CHECK(nota >= 0 AND nota <= 10),
        fecha_registro TEXT NOT NULL,

        FOREIGN KEY (estudiante_id)
            REFERENCES estudiantes(id),

        FOREIGN KEY (asignatura_id)
            REFERENCES asignaturas(id)
    )
    """)

    conexion.commit()
    conexion.close()