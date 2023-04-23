# if 5 > 3:
  #  print('5 es mayor a tres')

x ="33 años"
y = "quiero ser desarrollador python"
#print(x, y)

email="pythondeveloperhappy@gmail.com"
#print(email)

a,b,c = "I want", " to be","a super python developer"
#print(a,b,c)

V1=V2=V3="I will get in there"
#print(V1,V2,V3)

inicio = "welcome "
final = "to your new job"
#print(inicio + final)


lista =['My name ','Is fabian','Welcome to my new job']
lista2 = lista.copy()#copiar la lista 
lista.append('I want to be') #añadir a la lista 
lista.append('A super python developer')
#lista.clear() #eliminar toda la lista ()
#print(lista.count(2),lista2.count(2)) # contando que numero se repite en la lista 
#print(lista,lista2)
#print(len(lista),len(lista2))#len le dice cuantas lista hay 

largolista = len(lista)
largolista2 = len(lista2)
#print(largolista , largolista2)

#print(lista[4])# 0 es la inicio y es acceder a los elementos de la lista

#lista.pop() # este elimina al ultimo elemento
#lista.remove('is fabian') #este elimina un elemento por su valor

lista.reverse()# lista a reves
lista.sort()# ordenar la lista 
#print(lista)

tupla = ('hola','mundo','somos','tupla')#tupla no se puede modificar ni agregar 
listadetupla = list(tupla) #se crea una lista para poder agregar o modificar la lista de elementos
listadetupla.append('im the best')
#print(listadetupla)


rango = range(6)
#print(rango)

diccionario = {
   'nombre': 'jako',
   'raza': 'cocker',
   'edad': 6 
   }
#print(diccionario)
#print(diccionario["nombre"])
#print(diccionario["raza"])
#print(diccionario.get('nombre'))#es otro metodo para entrar al elemento de la lista 
diccionario['nombre'] = ' zimba'
#print(diccionario)
#print(len(diccionario))

diccionario["Grande"] = 'no'#agrega un elemento mas de la lista
#print(diccionario)
#diccionario.pop('Grande') #elimina al ultimo elemento
#diccionario.popitem() #otra forma de eliminra
copiamascota = diccionario.copy()
#del diccionario['Grande'] # y otra forma de eliminar
diccionario.clear() #borra toda la lista 
#print(diccionario,copiamascota)

gatos = {  #anidados 
    "zimba": {
     "nombre": "zimba",
     "edad": 4
    },
    
    "marry": {
    "nombre": "marry",
    "edad": 3

    }
}
print(gatos)

perros = dict(nombre="jako",edad=6) #constructor dict
print(perros)