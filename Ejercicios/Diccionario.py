Carlos = {'nombre': 'Carlos', 'apellido': 'Tena'}

Sharif = {} # Nombre y apellido agregado abajo
Sharif[ 'nombre']= 'Sharif'
Sharif ['apellido'] = 'Nasser'

print(Carlos['nombre']) #Solo imprimir nombre del diccionario
print()
print(Sharif) #Imprimir la variable Sharif (Que es diccionario)
print() # Espacio de separación

personas = [Carlos,Sharif]# Si es posible meter diccionarios en una lista, como aquí se ve
print(personas)
print()
print(personas[0])
print() 
print(personas[0]['nombre'])