#funciones en python 
def frutas(fruta1, fruta2, fruta3):
  print('las frutas rojas son:', fruta1, fruta2, fruta3)

frutas('sandia', 'manzana ','cereza') 

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


##funcion con el return "devolver el valor"
#La función calcular_area_cuadrado(lado=5) está definida con un parámetro lado que tiene un valor predeterminado de 5. 
# Cuando llamas a la función con calcular_area_cuadrado(3), el valor de lado se establece en 3 (ignorando el valor predeterminado) y luego la función calcula el área del cuadrado con un lado de longitud 3.
#La llamada calcular_area_cuadrado(3) devolverá el resultado del cálculo, que es 3 * 3 = 9. Sin embargo, para ver el resultado impreso en la consola, deberías agregar una instrucción print:

def calcular_area_cuadrado(lado=5):
    return lado * lado

resultado = calcular_area_cuadrado()
print('El area cuadrado es', resultado)

# "número predeterminado"
#  se refiere a un valor numérico que se asigna automáticamente a una variable o parámetro si no se especifica un valor explícito.