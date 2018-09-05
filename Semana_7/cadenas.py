def contiene(palabra, texto):
    '''
    (str, str) -> bool

    Valida si una palabra esta en un texto

    >>> contiene('hola', 'hola mundo')
    True
    >>> contiene('jose', 'Hola mundo')
    False
    >>> contiene(10, '10')
    Traceback (most recent call last):
      File "/snap/pycharm-educational/9/helpers/pycharm/docrunner.py", line 140, in __run
        compileflags, 1), test.globs)
      File "<doctest contiene[2]>", line 1, in <module>
        contiene(10, '10')
      File "/home/alumno/PycharmProjects/ProgramacionG320182/Semana_7/cadenas.py", line 19, in contiene
        raise ValueError(str(palabra)+ ' No es una cadena')
    ValueError: 10 No es una cadena

    :param palabra:
    :param texto:
    :return:
    '''
    if type(palabra) != str:
        raise ValueError(str(palabra)+ ' No es una cadena')
    elif type(texto) != str:
        raise ValueError(str(texto)+ ' No es una cadena')
    return palabra in texto

def suma_si(cadena_1, cadena_2):
    '''
    (str, str) -> obj

    Si las dos cadenas son numeros se suman si no se concatenan

    >>> suma_si('10', '20')
    30.0
    >>> suma_si('hola', '10')
    'hola10'

    :param cadena_1:
    :param cadena_2:
    :return: la suma de las cadenas
    '''
    if cadena_1.isnumeric() and cadena_2.isnumeric():
        return float(cadena_1) + float(cadena_2)
    return cadena_1 + cadena_2


def eliminar_titulo(texto):
    """
    (str) -> str

    Elimina el titulo del texto

    >>> eliminar_titulo('hola un monton de texto')
    'hola un monton de texto'
    >>> eliminar_titulo('hola un monton de texto')
    'hola un monton de texto'

    :param texto: el texto a evaluar (min len 11)
    :return:
    """
    if texto[9] == '\n':
        return texto[10:]
    return texto

def es_palindromo(texto):
    """
    (str) -> bool
    Decide si un texto es palindromo

    >>> es_palindromo('anitalavalatina')
    True
    >>> es_palindromo('oso')
    True
    >>> es_palindromo('Jose')
    False

    :param texto:
    :return:
    """
    #return texto == ''.join(reversed(texto))
    return texto == texto[::-1]

