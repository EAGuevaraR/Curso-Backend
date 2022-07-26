dias = ["lunes","martes","miercoles"]
print (dias)
#pop elimina el último valor de la lista
dias.pop()
print(dias)
# append agrega un valor a la lista
dias.append("miercoles")
print(dias)
dias[0] = "domingo"
print(dias)

for dia in dias:
  print("hoy es " + dia)
