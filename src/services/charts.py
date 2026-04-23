"""
Módulo de generación de gráficos.

Contiene funciones para representar visualmente
las estadísticas académicas del sistema.
"""

import matplotlib.pyplot as plt
from src.services.statistics import obtener_media_por_estudiante


def grafico_media_por_estudiante():
    """
    Genera un gráfico de barras con la nota media
    de cada estudiante.
    """

    datos = obtener_media_por_estudiante()

    nombres = []
    medias = []

    for fila in datos:
        nombres.append(fila["nombre"])
        medias.append(fila["nota_media"])

    plt.figure(figsize=(8, 5))
    plt.bar(nombres, medias)

    plt.title("Nota media por estudiante")
    plt.xlabel("Estudiantes")
    plt.ylabel("Nota media")

    plt.ylim(0, 10)
    plt.tight_layout()
    plt.show()

from src.services.statistics import (
    obtener_media_por_estudiante,
    obtener_todas_las_notas
)


def histograma_notas():
    """
    Genera un histograma con la distribución
    de todas las calificaciones registradas.
    """

    notas = obtener_todas_las_notas()

    plt.figure(figsize=(8, 5))
    plt.hist(notas, bins=5)

    plt.title("Distribución de calificaciones")
    plt.xlabel("Notas")
    plt.ylabel("Frecuencia")

    plt.xlim(0, 10)
    plt.tight_layout()
    plt.show()