""""
curso1="Requerimientos"

curso2="Algoritmos"

print("El curso1 es: ", curso1)

print("El curso2 es: ", curso2)

if curso1 == "Requerimientos":
    if curso2 == "Algoritmos":
        print ("Usted estudia Programación de Software")

    else:
        print ("Usted estudia otro programa diferente a Programación de Software")

print ("***** Final del Análisis del Programa de Formación SENA *****")



###EJERCICIOS CON ELIF (ELSE-IF)

voto= int(input(" \n digite su número de candidato (1=X 2=Y 3=Z) "))

if voto==1 :
    print (" \n su voto es para el candidato X " )

elif voto==2 :
    print (" \n su voto es para el candidato Y " )

elif voto==3 :
    print (" \n su voto es para el candidato Z " )

else:
    print ("su voto es inválido.")

print (" \n Ya ha depositado su voto, puede solicitar su documento y salir. Gracias")


##EXPRESIONES BOOLEANAS COMPUESTAS

a= int(input("Digita el primer numero entero "))

b= int(input("Digita el segundo numero entero "))

c= int(input("Digita el tercer numero entero "))

if a < b and a < c:
    print ("El menor numero entero es ", a)

elif b < c:
    print ("El menor numero entero es ", b)

else:
    print ("El menor numero entero es ", c)

print (" ******* END *************")

"""



#TALLER 4 PYTHON
#AUTOR : FABIAN JAMAICA
#FECHA : 16/07/2023
print()
from datetime import date
hoy = date.today()
print('Hoy es el dia', hoy)
print('TALLER CONDICIONALES ANIDADAS')
print()
print('EJERCICIO DE LAS CLASES DE TRIANGULOS')
a = int(input('Digite el valor de A: '))
b = int(input('Digite el valor de B: '))
c = int(input('Digite el valor de C: '))

if a==b and a==c and b==c:
    print('EL TRIANGULO ES EQUILATERO')
else:
    if a==b or b==c or a==c:
        print('EL TRIANGULO ES ISOCELES')
    else:
        print('EL TRIANGULO ES ESCALENO')
print()
animal = input('digite un animal: ')
animal = animal.upper()
if animal == 'PERRO':print('Este animal es el mejor amigo del hombre:',animal)
elif animal == 'GATO':
    print('Este animal persigue a los ratones: ',animal)
elif animal == 'OSO':
    print('Este animal vive en el bosque: ',animal)
else:
    print('No es PERRO, no es GATO ni tampoco es OSO...es:',animal)
print()
print('Fin taller condicionales anidadas')

