dias = ("lunes", "martes","miercoles","jueves","viernes")
#la tupla es inmutable, no funcionan el pop ni el append, l diferencia es que se pone con parentesis no como la lista que es con corchetes
#pero se puede convertir en una lista y viceversa

dias = list(dias)
dias.append("sabado")
print(dias)
dias = tuple(dias)
print(dias)


