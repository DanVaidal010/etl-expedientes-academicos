"""
Panel de visualización y análisis académico.

Muestra estadísticas generales del sistema
y permite abrir gráficos de análisis.
"""

from tkinter import ttk

from src.services.statistics import (
    obtener_estadisticas_generales
)

from src.services.charts import (
    grafico_media_por_estudiante,
    histograma_notas
)


def crear_dashboard(panel):
    """
    Crea el panel de estadísticas académicas.

    Args:
        panel: Frame donde se dibuja el dashboard.
    """

    ttk.Label(
        panel,
        text="Dashboard Académico",
        font=("Arial", 16)
    ).pack(pady=20)

    estadisticas = obtener_estadisticas_generales()

    texto = (
        f"Total estudiantes: "
        f"{estadisticas['total_estudiantes']}\n\n"

        f"Total asignaturas: "
        f"{estadisticas['total_asignaturas']}\n\n"

        f"Total calificaciones: "
        f"{estadisticas['total_calificaciones']}\n\n"

        f"Media global: "
        f"{estadisticas['media_global']}\n\n"

        f"Aprobados: "
        f"{estadisticas['aprobados']}"
    )

    ttk.Label(
        panel,
        text=texto,
        font=("Arial", 12),
        justify="left"
    ).pack(pady=20)

    # ----------------------------
    # Botón gráfico medias
    # ----------------------------
    ttk.Button(
        panel,
        text="Ver gráfico de medias por estudiante",
        command=grafico_media_por_estudiante
    ).pack(pady=10)

    # ----------------------------
    # Botón histograma
    # ----------------------------
    ttk.Button(
        panel,
        text="Ver histograma de calificaciones",
        command=histograma_notas
    ).pack(pady=10)