#EJERCICIO 1
diccionario={}
usuario=input('Pon un usuario o no para salir')
while usuario!="no":
    telefono=input('Pon un telefono')
    diccionario[usuario]=telefono
    usuario=input('Pon un usuario o no para salir')
print (diccionario)

#EJERCICIO 2
numeros=[]
for cont in range (10):
    posicion=float(input('Pon numeros'))
    numeros.append(posicion)
    
print(numeros)
print('La media es: ',sum(numeros)/len(numeros))
print('La suma es: ',sum(numeros))
    
    
    
