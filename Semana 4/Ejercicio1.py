# Preguntar salario 1
salario_1 = float(input('Ingrese el salario 1: '))
# Preguntar tasa 1
tasa_1 = float(input('Ingrese la tasa de retefuente 1 '))
# Calcular salario neto 1
salario_neto_1 = salario_1 * (100 - tasa_1) / 100

# Preguntar salario 2
salario_2 = float(input('Ingrese el salario 2: '))
# Preguntar tasa 2
tasa_2 = float(input('Ingrese la tasa de retefuente 2 '))
# Calcular salario neto 2
salario_neto_2 = salario_2 * (100 - tasa_2) / 100

# Preguntar salario 3
salario_3 = float(input('Ingrese el salario 3: '))
# Preguntar tasa 1
tasa_3 = float(input('Ingrese la tasa de retefuente 3 '))
# Calcular salario neto 1
salario_neto_3 = salario_3 * (100 - tasa_3) / 100


# Calcular ingreso total
ingreso_neto_total = salario_neto_1 + salario_neto_2 + salario_neto_3

# Imprimir el resultado
print('El ingreso neto total es',ingreso_neto_total)