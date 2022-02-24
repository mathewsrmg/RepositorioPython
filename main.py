#Esto es un comentario de linea

'''
Cometario de bloque
'''

#Salida por consola
#print("Hola mundo Python")

#Variables o entradas
#nameUser = 'Marquitos'
#ageUser = 36
#heightUser = 1.72
#IsaGreenSupporter = True

#Salida de variables
'''
print(nameUser)
print('Buenos dias',nameUser)
print(f'Buenos dias {nameUser}')

print(f'Buenos dias señor: {nameUser} su edad es: {ageUser} su altura es: {heightUser} le gusta el verde?: {IsaGreenSupporter}' )
print(f'usted imprimio el numero {total}')
'''


#Recibiendo variables de consola
#numero1 = int (input('Digita un numero entero: '))
#numero2 = int (input('Digita un otro numero: '))
#total = numero1 + numero2
#print(f'el total es: {total}')
#print(f'{numero1} + {numero2} = {total}')


#Tomando decisiones
#numero = int (input("Por favor digita un numero : "))
#print(f'El numero digitado fue: {numero}')

#if(numero>=0):
#    print(f"El numero que digitaste es positivo")
#else:
#    print(f"El numero que digitaste es negativo")
#    print("oe... fuck you men")

#Hidroituango
'''
nivelAgua = int(input('Digite el nivel de agua ;) '))

if(nivelAgua<200):
    print(f"Hay muy poca agua en la represa")
elif(nivelAgua>=200 and nivelAgua<450):
    print(f"Hay buena cantidad de agua mi so")
else:
    print(f"Hay mucha agua ojo")
'''

#Calcular estacion segun
'''
mes = input('Digite el mes: ')

if(mes== "enero" or mes== "febrero" or mes== "marzo"):
    print(f"estamos en invierno")
elif(mes== "abril" or mes== "mayo" or mes== "junio"):
    print(f"estamos en verano")
elif(mes== "julio" or mes== "agosto" or mes== "septiembre"):
    print(f"estamos en otoño")
elif(mes== "octubre" or mes== "noviembre" or mes== "diciembre"):
    print(f"estamos en primavera")
else:
    print(f"uste que digito??")
'''

#While/for bucles, ciclos, loops, repeticiones
contador=0

while(contador<10):
    contador+=1
    print(contador)
else:
    print("termino el ciclo")

