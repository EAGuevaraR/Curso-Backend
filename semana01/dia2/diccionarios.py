#similar a json
from msilib.schema import tables


capitales = {
  'Perú':'Lima',
  'Ecuador':'Quito',
  'Chile':'Santiago',
  'Uruguay':'Montevideo',
}
print(capitales)

#COn update agrego elementos al diccionario
nuevaCapital = {'Brasil':'Brasilia'}
capitales.update(nuevaCapital)
print(capitales)

#con pop puedo eliminar un elemento del diccionario
capitales.pop('Chile')
print(capitales)

#tambien puedo eliminar un elemento del diccionario, pero almacenarlo en una variable y además 
# si el elemento a eliminar no existe, decirle que me bote un mensaje
c = capitales.pop('Venezuela', 'no existe ese valor en el diccionario')
print (c)
print(capitales)

### RECORRER DICCIONARIOS
for capital in capitales:
  print(capital + " : " + capitales[capital])
print(capitales.keys())
print(capitales.values())
print(capitales.items())

for clave in capitales.keys():
  print(clave +"=>" + capitales[clave])


##### BASE DE DATOS DE ALUMNOS #####
alumno1 = {
  'Nombre':'César Mayta',
  'Edad':39,
  'Nota':19.5,
  'Aprobado':True,
  'Cursos':['JS','Python','C#']
}
alumno2 = {
  'Nombre':'Lucía Torres',
  'Edad':29,
  'Nota':20,
  'Aprobado':True,
  'Cursos':['Java','Swift','Kotlin']
}
alumnos = [alumno1, alumno2]
print("*" * 100)
for columna in alumno1:
  print(columna,end = '            |')
print()
print("*" * 100)
for alumno in alumnos:
  for clave,valor in alumno.items():
    print(valor,end = '        |      ')
  print()



