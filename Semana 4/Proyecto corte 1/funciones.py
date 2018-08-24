def calcular_precio_producto(coste_producto):
 '''
 (float) -> float

 Código para calcular el precio de un producto

 >>> calcular_precio_producto(100)
 150.0

 >>> calcular_precio_producto(200)
 300.0

 >>> calcular_precio_producto(500)
 750.0

 :param coste_producto: costo del producto
 :return: costo del producto màs el 50%
 '''

 return coste_producto + (coste_producto/2)

# calcular el coste del producto con la comisión ingresando el precio del producto
coste_producto = calcular_precio_producto(float(input('ingrese el precio de producto: ')))



# Imprimir el precio total con comisión
print('precio con comision:',coste_producto)

#

def calcular_precio_servicio(cantidad_horas):
 '''
 (float) -> float

 Código para calcular el valor de la hora de servicio

 >>> calcular_precio_servicio(2)
 200000

 >>> calcular_precio_servicio(45)
 4500000

 >>> calcular_precio_servicio(4)
 400000

 :param cantidad_horas: el numero de horas trabajado
 :return: el valor del servicio
 '''

 return cantidad_horas * 100000

# calcular el precio de servicio ingresando la cantidad de horas
cantidad_horas = calcular_precio_servicio(float(input('ingrese cantidad horas: ')))




# Imprimir el resultado del precio de servicio
print('precio de horas:',cantidad_horas)


def calcular_precio_servicio_extras(cantidad_horas_extra):
  '''
  (float) - > float

  Código para realizar el cálculo de las horas extra de un empleado

  >>> calcular_precio_servicio_extras(1)
  125000.0

  >>> calcular_precio_servicio_extras(4)
  500000.0

  >>> calcular_precio_servicio_extras(8)
  1000000.0

  :param cantidad_horas: cantidad de horas extras trabajadas
  :return: cantidad de la hora trabajada mas el 25%
  '''

  return cantidad_horas_extra * 125000.0

# calcular el precio de servicio de horas extra
cantidad_horas_extra = calcular_precio_servicio_extras(float(input('ingrese cantidad horas extra: ')))


# Imprimir el servicio de horas extra
print('precio de horas extra:',cantidad_horas_extra)

def calcular_costo_envio(kilometros):
  '''
  (float) -> float

  Código para calcular el costo del envio

  >>> calcular_costo_envio(3)
  345

  >>> calcular_costo_envio(5)
  575

  >>> calcular_costo_envio(10)
  1150

  :param kilometros: Cantidad de kilometros a cobrar por fuera
  :return: cantidad de kilometros * $115
  '''
  return kilometros * 115

# calcular el costo de envio con los kilometros
kilometros = calcular_costo_envio(float(input('ingrese kilometros recorrridos de envio: ')))




# Imprimir el salario total
print('precio de recargo por envio:',kilometros)


def calcular_precio_producto_fuera(coste_producto,kilometros):
  '''

  (float, float) -> float

#código para saber el precio del producto cuando es por fuera de la ciudad

  >>> calcular_precio_producto_fuera(100, 10)
  1300.0

  >>> calcular_precio_producto_fuera(200, 10)
  1450.0

  >>> calcular_precio_producto_fuera(400, 10)
  1750.0


  :param coste_producto: valor del producto
  :param kilometros: valor del envio
  :return: costo del valor del producto mas el valor del envío
  '''

  return calcular_precio_producto(coste_producto) + calcular_costo_envio(kilometros)



costo_total_mas_comision = (coste_producto+kilometros)

# Imprimir el salario total
print('costo total mas comision por envio:',costo_total_mas_comision)

def calcular_iva_producto(coste_producto,tasa):
  '''
  (float, float) -> float

  #Código para calcular el precio del producto mas iva

  >>> calcular_iva_producto(200, 0.19)
  357.0

  >>> calcular_iva_producto(100, 0.19)
  178.5

  >>> calcular_iva_producto(500, 0.19)
  892.5

  :param coste_producto: Valor costo del producto
  :param tasa: Valor del IVA
  :return: Valor costo del producto mas el iva
  '''

  return calcular_precio_producto(coste_producto) + (calcular_precio_producto(coste_producto) * tasa)

tasa = (float(input('ingrese tasa de iva: ')))

# Calcular iva producto
calcular_iva_producto = (coste_producto)+(coste_producto*(tasa))

# Imprimir el total con el iva
print('costo total mas iva:',calcular_iva_producto)

def calcular_iva_servicio(cantidad_horas, tasa):
  '''
  (float) - > float



  >>> calcular_iva_servicio(2,0.19)
  238000.0

  >>> calcular_iva_servicio(5,0.19)
  595000.0

  >>> calcular_iva_servicio(8,0.19)
  952000.0

  :param cantidad_horas: Cantidad de horas trabajadas
  :param tasa: valor del IVA
  :return: valor del precio del servicio mas el iva
  '''
  return calcular_precio_servicio(cantidad_horas)+(calcular_precio_servicio(cantidad_horas)*tasa)



# Calcular el iva del servicio
calcular_iva_servicio = (cantidad_horas)+(cantidad_horas*tasa)

# Imprimir el iva del servico
print('costo servicio mas iva:',calcular_iva_servicio)

def calcular_iva_envio(kilometros,tasa):
  '''
  (float) - > float

  #Codigo para calcular el costo del envio mas el iva

  >>> calcular_iva_envio(3,0.19)
  410.55

  >>> calcular_iva_envio(5, 0.19)
  684.25

  >>> calcular_iva_envio(10,0.19)
  1368.5

  :param kilometros: Cantidad de kilometros de envio
  :param tasa: valor del IVA
  :return: valor del envio mas el iva
  '''
  return calcular_costo_envio(kilometros) + (calcular_costo_envio(kilometros)*0.19)

# Calcular el iva con envio
calcular_iva_envio = (kilometros)+(kilometros*tasa)


# Imprimir el costo mas iva
print('costo envio mas iva:',calcular_iva_envio)


