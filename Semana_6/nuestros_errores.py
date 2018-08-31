def es_vocal(letra):
    """
    (str) -> bool

    Decide si una letra es vocal

    >>> es_vocal('a')
    True
    >>> es_vocal('b')
    False
    >>> es_vocal('hola')
    ValueError: hola no es una letra
    >>> es_vocal(30)
    ValueError: 30 no es una letra


    :param letra: la letra a evaluar
    :return: True si es vocal False de lo contrario
    """
    if type(letra) == str:
        if len(letra) == 1:
            return letra in 'aeiouAEIOU'
        else:
            raise ValueError(letra + ' no es una letra')
    else:
        raise ValueError(str(letra)+ ' no es una letra')