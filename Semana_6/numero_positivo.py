# Creemos una función que nos de un mensaje si un numero es positivo

def es_positivo(num):
    """
    (num) -> str

    Crea un mensaje si el numero es positivo

    >>> es_positivo(7)
    'el numero es positivo'
    >>> es_positivo(-10)
    'el numero es negativo'
    >>> es_positivo(0)
    'el numero es positivo'
    >>> es_positivo(7.89)
    'el numero es positivo'
    >>> es_positivo(-96852.2412)
    'el numero es negativo'

    :param num: el numero a evaluar
    :return: (str) mensaje resultante de la evaluación
    """
    if num >= 0:
        return 'el numero es positivo'
    return 'el numero es negativo'