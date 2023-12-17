"""
print("----Uso de IF-------")

numero = -2

if numero < 0:
    print("El número ingresado es negativo:", numero, "\n")
    print("El número será cambiado a cero.\n")
    numero = 0

print("El número ingresado ahora es", numero, "\n")


print("----Uso de IF-ELSE-------")
x = 7

if x % 2 == 0:
    print(x, "el número secreto es par")
else:
    print(x, "el número secreto es impar")

print("-------------------------")
print("Hemos terminado la verificación para este número")



edad = int(input("¿Cuántos años tiene? "))

if edad < 99:
    pass

else:
  print("¡No creo que usted tenga esa edad!")
  print(f"Usted dice que tiene {edad} años.")

"""

#TALLER 3 PYTHON
#AUTOR : FABIAN JAMAICA
#FECHA : 16/07/2023
print()
from datetime import date
hoy = date.today()
print('Hoy es el dia', hoy)
print('TALLER CONDICIONALES SIMPLES')
print()
a=int(input('digite el valor de A: '))
b=int(input('digite el valor de B: '))

if a>=b:
    print('A es mayor o igual a B')
else:
    print('A es menor que B')

print()
curso1 = 'Requerimientos'
curso2 = 'Algoritmos'

print('El curso es: ' , curso1)
print('El curso es: ' , curso2)
if curso1 == 'Requerimientos' and curso2 =='Algoritmos':
    print('usted estudia programacion de Software')
else:
    print('usted estudia otro programa diferente a programacion de sofware')
print()
print('*** Final del analisis del programa de Formación SENA ***')
print()
frase=input('digite una oracion: ')
print('la frase en mayuscula es : ' , frase.upper())
longitud=len(frase)
print('la longitud de la frase es: ', len(frase), 'caracteres')
if longitud > 10:
    print ('La frase contiene mas de 10 caracteres')
else:
    print('La frase contiene menos de 11 caracteres')
print()
print('Fin del taller Condicionales Simples ')
 
