opcion = "0"
while(opcion == 0):
  print(" ============opciones============")
  print("1) opcion 01")
  print("2) opcion 02")
  print("3) opcion 03")
  opcion = int(input("opcion elegida :"))
  print("ud selecciono la opcion " + str(opcion))
  salir = input("desea salir (si/no)")
  if (salir =="no"):
    opcion = 0
