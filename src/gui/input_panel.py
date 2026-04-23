"""
Panel de introducción de datos.

Permite registrar nuevos estudiantes
en la base de datos.
"""

from tkinter import ttk
from tkinter import messagebox

from src.database.repositories import insertar_estudiante
from src.database.repositories import insertar_asignatura


def crear_panel_estudiantes(panel):
    """
    Crea el formulario para insertar estudiantes.

    Args:
        panel: Frame donde se dibuja el formulario.
    """

    # ----------------------------
    # Título
    # ----------------------------
    ttk.Label(
        panel,
        text="Registro de estudiantes",
        font=("Arial", 14)
    ).pack(pady=15)

    # ----------------------------
    # Nombre
    # ----------------------------
    ttk.Label(
        panel,
        text="Nombre:"
    ).pack()

    entrada_nombre = ttk.Entry(
        panel,
        width=40
    )
    entrada_nombre.pack(pady=5)

    # ----------------------------
    # Email
    # ----------------------------
    ttk.Label(
        panel,
        text="Email:"
    ).pack()

    entrada_email = ttk.Entry(
        panel,
        width=40
    )
    entrada_email.pack(pady=5)

    # ----------------------------
    # Función guardar
    # ----------------------------
    def guardar_estudiante():
        nombre = entrada_nombre.get()
        email = entrada_email.get()

        resultado = insertar_estudiante(
            nombre,
            email
        )

        if resultado:
            messagebox.showinfo(
                "Éxito",
                "Estudiante registrado correctamente"
            )

            entrada_nombre.delete(0, "end")
            entrada_email.delete(0, "end")

        else:
            messagebox.showerror(
                "Error",
                "No se pudo registrar el estudiante"
            )

    # ----------------------------
    # Botón
    # ----------------------------
    ttk.Button(
        panel,
        text="Guardar estudiante",
        command=guardar_estudiante
    ).pack(pady=20)


def crear_panel_asignaturas(panel):
    """
    Crea el formulario para insertar asignaturas.

    Args:
        panel: Frame donde se dibuja el formulario.
    """

    # ----------------------------
    # Separador visual
    # ----------------------------
    ttk.Separator(
        panel,
        orient="horizontal"
    ).pack(fill="x", pady=20)

    # ----------------------------
    # Título
    # ----------------------------
    ttk.Label(
        panel,
        text="Registro de asignaturas",
        font=("Arial", 14)
    ).pack(pady=10)

    # ----------------------------
    # Nombre
    # ----------------------------
    ttk.Label(
        panel,
        text="Nombre de asignatura:"
    ).pack()

    entrada_nombre = ttk.Entry(
        panel,
        width=40
    )
    entrada_nombre.pack(pady=5)

    # ----------------------------
    # Código
    # ----------------------------
    ttk.Label(
        panel,
        text="Código:"
    ).pack()

    entrada_codigo = ttk.Entry(
        panel,
        width=40
    )
    entrada_codigo.pack(pady=5)

    # ----------------------------
    # Créditos
    # ----------------------------
    ttk.Label(
        panel,
        text="Créditos:"
    ).pack()

    entrada_creditos = ttk.Entry(
        panel,
        width=40
    )
    entrada_creditos.pack(pady=5)

    # ----------------------------
    # Función guardar
    # ----------------------------
    def guardar_asignatura():
        nombre = entrada_nombre.get()
        codigo = entrada_codigo.get()

        try:
            creditos = int(
                entrada_creditos.get()
            )
        except ValueError:
            messagebox.showerror(
                "Error",
                "Los créditos deben ser numéricos"
            )
            return

        resultado = insertar_asignatura(
            nombre,
            codigo,
            creditos
        )

        if resultado:
            messagebox.showinfo(
                "Éxito",
                "Asignatura registrada correctamente"
            )

            entrada_nombre.delete(0, "end")
            entrada_codigo.delete(0, "end")
            entrada_creditos.delete(0, "end")

        else:
            messagebox.showerror(
                "Error",
                "No se pudo registrar la asignatura"
            )

    # ----------------------------
    # Botón
    # ----------------------------
    ttk.Button(
        panel,
        text="Guardar asignatura",
        command=guardar_asignatura
    ).pack(pady=20)

from src.database.repositories import insertar_calificacion


def crear_panel_calificaciones(panel):
    """
    Crea el formulario para registrar calificaciones.

    Args:
        panel: Frame donde se dibuja el formulario.
    """

    # ----------------------------
    # Separador visual
    # ----------------------------
    ttk.Separator(
        panel,
        orient="horizontal"
    ).pack(fill="x", pady=20)

    # ----------------------------
    # Título
    # ----------------------------
    ttk.Label(
        panel,
        text="Registro de calificaciones",
        font=("Arial", 14)
    ).pack(pady=10)

    # ----------------------------
    # ID estudiante
    # ----------------------------
    ttk.Label(
        panel,
        text="ID del estudiante:"
    ).pack()

    entrada_estudiante = ttk.Entry(
        panel,
        width=40
    )
    entrada_estudiante.pack(pady=5)

    # ----------------------------
    # ID asignatura
    # ----------------------------
    ttk.Label(
        panel,
        text="ID de la asignatura:"
    ).pack()

    entrada_asignatura = ttk.Entry(
        panel,
        width=40
    )
    entrada_asignatura.pack(pady=5)

    # ----------------------------
    # Nota
    # ----------------------------
    ttk.Label(
        panel,
        text="Nota:"
    ).pack()

    entrada_nota = ttk.Entry(
        panel,
        width=40
    )
    entrada_nota.pack(pady=5)

    # ----------------------------
    # Función guardar
    # ----------------------------
    def guardar_calificacion():
        try:
            estudiante_id = int(
                entrada_estudiante.get()
            )

            asignatura_id = int(
                entrada_asignatura.get()
            )

            nota = float(
                entrada_nota.get()
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Los valores deben ser numéricos"
            )
            return

        resultado = insertar_calificacion(
            estudiante_id,
            asignatura_id,
            nota
        )

        if resultado:
            messagebox.showinfo(
                "Éxito",
                "Calificación registrada correctamente"
            )

            entrada_estudiante.delete(0, "end")
            entrada_asignatura.delete(0, "end")
            entrada_nota.delete(0, "end")

        else:
            messagebox.showerror(
                "Error",
                "No se pudo registrar la calificación"
            )

    # ----------------------------
    # Botón
    # ----------------------------
    ttk.Button(
        panel,
        text="Guardar calificación",
        command=guardar_calificacion
    ).pack(pady=20)