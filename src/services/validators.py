"""
Módulo de validación de datos.

Contiene funciones para validar la información
antes de insertarla en la base de datos.
"""

import re


def validar_nombre(nombre):
    """
    Valida que el nombre no esté vacío.

    Args:
        nombre (str): Nombre del estudiante.

    Returns:
        bool: True si es válido, False si no.
    """

    if not nombre or not nombre.strip():
        return False

    return True


def validar_email(email):
    """
    Valida que el email tenga un formato correcto.

    Args:
        email (str): Email del estudiante.

    Returns:
        bool: True si es válido, False si no.
    """

    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if re.match(patron, email):
        return True

    return False

def validar_codigo_asignatura(codigo):
    """
    Valida que el código de asignatura no esté vacío.

    Args:
        codigo (str): Código de la asignatura.

    Returns:
        bool: True si es válido, False si no.
    """

    if not codigo or not codigo.strip():
        return False

    return True


def validar_creditos(creditos):
    """
    Valida que los créditos sean mayores que 0.

    Args:
        creditos (int): Créditos de la asignatura.

    Returns:
        bool: True si es válido, False si no.
    """

    if isinstance(creditos, int) and creditos > 0:
        return True

    return False

def validar_nota(nota):
    """
    Valida que la nota esté entre 0 y 10.

    Args:
        nota (float): Nota del estudiante.

    Returns:
        bool: True si es válida, False si no.
    """

    if isinstance(nota, (int, float)) and 0 <= nota <= 10:
        return True

    return False