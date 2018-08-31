"""
Diseña un programa que lea la edad de dos personas y diga
quién es más joven, la primera o la segunda.
Ten en cuenta que ambas pueden tener la misma edad.
En tal caso, hazlo saber con un mensaje adecuado.
"""
def persona_mas_joven(persona_1, edad_1,
                      persona_2, edad_2):
    """
    (str, int, str, int) -> str

    Determina quien de los dos es mas joven

    >>> persona_mas_joven('Hugo', 10, 'Paco', 15)
    'Hugo es mas joven que Paco'
    >>> persona_mas_joven('Hugo', 10, 'Paco', 10)
    'Hugo y Paco tienen la misma edad'
    >>> persona_mas_joven('Hugo', 10, 'Paco', 8)
    'Paco es mas joven que Hugo'

    :param persona_1: El nombre de la primera persona
    :param edad_1: La edad de la primera persona
    :param persona_2: El nombre de la segunda persona
    :param edad_2: La edad de la segunda persona
    :return: mensaje indicando quien es el mas joven
    """
    if edad_1 > edad_2:
        return persona_2+' es mas joven que '+persona_1
    elif edad_1 == edad_2:
        return persona_1 + ' y ' + persona_2 + ' tienen la misma edad'
    return persona_1 + ' es mas joven que ' + persona_2
