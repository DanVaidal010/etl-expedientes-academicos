"""
Módulo de estadísticas académicas.

Contiene funciones para calcular métricas
y consultas analíticas sobre los expedientes.
"""

from src.database.connection import obtener_conexion


def obtener_media_por_estudiante():
    """
    Devuelve la nota media de cada estudiante.

    Returns:
        list: Lista de estudiantes con su nota media.
    """

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            e.nombre,
            ROUND(AVG(c.nota), 2) AS nota_media
        FROM estudiantes e
        JOIN calificaciones c
            ON e.id = c.estudiante_id
        GROUP BY e.id
        ORDER BY nota_media DESC
    """)

    resultados = cursor.fetchall()
    conexion.close()

    return resultados

def obtener_media_por_asignatura():
    """
    Devuelve la nota media de cada asignatura.

    Returns:
        list: Lista de asignaturas con su nota media.
    """

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            a.nombre,
            a.codigo,
            ROUND(AVG(c.nota), 2) AS nota_media
        FROM asignaturas a
        JOIN calificaciones c
            ON a.id = c.asignatura_id
        GROUP BY a.id
        ORDER BY nota_media DESC
    """)

    resultados = cursor.fetchall()
    conexion.close()

    return resultados

def obtener_estadisticas_generales():
    """
    Devuelve estadísticas académicas generales.

    Returns:
        dict: Diccionario con métricas generales.
    """

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # Total estudiantes
    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM estudiantes
    """)
    total_estudiantes = cursor.fetchone()["total"]

    # Total asignaturas
    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM asignaturas
    """)
    total_asignaturas = cursor.fetchone()["total"]

    # Total calificaciones
    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM calificaciones
    """)
    total_calificaciones = cursor.fetchone()["total"]

    # Media global
    cursor.execute("""
        SELECT ROUND(AVG(nota), 2) AS media_global
        FROM calificaciones
    """)
    media_global = cursor.fetchone()["media_global"]

    # Aprobados (nota >= 5)
    cursor.execute("""
        SELECT COUNT(*) AS aprobados
        FROM calificaciones
        WHERE nota >= 5
    """)
    aprobados = cursor.fetchone()["aprobados"]

    conexion.close()

    return {
        "total_estudiantes": total_estudiantes,
        "total_asignaturas": total_asignaturas,
        "total_calificaciones": total_calificaciones,
        "media_global": media_global,
        "aprobados": aprobados
    }

def obtener_todas_las_notas():
    """
    Devuelve todas las calificaciones registradas.

    Returns:
        list: Lista con todas las notas.
    """

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT nota
        FROM calificaciones
    """)

    resultados = cursor.fetchall()
    conexion.close()

    return [fila["nota"] for fila in resultados]