dato = input('Ingrese dato: ')

lista = ['ana','jhon','julio','fernando','sandra']
if lista.count(dato) > 0:
    print('El dato existe:', dato)
else:
    print('el dato no existe : ',dato)

#CALCULADORA QUE SUMA# 

#primero = input('ingrese primer numero: ')

#segundo = input('ingrese segundo numero: ')

#primerNumero = int(primero)
#segundoNumero = int(segundo)
#print(primerNumero + segundoNumero)


#SOLO INGRESAR NUMEROS Y NO CARACTERES# 

#primero = input('ingrese primer numero: ')

#try:
   # primero = int(primero)
#except:
   # primero = 'soy el mejor'

#segundo = input('ingrese segundo numero: ')

#try:
   # segundo = int(segundo)
#except:
   # segundo = 'quiero ser desarrollador'

#if primero == 'soy el mejor' or segundo =='quiero ser desarrollador':
   # print('ingresaste mal un dato, por favor intente ingresar solo con numeros')
#else:
    #print(primero + segundo)

#VALIDACION CADA ENTRADA CON EXIT#


#primero = input('ingrese primer numero: ')

#try:
   # primero = int(primero)
#except:
    #primero = 'soy el mejor'

#if primero == 'soy el mejor':
   # print('el valor ingresado no es un entero')
   # exit()

#segundo = input('ingrese segundo numero: ')

#try:
   # segundo = int(segundo)
#except:
   # segundo = 'quiero ser desarrollador'

#if segundo == 'quiero ser desarrollador':
   # print('el valor ingresado no es un entero')
   # exit()

#print(primero + segundo)

#AGREGANDO OPERACIONES#

primero = input('ingrese primer numero: ')

try:
    primero = int(primero)
except:
    primero = 'soy el mejor'

if primero == 'soy el mejor':
    print('el valor ingresado no es un entero')
    exit()

segundo = input('ingrese segundo numero: ')

try:
    segundo = int(segundo)
except:
    segundo = 'quiero ser desarrollador'

if segundo == 'quiero ser desarrollador':
    print('el valor ingresado no es un entero')
    exit()

simbolo = input("ingrese operación: ")

if simbolo == '+':
    print('Suma:', primero + segundo)
elif simbolo == '-':
    print('resta', primero - segundo)
elif simbolo == '*':
    print('multiplicar', primero * segundo)
elif simbolo == '/':
    print('division', primero / segundo)
else:
    print('el simbolo ingresado no es valido')

