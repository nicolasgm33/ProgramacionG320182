# Leer los dos numeros
numero_1 = input('Ingrese su primer número ')
numero_2 = input('Ingrese su segundo número ')

# Intentar convertirlos
try:
    numero_1 = float(numero_1)
    numero_2 = float(numero_2)

    # compararlos y decir cual es el mayor
    if numero_1 > numero_2:
        print(numero_1, 'es mayor que', numero_2)
    elif numero_1 == numero_2:
        print(numero_1, 'es igual que', numero_2)
    else:
        print(numero_2, 'es mayor que', numero_1)

# Manejamos nuestros errores
except ValueError:
    print(numero_1, 'y', numero_2,'No son números válidos')