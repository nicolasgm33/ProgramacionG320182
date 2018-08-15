def de_kelvin_a_centigrados(kelvin):
    """

    (float) -> float

    Convierte una cantidad dada en grados kelvin a grados centigrados

    >>> de_kelvin_a_centigrados(273.0)
    0.0

    >>> de_kelvin_a_centigrados(73.0)
    -200.0

    :param kelvin: (float) la cantidad de grados kelvin
    :return: (float) la cantidad en grados centigrados
    """
    return kelvin - 273

def de_dolares_a_pesos(dolares, trm):
    """
    (num, num) -> num
    Convierte una cantidad en dolares a otra cantidad en pesos dada la
    TRM

    >>> de_dolares_a_pesos(20, 3000)
    60000

    >>> de_dolares_a_pesos(0, 3000)
    0

    >>> de_dolares_a_pesos(100, 0)
    0

    >>> de_dolares_a_pesos(30, 1500)
    45000

    :param dolares: (num) La cantidad de dinero en dolares >= 0
    :param trm: (num) La tasa representativa del mercado >=0
    :return: (num) la cantidad en pesos
    """
    return dolares * trm