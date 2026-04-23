"""
Script de carga inicial de datos.

Inserta estudiantes, asignaturas y calificaciones
de ejemplo para poblar la base de datos.
"""

from src.database.schema import crear_tablas
from src.database.repositories import (
    insertar_estudiante,
    insertar_asignatura,
    insertar_calificacion
)


def cargar_datos_iniciales():
    """
    Inserta datos de ejemplo en la base de datos.
    """

    crear_tablas()

    # ----------------------------
    # Estudiantes
    # ----------------------------
    estudiantes = [
        ("Dan Vidal", "dan@email.com"),
        ("Laura Gómez", "laura@email.com"),
        ("Carlos Ruiz", "carlos@email.com"),
        ("Ana Pérez", "ana@email.com"),
        ("Marta López", "marta@email.com")
    ]

    for nombre, email in estudiantes:
        insertar_estudiante(nombre, email)

    # ----------------------------
    # Asignaturas
    # ----------------------------
    asignaturas = [
        ("Bioinformática", "BIO101", 6),
        ("Algoritmos", "ALG201", 6),
        ("Bases de Datos", "BBDD301", 6),
        ("Genética", "GEN102", 6),
        ("Programación", "PRO401", 6)
    ]

    for nombre, codigo, creditos in asignaturas:
        insertar_asignatura(nombre, codigo, creditos)

    # ----------------------------
    # Calificaciones
    # ----------------------------
    calificaciones = [
        (1, 1, 8.5),
        (1, 2, 7.0),
        (1, 3, 9.0),
        (2, 1, 6.5),
        (2, 4, 8.0),
        (3, 2, 5.5),
        (3, 5, 7.5),
        (4, 3, 9.2),
        (4, 4, 8.8),
        (5, 1, 4.5),
        (5, 2, 6.0)
    ]

    for estudiante_id, asignatura_id, nota in calificaciones:
        insertar_calificacion(
            estudiante_id,
            asignatura_id,
            nota
        )

    print("Datos iniciales cargados correctamente")


if __name__ == "__main__":
    cargar_datos_iniciales()