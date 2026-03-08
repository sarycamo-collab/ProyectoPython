# Autor: Sariabeth Camarena
# Fecha: 08/03/2026
# Versión: 1.0

# Módulo de operaciones matemáticas básicas.
def suma(a, b):
    return a + b # Devuelve la suma de dos números

def resta(a, b):
    return a - b # Devuelve la resta de dos números

def multiplicacion(a, b):
    return a * b # Devuelve la multiplicación de dos números

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b # Devuelve la división de dos números