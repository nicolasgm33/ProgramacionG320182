def dividir(dividendo, divisor):
    """
    (num, num) -> float

    Calcula la división entre dos números

    >>> dividir(10, 5)
    2.0
    >>> dividir(1, 0)
    'no puedo dividir entre 0'

    :param dividendo: el dividendo de la operación
    :param divisor: el divisor de la operación diferente de 0
    :return: el resultado calculado o 'no puedo dividir entre 0'
    si se presenta un error
    """
    try:
        return dividendo / divisor
    except ZeroDivisionError:
        return 'no puedo dividir entre 0'


def dividir_ver_if(dividendo, divisor):
    """
    (num, num) -> float

    Calcula la división entre dos números

    >>> dividir_ver_if(10, 5)
    2.0
    >>> dividir_ver_if(1, 0)
    'no puedo dividir entre 0'

    :param dividendo: el dividendo de la operación
    :param divisor: el divisor de la operación diferente de 0
    :return: el resultado calculado o 'no puedo dividir entre 0'
    si se presenta un error
    """
    if divisor == 0:
        return 'no puedo dividir entre 0'
    return dividendo / divisor
