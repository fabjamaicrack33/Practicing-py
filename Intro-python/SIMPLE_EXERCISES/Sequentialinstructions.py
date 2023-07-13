
#Constant 
IVA = 0.19   #Constant doesn't change its value, when it is a constant , always refers with capital letter 
precioinicial = 3000
preciofinal = precioinicial * (1.0+IVA)
#print('The final price is :', preciofinal)


#Functions of strings in Python

#Len() calcula la longitud en caracteres de una cadena 
#print('La longitud es:', len('hello world'))

#split() lo convierte en una lista 

cadena =('yo sé bien que soy el rey')

lista=cadena.split()
#print('tenemos lista', lista)


#lower() convierte una cadena en minuscula

sentence = 'BELIEVE YOU CAN AND YOU ARE HALFWAY THERE.'
sentence = sentence.lower()
#print(sentence)

#upper() convierte una cadena en mayuscula 

quote = 'Do not wait for opportunity. Create it.'
quote = quote.upper()
#print('CAPITAL LETTER:' , quote)



#replace() Reemplaza una cadena por otra 

f = 'yo soy un principe'
#print(f.replace('principe','rey'))


#Functions of numbers in Python

#range() Crear un rango de números

m = range(10)
#print(list(m))

#str() de valor numerico a texto
number = 10.2
#print(str(number))

#int() convierte a valor entero
num2 = '45'
print(int(num2))

#float() convierte a un valor decimal 

num3 = 90
print(float(num3))

#max() determina el maximo entre un grupo de numeros

a = [2,3,4,5,8]
print(max(a))

#min() determina el minimo entre un grupo de números

w = [10,32,24,15,80]
print(min(w))

#sum() suma el total de una lista de números

k = [2,3,5,8,1,5,10]
#print(sum(k))

#round() redondea despues de la coma de un float
#print(round(77.62))

#Bonus Track , calcular el promedio
datos = [1, 2, 3, 4, 5]  # Ejemplo de una lista de datos
promedio = sum(datos) / len(datos)
#print("El promedio es:", promedio)
