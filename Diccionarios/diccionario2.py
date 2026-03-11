alumnos = {}
for i in range(3):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    nota = float(input("Nota: "))
    alumnos[nombre] = {"edad": edad, "nota": nota}
print("\n-Alumnos-")
for nombre, datos in alumnos.items():
    print("Nombre: {}, Edad: {}, Nota: {}".format(nombre, datos["edad"], datos["nota"]))
notas = [datos["nota"] for datos in alumnos.values()]
suma = 0
for datos in alumnos.values():
    suma += datos["nota"]
nota_media = suma / len(alumnos)
print('Nota media de la clase: ',nota_media) 
mejor_alumno = max(alumnos, key=lambda x: alumnos[x]["nota"])
print("Alumno con la nota más alta:", mejor_alumno)

