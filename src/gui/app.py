"""
Aplicación principal de la interfaz gráfica.

Gestiona la ventana principal y los paneles
del sistema académico.
"""

import tkinter as tk
from tkinter import ttk
from src.gui.input_panel import (
    crear_panel_estudiantes,
    crear_panel_asignaturas,
    crear_panel_calificaciones
)
from src.gui.dashboard_panel import crear_dashboard

def iniciar_aplicacion():
    """
    Inicia la ventana principal de la aplicación.
    """

    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Sistema de Expedientes Académicos")
    ventana.geometry("900x600")

    # Sistema de pestañas
    pestañas = ttk.Notebook(ventana)

    # --------------------------------------------------
    # Panel 1: Introducción de datos
    # --------------------------------------------------
    panel_datos = ttk.Frame(pestañas)
    pestañas.add(
        panel_datos,
        text="Introducción de Datos"
    )

    # Crear formulario de estudiantes
    crear_panel_estudiantes(panel_datos)
    crear_panel_asignaturas(panel_datos)
    crear_panel_calificaciones(panel_datos)

    # --------------------------------------------------
    # Panel 2: Dashboard académico
    # --------------------------------------------------
    panel_dashboard = ttk.Frame(pestañas)
    pestañas.add(
        panel_dashboard,
        text="Dashboard Académico"
    )

    crear_dashboard(panel_dashboard)

    # Mostrar pestañas
    pestañas.pack(
        expand=True,
        fill="both"
    )

    # Ejecutar aplicación
    ventana.mainloop()