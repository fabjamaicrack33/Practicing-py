#EJEMPLO CICLO FOR PYTHON
"""
animales = ['leon','tigre','cocodrilo']
for animal in animales:
    print('El animal es : {0}, tamaño de palabra es:{1}'.format(animal,len(animal)))

#Formateo con nombres de parámetros:
nombre = 'Bob'
ocupacion = 'programador'
print('Hola, soy {nombre} y soy {ocupacion}.'.format(nombre=nombre, ocupacion=ocupacion))

#Utilizar f-strings para formatear cadenas de texto de manera más concisa  
#Uso de la estructura de control iterativa for en listas
nombre = 'Eduardo'
edad  = '34'
print(f'Hola, soy {nombre} y soy {edad}.')


##USO RANGE CICLO FOR 

for i in range (5): #Es posible indicar solo un valor final, en caso tal, el ciclo inicia en 0
    print(i)
print('Fin del ciclo')  


for i in range(2, 5):
    print(i, i ** 3)

print('fin del ciclo')


##range(valor_inicial, valor_final, incremento/decremento)
#Ejemplo

for i in range(20,0,-2):
    print(i)
print('Fin del ciclo')

#Uso del ciclo iterativo for en cadenas
#Ejemplo
for character in "hola mundo":
     print(character)
print("fin del ciclo")

 #Ejemplo estructura de control interativa for en listas

frutas = ['maracuya', 'cereza', 'manzana', 'pera', 'fresa']
for fruta in frutas:
    print(fruta,end =' ')
print('fin de mercado frutas')

#Ejemplo 2 con numeros 
numeros = [0, 1, 2, 3, 4, 5]
for numero in numeros:
  print (numero, end=" " )

print("fin del ciclo")

#Ciclo for en tuplas
conexion_bd = ("115.16.10.5","root","7890","clientes")

print("la tupla es: ")

for parametro in conexion_bd:
    print (parametro)

print ("fin del ciclo")


#Uso del bucle for en diccionarios
#Los nombres de las frutas son claves ,los colores de las frutas son los valores 
#.item() es el metodo para obtener una lista tupla que contienen tanto las claves como los valores del diccionario.

ensalada = {'Manzana':'verde','Patilla':'rosado','Banano':'amarillo','Papaya':'naranja'}
for nombre,color in ensalada.items(): 
     print(nombre, 'es de color', color)

print('fin del ciclo')

##Otra forma para el uso del diccionario 
##Se accede a los valores directamente usando ensalada[elemento], donde elemento es la clave en cada iteración del bucle. 
ensalada = {'Manzana':'verde', 'Patilla':'rosado', 'Banano':'amarillo', 'Papaya':'naranja'}
for elemento in ensalada:
 print (elemento, 'es de color', ensalada[elemento] )

print ("fin del ciclo")

#Sentencias BREAK, CONTINUE y PASS
##BREAK
print('Uso de la sentencia break')

for caracter in "PYTHON SENA":
   if caracter == "N":
      break

   print ("El caracter actual es : " +caracter)

print ('fin del ciclo')

##EJEMPLO CON SENTENCIA CONTINUE 

print("Uso de la sentencia continue")

variable = 15

for variable in range(variable, 1, -2):
    if variable == 9:
        continue
    print("Valor actual de la variable:", variable)

print("fin del ciclo")

##EJEMPLO CON SENTENCIA PASS

print("Uso de la sentencia pass")

for letra in "PYTHON SENA":
  if letra == "N":
     pass
  print ("El caracter actual es :" + letra)

print ("fin del ciclo")

#Estructura FOR - ELSE

db_connection = ("115.0.0.5", "7890", "root", "empleados")

for parametro in db_connection:
    print(parametro)
else:
    print('El comando PostgreSQL es: psql -h {server} -p {port} -U {user} -d {db_name}.'.format(
        server=db_connection[0], port=db_connection[1], user=db_connection[2], db_name=db_connection[3]))

"""


# TALLER 5 PYTHON
# AUTOR : FABIAN EDUARDO JAMAICA VARGAS
from datetime import date
hoy = date.today()
print('Hoy es el dia: ', hoy)
print()
print('TALLER 5 CICLOS ITERATIVOS CON LA SENTENCIA FOR')
print()

num1=int (input('digite el primer numero:'))
num2=int (input('digite el segundo numero (mayor):'))
print('ciclo para el primer numero')
for i in range(num1):
    print(i)
print('fin del ciclo')

print()
print('Ciclo desde el primero hasta el segundo numero con incremento de 2')
for i in range(num1,num2, 2):
    print(i)
print('Fin del ciclo')   

print()
empresa=input('digite nombre de una empresa: ')
empresa=empresa.lower()
for character in empresa :
    print(character)
print('Fin del ciclo')

print()
print('FIN')
