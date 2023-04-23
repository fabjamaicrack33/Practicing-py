#funciones en python 
#def frutas(fruta1, fruta2, fruta3):
  #print('las frutas rojas son:', fruta1, fruta2, fruta3)

#frutas('sandia', 'manzana ','cereza') 

#Imprimir una tupla
def frutas(*fruta):
  print('la fruta de color rojo es:', fruta[2])#para acceder una nomeclatura o elemento en tupla 
  
#frutas('sandia','manzana ','cereza'0)

#no hay orden para asignar el valor de los argumentos
def fruta_color(color,fruta):
  print(fruta,color)

#fruta_color(fruta='pera',color='verde')

#funcion con kwarg , especie de diccionario
def fruta_color2(**kwargs):
  print(kwargs['fruta'], kwargs['color'])

fruta_color2(fruta='banano',color='amarillo')





