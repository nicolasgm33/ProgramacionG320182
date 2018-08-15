# Definir una funcion calcular salario neto
def obtener_salario_neto(salario, tasa):
    '''
    Calcula el salario neto descontando la retención en la fuente

    >>> obtener_salario_neto(100, 2)
    98.0

    >>> obtener_salario_neto(200, 10)
    180.0

    >>> obtener_salario_neto(200, 0)
    200.0

    :param salario: (num) El salario del empleado
    :param tasa: (num) la tasa de retefuente (entre 0 y 100)
    :return: (num) el salario neto del empleado
    '''
    salario_neto = salario * (100 - tasa) / 100
    return salario_neto

# LLamar la función 3 veces
salario_neto_1 = obtener_salario_neto(float(input('digite su salario ')),
                                      float(input('digite su Tasa ')))
salario_neto_2 = obtener_salario_neto(float(input('digite su salario ')),
                                      float(input('digite su Tasa ')))
salario_neto_3 = obtener_salario_neto(float(input('digite su salario ')),
                                      float(input('digite su Tasa ')))


# Calcular el salario neto total
salario_total = salario_neto_1 + salario_neto_2 + salario_neto_3

# Imprimir el salario total
print('El total de ingresos es',salario_total)