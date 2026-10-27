"""Ejemplo sencillo para practicar branches, PRs y conflictos."""


def sumar(a, b):
    """Suma dos numeros e imprime el resultado para depuracion."""
    resultado = a + b
    print(f"sumar({a}, {b}) = {resultado}")
    return resultado


def restar(a, b):
    return a - b


if __name__ == "__main__":
    print("2 + 3 =", sumar(2, 3))
    print("5 - 1 =", restar(5, 1))
