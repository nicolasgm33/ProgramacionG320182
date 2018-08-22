# Dado los lados de un triangulo calcule el perimetro
def perimetro(lado_1, lado_2, lado_3):
    """
    (num, num, num) -> num

    Calcula el perimetro de un triangulo dados sus lados

    >>> perimetro(1, 2, 3)
    6

    >>> perimetro(2, 2, 2)
    6

    >>> perimetro(3, 3, 3)
    9

    :param lado_1:
    :param lado_2:
    :param lado_3:
    :return: num el perimetro del triangulo
    """
    return lado_1 + lado_2 + lado_3


def semiperimetro(lado_1, lado_2, lado_3):
    """
    (num, num, num) -> num

    Calcula el semiperimetro de un triangulo dados sus lados

    >>> semiperimetro(1, 2, 3)
    3.0

    >>> semiperimetro(2, 2, 2)
    3.0

    >>> semiperimetro(3, 3, 3)
    4.5

    :param lado_1:
    :param lado_2:
    :param lado_3:
    :return:
    """
    return perimetro(lado_1, lado_2, lado_3) / 2

def area(lado_1, lado_2, lado_3):
    """
    (num, num, num) -> num

    Calcula el area de un triangulo dados sus lados

    >>> area(2, 2, 2)
    1.7320508075688772

    >>> area(3, 3, 3)
    3.897114317029974

    >>> area(8, 15, 17)
    60.0


    :param lado_1:
    :param lado_2:
    :param lado_3:
    :return: el area del triangulo
    """
    # semiperimetro del trianulo
    s = semiperimetro(lado_1, lado_2, lado_3)
    area = s * (s - lado_1) * (s - lado_2) * (s - lado_3)
    return area ** (1/2)
