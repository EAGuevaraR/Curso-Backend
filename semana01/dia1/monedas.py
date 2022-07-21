#PROGRAMA PARA CONVERTIR MONEDAS
#VERSION 1.0 - CONVERTIR SOLES A DOLARES
#INPUTS - ENTRADAS
montoOrigen = input("Ingrese monto: ")
#PROCESO
opcion = "0"
while(opcion == "0"):
  print("opcion1 - soles a dolares")
  print("opcion2 - dolares a soles")
  print("opcion3 - soles a euros")
  print("opcion4 - euros a soles")
  opcion = input("elija una opcion :")
  if(opcion == "1"):
    montoDolares = float(montoOrigen) / 3.80
    montoDolaresFormato = "$ {:,.2f}".format(montoDolares)
    #OUTPUTS - SALIDAS
    print("El monto en dolares es : " + str(montoDolaresFormato))
  elif(opcion == "2"):
    montoSoles = float(montoOrigen) * 3.80
    montoSolesFormato = "S/. {:,.2f}".format(montoSoles)
    #OUTPUT - SALIDA
    print("El monto en soles es : ",montoSolesFormato)
  elif(opcion == "3"):
    montoEuros = float(montoOrigen) / 4
    montoEurosFormato = "€. {:,.2f}".format(montoEuros)
    #OUTPUT - SALIDA
    print("El monto en Euros es : ",montoEurosFormato)
  elif(opcion == "4"):
    montoSoles = float(montoOrigen) * 4
    montoSolesFormato = "S/. {:,.2f}".format(montoSoles)
    #OUTPUT - SALIDA
    print("El monto en soles es : ",montoSolesFormato)
  else:
    print("Alerta!! debe seleccionar una opción valida")
    opcion = "0"
