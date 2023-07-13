texto = 'Hello World'
#print(texto)


empleado = 'EDUARDO'
salario = '1.900.000'
#print ('El salario devengado por', empleado, 'es la suma de ', salario) 
#print("El salario devengado por", empleado, "\n es la suma de $", salario) #\n = salto de línea. ‘\n’ termina la línea y mueve el cursor a otra línea
#print("El salario devengado por \t", empleado, "\t es la \t suma de $", salario) #\t = es el carácter “tab horizontal" y se usa para simular sangrías de texto.

#Se utilizan los siguientes formatos para la salida de datos:
# %c = un caracter
# %s = str, cadena de caracteres
# %d = int, enteros
# %f = float, flotantes

titulo = "raíz cuadrada de tres"
valor = 3**0.5

PatPrimo = 'Palermo la Via'
S = 'S'

#print ("el resultado de %s es %f " % (titulo, valor))
#print ("Cliente: %s, ¿Activar S o N?: %c" % (PatPrimo, S))
#print ("Nro. factura: %d, Total a pagar: $ %f") % (567, 12500.83)

#Es posible controlar el formato de salida, por ejemplo, para obtener el valor con ocho (8) dígitos después del punto decimal, se digita %.8f; para una salida con 2 decimales se digita %.2f

titulo = "raíz cuadrada de tres"

valor = 3**0.5

#print ("el resultado de %s es %.8f " % (titulo, valor)) #salida con 8 decimales
#print ("el resultado de %s es %.1f " % (titulo, valor)) #salida con 1 decimal

print('Esta es la nota final del curso de VARIACIONES Y ESTRUCTURA DE CONTROL EN PYTHON ')

not1 = 4.2
not2 = 5.0
not3 = 4.5
not4 = 3.9
datos = [not1,not2,not3,not4]
prom = sum(datos)/len(datos)
nom = 'Fabian'
ape = 'Jamaica'

print('La nota 1 es de %.1f,la nota 2 es de %.1f,la nota 3 es de %.1f y la nota 4 es de %.1f' % (not1,not2,not3,not4))
print('La nota definitiva de' , nom , ape, 'es de %.1f' % (prom))


print('Si aprobaste ,felicitaciones y te deseamos muchos éxitos y Si no aprobaste ,puedes participar de nuevo a la proxima convocatoria del curso ')
print('Gracias')