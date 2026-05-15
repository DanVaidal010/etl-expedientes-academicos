from src.services.validators import (
    validar_nombre,
    validar_email,
    validar_nota
)


def test_validar_nombre():
    assert validar_nombre("Dan") is True
    assert validar_nombre("") is False


def test_validar_email():
    assert validar_email("test@email.com") is True
    assert validar_email("correo_mal") is False


def test_validar_nota():
    assert validar_nota(5) is True
    assert validar_nota(11) is False