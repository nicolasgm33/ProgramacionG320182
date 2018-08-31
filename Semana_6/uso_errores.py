from Semana_6 import nuestros_errores as ne

try:
    ne.es_vocal('hola')
except:
    print('no puedo evaluar hola como una letra')

ne.es_vocal(87)