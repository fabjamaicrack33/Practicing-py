"""
i = 1

while i <= 11:
    print(i)
    i += 2  ##Donde i += 2 significa que el valor de i se incrementa en 2 cada vez que se ejecuta el ciclo repetitivo

print("Programa Finalizado")


#el programa solicita un número al usuario una y otra vez hasta que el usuario acierte.

i = 1

numero1=10

numero2 = int(input("Digite un número de 1 a 10: "))


while numero2 != numero1:
    i += 1
    numero2 = int(input("Digite un número de 1 a 10: "))

print ("Acertaste en el intento No.", i)

##Con esta modificación, el programa pedirá al usuario que ingrese un número nuevamente si está fuera del rango de 1 a 10, lo que hace que el programa sea más robusto.

i = 1
numero1 = 10
numero2 = int(input("Digite un número de 1 a 10: "))

while numero2 < 1 or numero2 > 10:
    print("El número debe estar dentro del rango de 1 a 10.")
    numero2 = int(input("Digite un número de 1 a 10: "))

while numero2 != numero1:
    i += 1
    numero2 = int(input("Digite un número de 1 a 10: "))

print("Acertaste en el intento No.", i)

##Ciclo while controlado por contador

print ("Uso del ciclo while con contador")

total, valor = 0, 1

while valor <= 12:
    print (valor)
    total = total + valor
    print ("el total parcial es ",total)
    valor = valor + 1

print ("El total final es ",total)

print( "fin del ciclo while")

##Ciclo while controlado por evento

#print ("Uso del ciclo while controlado por evento")

promedio, total, contador = 0, 0, 0

#print ("=== Software para parqueadero ===")

placa = input("Introduzca la placa del vehiculo (99 para salir): " )

while placa != "99": ##!= no sea igual o diferente al valor 
    valor= float(input("Digite valor del parqueadero: "))
    total = total + valor
    contador= contador+1
    placa = input("Introduzca la placa del vehiculo (99 para salir): " )
else:##es tambien valido sin el else 
   promedio = round(total / contador)

#print ("Promedio de vr. parqueadero por vehiculo: " + str(promedio))

#print ("Total dinero recaudado: ", round(total))

#print( "fin del ciclo while")

##Sentencias BREAK, CONTINUE y PASS

##Ejemplo setencia break While

print("Uso de la sentencia BREAK en while")

variable = 35

while variable > 1:
    variable = variable -5
    if variable == 10:
        break
    print ("Valor actual del caracter : " + str(variable))

print ("fin del ciclo")

#Ejemplo setencia CONTINUE

print("Uso de la sentencia CONTINUE en while")

variable = 35

while variable > 1:
    variable = variable -5
    if variable == 15:
        continue
    print ("Valor actual del caracter : " + str(variable))

print ("fin del ciclo")

#Ejemplo setencia PASS

print("Uso de la sentencia PASS en while")

variable = 35

while variable > 1:
    variable = variable -5
    if variable == 25:
        pass
    print ("Valor actual del caracter : " + str(variable))

print ("fin del ciclo")
"""


# TALLER 6 PYTHON
# AUTOR : FABIAN EDUARDO JAMAICA VARGAS
from datetime import date
hoy = date.today()
print('Hoy es el dia: ', hoy)
print()
print('TALLER 6 CICLOS ITERATIVOS CON LA SENTENCIA WHILE')
print()
num1= int(input('digite un numero: '))
print('***Ciclo controlado  por contador')
i = 1
while i <= num1:
    print(i)
    i += 1
print('Fin del ciclo')
print()
print('***Ciclo controlado por evento')
i=1
numero1=5
numero2= int(input('Digite un numero de 1 a 10:'))
while numero2 != numero1:
    i += 1
    numero2 = int(input('Digite un número de 1 a 10: '))
print('Acertaste en el intento No. ', i)
print('Fin del ciclo')

print()
print('Ciclo abortado con la sentencia break')
amistad=input('digite nombre de una amistad: ')
amistad= amistad.upper()
for character in amistad:
    print(character)
    if character =='A':
        break
print('fin del ciclo')
print()
print('FIN')    


