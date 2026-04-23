"""
Módulo de conexión a la base de datos.

Proporciona funciones para establecer la conexión
con la base de datos SQLite del proyecto.
"""

import sqlite3
import os

# Carpeta y ruta de la base de datos
CARPETA_DATOS = "data"
RUTA_BD = os.path.join(CARPETA_DATOS, "academic_records.db")


def obtener_conexion():
    """
    Crea y devuelve una conexión a la base de datos SQLite.

    Returns:
        sqlite3.Connection: Objeto de conexión a la base de datos.
    """

    # Crear carpeta data si no existe
    if not os.path.exists(CARPETA_DATOS):
        os.makedirs(CARPETA_DATOS)

    conexion = sqlite3.connect(RUTA_BD)
    conexion.row_factory = sqlite3.Row

    return conexion