def suma_cruzada(lista_1, lista_2):
    """
    (list of num, list of num) -> list of num

    Suma de forma cruzada los elementos de una lista

    >>> suma_cruzada([1, 2, 3 ,4], [4, 3, 2, 1])
    [2, 4, 6, 8]
    >>> suma_cruzada([1, 1, 1 ,1], [1, 1, 1, 1])
    [2, 2, 2, 2]


    :param lista_1: lista de 4 numeros
    :param lista_2: lista de 4 numeros
    :return: lista con la suma cruzada de numeros
    """
    lista_resultante = []
    lista_resultante.append(lista_1[0] + lista_2[-1])
    lista_resultante.append(lista_1[1] + lista_2[-2])
    lista_resultante.append(lista_1[2] + lista_2[-3])
    lista_resultante.append(lista_1[3] + lista_2[-4])
    return lista_resultante


def primero_mayor(lista):
    """
    (list) -> bool

    Define si el primer elemento de la lista es mayor que el ultimo

    >>> primero_mayor([1, 2, 3])
    False
    >>> primero_mayor([5, 2, 3])
    True
    >>> primero_mayor([1])
    False
    >>> primero_mayor([])
    False

    :param lista:
    :return:
    """
    if lista:
        return lista[0] > lista[-1]
    return False


def producto_escalar(numero, lista):
    """
    (num, list) -> list

    Realiza el producto sobre una lista de 4 elementos

    >>> producto_escalar(3, [10, 'Hola', 15.0, 'mundo'])
    [30, 'HolaHolaHola', 45.0, 'mundomundomundo']

    :param numero:
    :param lista:
    :return:
    """
    return [numero * lista[0], numero * lista[1], numero * lista[2], numero * lista[3]]

def producto_punto(lista_1, lista_2):
    """

    >>> producto_punto([1,2,3,4],[1,2,3,4])
    30

    :param lista_1:
    :param lista_2:
    :return:
    """
    resultado = lista_1[0] * lista_2[0]
    resultado += lista_1[1] * lista_2[1]
    resultado += lista_1[2] * lista_2[2]
    resultado += lista_1[3] * lista_2[3]
    return resultado