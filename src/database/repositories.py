"""
Módulo de operaciones sobre la base de datos.

Contiene funciones para insertar, consultar
y gestionar estudiantes, asignaturas y calificaciones.
"""

from src.database.connection import obtener_conexion
from src.services.validators import validar_nombre, validar_email
from src.services.validators import (
    validar_nombre,
    validar_email,
    validar_codigo_asignatura,
    validar_creditos,
    validar_nota
)
from datetime import datetime


def insertar_estudiante(nombre, email):
    """
    Inserta un nuevo estudiante en la base de datos.
    """

    if not validar_nombre(nombre):
        print("Nombre no válido")
        return False

    if not validar_email(email):
        print("Email no válido")
        return False

    conexion = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO estudiantes (nombre, email)
            VALUES (?, ?)
        """, (
            nombre.strip(),
            email.strip().lower()
        ))

        conexion.commit()
        return True

    except Exception as error:
        print(f"Error al insertar estudiante: {error}")
        return False

    finally:
        if conexion:
            conexion.close()
    
def insertar_asignatura(nombre, codigo, creditos):
    """
    Inserta una nueva asignatura en la base de datos.
    """

    if not validar_nombre(nombre):
        print("Nombre de asignatura no válido")
        return False

    if not validar_codigo_asignatura(codigo):
        print("Código de asignatura no válido")
        return False

    if not validar_creditos(creditos):
        print("Créditos no válidos")
        return False

    conexion = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO asignaturas (nombre, codigo, creditos)
            VALUES (?, ?, ?)
        """, (
            nombre.strip(),
            codigo.strip().upper(),
            creditos
        ))

        conexion.commit()
        return True

    except Exception as error:
        print(f"Error al insertar asignatura: {error}")
        return False

    finally:
        if conexion:
            conexion.close()


from datetime import datetime


def insertar_calificacion(estudiante_id, asignatura_id, nota):
    """
    Inserta una nueva calificación en la base de datos.
    """

    if not validar_nota(nota):
        print("Nota no válida")
        return False

    conexion = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        fecha_actual = datetime.now().strftime("%Y-%m-%d")

        cursor.execute("""
            INSERT INTO calificaciones (
                estudiante_id,
                asignatura_id,
                nota,
                fecha_registro
            )
            VALUES (?, ?, ?, ?)
        """, (
            estudiante_id,
            asignatura_id,
            nota,
            fecha_actual
        ))

        conexion.commit()
        return True

    except Exception as error:
        print(f"Error al insertar calificación: {error}")
        return False

    finally:
        if conexion:
            conexion.close()