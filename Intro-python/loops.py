i = 0 #inicializar

while i < 5:
    #print(i)
    i = i + 1 #otra alternativa es i += 1

#while continue#
i = 0

while i < 5:
  i += 1
  if i == 3:
    continue
  #print(i)


#while break#

i = 0
while i < 5:
  #print(i)
  if i == 3:
    break 
  i += 1

#for lopps es crear lista e interatuar los elementos 
#Usuarios = ['Luis', 'Maria', 'Nicolas', 'Fernanda' , 'Carlos' ]   
#for Usuario in Usuarios:
 # print(Usuario)

#acceder los caracteres en un string 
#usuario = 'Maria'
#for c in usuario :
 # print(c) 

 #con break and continue en una lista

Usuarios = ['Luis', 'Maria', 'Nicolas', 'Fernanda' , 'Carlos' ]   
for Usuario in Usuarios:
  if Usuario == 'Nicolas':
    break
  #print(Usuario)

Usuarios = ['Luis', 'Maria', 'Nicolas', 'Fernanda' , 'Carlos' ]   
for Usuario in Usuarios:
  if Usuario == 'Nicolas':
    continue
  print(Usuario)

#range 
for x in range(4,100,6):
  print(x)

#interatuar dos listas 
Usuarios = ['Luis', 'Maria', 'Nicolas', 'Fernanda' , 'Carlos' ]

edades = [32,30,31,25,28]

for usuario in Usuarios:
  for edad in edades :
    print(usuario,edad)




