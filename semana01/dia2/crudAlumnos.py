import tabulate
#PROGRAMA PARA CREAR UN 
# CRUD
# CREATE
# READ
# UPDATE
# DELETE

from faulthandler import cancel_dump_traceback_later


print("-"*49)
print("|" + " "* 9 + "MATRÍCULA DE ALUMNOS EN CODIGO" + " " * 8 + "|")
print("-" * 49)
print("|" + " "* 9 + "MENU DE OPCIONES      " + " " * 16 + "|")
print("|" + " "* 9 + "[1] REGISTRAR ALUMNO  " + " " * 16 + "|")
print("|" + " "* 9 + "[2] MOSTRAR ALUMNO    " + " " * 16 + "|")
print("|" + " "* 9 + "[3] ACTUALIZAR ALUMNO " + " " * 16 + "|")
print("|" + " "* 9 + "[4] ELIMINAR ALUMNO   " + " " * 16 + "|")
print("|" + " "* 9 + "[5] SALIR             " + " " * 16 + "|")
print("-" * 49)
opcion = 0
alumnos =[{'nombre':'cesar mayta','email':'cesarmayta@gmail.com','celular':'45654654'}]
while(opcion!=5):
  opcion = int(input("INGRESE OPCION DEL MENU: "))
  if(opcion == 1):
    print("NUEVO ALUMNO")
    nombre = input ("NOMBRE : ")
    email = input ("EMAIL : ")
    celular = input ("CELULAR : ")
    dictAlumno = {
      'nombre': nombre,
      'email': email,
      'celular':celular
    }
    alumnos.append(dictAlumno)
    print("ALUMNOS REGISTRADO CON EXITO!!!")
  elif(opcion == 2):
    print("RELACION DE ALUMNOS")
    cabeceras = alumnos[0].keys()
    registros = [x.values() for x in alumnos]
    print(tabulate.tabulate(registros,cabeceras))
  elif(opcion == 3):
    print("ACTULALIZAR ALUMNO")
  elif(opcion == 4):
    print("ELIMINAR DE ALUMNOS")
  elif(opcion == 5):
    print("FINALIZANDO PROGRAMA")  
  else:
    print("OPCION INCORRECTA")


