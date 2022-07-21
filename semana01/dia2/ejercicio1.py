#crear un cuadrado con *
#entrada
lado = int(input("Ingrese el lado del cuadrado : "))
#proceso
total = lado + 1
for contador in range (1, total,1):
  if(contador == 1 or contador == lado):
    print('* ' * lado)
  else:
    print('* ' + '  ' * (lado-2) + '*')

#salida
