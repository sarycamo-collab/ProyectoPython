# Autor: Sariabeth Camarena
# Fecha: 08/03/2026
# Versión: 1.0

# Módulo de operaciones matemáticas básicas.
def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b


def resta(a, b):
    """Devuelve la resta de dos números."""
    return a - b


def multiplicacion(a, b):
    """Devuelve la multiplicación de dos números."""
    return a * b


def division(a, b):
    """Devuelve la división de dos números."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b