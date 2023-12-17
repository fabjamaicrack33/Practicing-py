#Iterar significa repertir una accion o conjunto de acciones en un bucle hasta que se cumple una condicion determinada 
print('## Bucle while ##')
lista=[5,4,1,2,8]
i=0
while i<len(lista):
    elemento=lista[i]
    print(elemento)
    i+=1

print('## Bucle for ##')
lis=[3,6,9,0,7]
for elemento in lis:   ## Un bucle FOR se utiliza para iterar sobre una secuencia de elementos. IN  es una palabra clave que se utiliza para especificar la secuencia sobre la cual se realizará la iteración.
    print(elemento)    ## ELEMENTO es una variable que se utiliza para representar cada elemento de la secuencia en cada iteración del bucle.

print('## iterar una cadena o string con For ##')
Myname = 'Fabian'
for name in Myname:
 print(name)

print('## interar una cadena o string con while ##')

Mysurname = 'Vargas'
i=0
while i<len(Mysurname):
   surname=Mysurname[i]
   print(surname)
   i+=1

print('## funcion enumerate() ##')

Myname = 'Fabian'
for name in enumerate(Myname): ## funcion enumarate() esta funcion agrega indice a cada caracter de una cadena
 print(name)


print('# para verificar si es interable o no con isinstance #')

from collections.abc import Iterable
Nombre = 'Fabian'
num = 76

print(isinstance(Nombre,Iterable))
print(isinstance(num,Iterable))


print('## Metodos ##')

print('# metodo LIST #')

print(list('Eduardo'))

print('# metodo SUM #')

print(sum([1,2,9,3]))

print('# metodo JOIN #')

print(','.join('Jamaica'))

print('Iterar con dictionario')
dictionary={'a':'I','b':'You','c':'We'}
for d in dictionary:
   print(d)
