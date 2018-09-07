# Para crear una lista
lista = []

# podemos ver el tipo lista
print(type(lista))

# Podemos poblar nuestra lista desde el momento de la declaraci�n
lista = [10, 20 , 30]

print(lista)

# Adicionar al final de la lista
lista.append(40)

print(lista)

# Insertar en un indice de la lista
lista.insert(0, 30)

print(lista)

# En python los tipos de datos en una lista, tambien son dinamicos
lista = ['hoola', 10, 30.5, True]

print(lista)

# Puedo aceder a los elementos de una lista por sus indices
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# Saber si tengo algo en la lista
print(30.5 in lista)

print(lista)
lista.reverse()
print(lista)

lista = []
print(not lista)