from Semana_5 import triangulos

# Leemos los lados del triangulo
lado_1 = float(input('Ingrese su lado 1 '))
lado_2 = float(input('Ingrese su lado 2 '))
lado_3 = float(input('Ingrese su lado 3 '))

# Calculamos las magnitudes
perimetro = triangulos.perimetro(lado_1, lado_2, lado_3)
semiperimetro = triangulos.semiperimetro(lado_1, lado_2, lado_3)
area = triangulos.area(lado_1, lado_2, lado_3)

# Imprimimos los resultados
print('El perimetro de su triangulo es',perimetro)
print('El semiperimetro de su triangulo es', semiperimetro)
print('El área de su triangulo es', area)
