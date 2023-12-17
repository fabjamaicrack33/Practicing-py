def suma(num1,num2):
  return num1 + num2
def resta(num1,num2):
  return num1 - num2
def multiplicar(num1,num2):
  return num1 * num2
def division(num1,num2):
  return num1 / num2

print('######### Bienvenid@ a la Calculadora #########')
dato = int(input('Por favor digite una de las siguintes opciones 1)SUMA  2)RESTA  3)MULTIPLICAR  4)DIVISION:  '))

if dato == 1:
 num1 = int(input('ingrese el primer valor: '))
 num2 = int(input('ingrese el segundo valor: '))
 resultado = suma(num1,num2)
 print('La suma es',resultado,'Gracias por participar')

elif dato == 2:
 num1 = int(input('ingrese el primer valor: '))
 num2 = int(input('ingrese el segundo valor: '))
 resultado = resta(num1,num2)
 print('La resta es', resultado, 'Gracias por participar')

elif dato == 3:
 num1 = int(input('ingrese el primer valor: '))
 num2 = int(input('ingrese el segundo valor: '))
 resultado = multiplicar(num1,num2)
 print('La multiplocacion es', resultado, 'Gracias por participar')

elif dato == 4:
 num1 = int(input('ingrese el primer valor: '))
 num2 = int(input('ingrese el segundo valor: '))
 resultado = division(num1,num2)
 print('La division es', resultado, 'Gracias por participar')

else:
 print('Numero equivocado , Por favor vuelva a marcar')
