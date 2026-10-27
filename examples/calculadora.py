"""Ejemplo sencillo para practicar branches, PRs y conflictos."""


def sumar(a, b):
    """Suma validando que los argumentos sean numéricos."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("sumar requiere numeros")
    return a + b


def restar(a, b):
    return a - b


if __name__ == "__main__":
    print("2 + 3 =", sumar(2, 3))
    print("5 - 1 =", restar(5, 1))
