#cuadrado con asteriscos usando for

lado = int(input("ingresa el lado del cuadrado : "))

for contador in range (1,lado+1):
  if(contador==1 or contador== lado):
    print ("* " * lado)
  else:
    print("* " + "  " * (lado-2) + "*")
 
