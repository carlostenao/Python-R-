nombres=['Sharif', 'Carlos']
print(nombres)
nombres.append('Maria')
print(nombres)

nombres.sort()
print(nombres)


un_nombre = nombres[1]
print(un_nombre)

dos_nombres= nombres[0:2] # Aquí no se toma en cuenta el valor dos
print(dos_nombres)

dos_nombres1= nombres[1:3] # Aquí no se toma en cuenta el valor 1 ni 3
print(dos_nombres1)

if 'Sharif' in nombres:  #NO OLVIDAR NUNCA ":"
    print('Si esta en la lista')
else:
    print('No está en la lista')

if 'Jim' in nombres: #El IN se ocupa para saber si se encuentra dentro de la lista "X"
    print('Si esta en la lista')
else:
    print('No está en la lista')