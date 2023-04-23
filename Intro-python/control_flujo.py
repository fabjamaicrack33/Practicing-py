#if 2 == 2:
   # print('2 es igual a 2')

#if 2 == 3:
    #print('2 es igual a 3')

#if 2 > 5:
   # print('2 es mayor a 5')

#if 5 > 2:
   # print('5 es mayor a 2')

#if 2 != 2:
   # print('2 es distinto a 2')

#if 3 != 2:
   # print('3 es distinto  a 2')

#if 3 >= 2:
   # print('3 es mayor o igual a 2')

#if 3 <= 3:
   # print('3 es menor o igual a 3')

if 2 > 5:
    print('2 es menor a 5 en if')
elif 2 > 5:
    print('2 es menor a 5 en elif')
elif 2 > 5:
    print('2 es menor a 5 en elif')
else: 
    print('yo me imprimo , si todo es falso')

print('it is true')if 5 < 2 else print('it is false')#unir en una sola linea es una operacion ternario

#and or
if 2 < 5 and 3 > 2: # and se cumple cuando ambas son trues
    print("ambas devuelve true")

if 2 < 5 and 3 < 2:
    print("hay una falsa, esto no se mostrará")

if 1 < 0 or 1 > 0: # Or se cumple cuando una es true 
    print('una de las dos condiciones devolvió true')

if 1 < 0 or 1 < 0:
    print('si ambas condiciones evaluan en false no se ejecuta esto')

