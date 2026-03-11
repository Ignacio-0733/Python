#EJERCICIO 1
nombres=[]
numeros=[]
pulsa=int(input('1 Agregar,2 Eliminar,3 Buscar por nombre, 4 mostrar,5 para salir'))
while pulsa>0 and pulsa<5:
    if pulsa==1:
        nombre=input('Añade el nombre')
        num=int(input('Añade el numero'))
        nombres.append(nombre)
        numeros.append(num)
        pulsa=int(input('1 Agregar,2 Eliminar,3 Buscar por nombre, 4 mostrar'))
    if pulsa==2:
        nombre=input('Pon el nombre del que quieras eliminar')
        if nombre in nombres:
            posicion=nombres.index(nombre)
            nombres.pop(posicion)
            print('Eliminado')
            pulsa=int(input('1 Agregar,2 Eliminar,3 Buscar por nombre, 4 mostrar'))
    if pulsa==3:
        nombre=input('¿Que nombre quieres buscar?')
        if nombre in nombres:
            posicion=nombres.index(nombre)
            print('El numero de {nombre} es {numeros[posicion]}')
            pulsa=int(input('1 Agregar,2 Eliminar,3 Buscar por nombre, 4 mostrar'))
    if pulsa==4:
        print(nombres,'\n',numeros)
        pulsa=int(input('1 Agregar,2 Eliminar,3 Buscar por nombre, 4 mostrar'))
    if pulsa==5:
        quit
        
    
        
            
        
#EJERCICIO 2
notas=[]
print('Elige uno para añadir, elige dos para mostrar, elige tres para calcular el promedio, elige 4 mostrar la mas alta y la mas baja')
num=int(input('Elige la opcion1'))
while num>0 and num<6:
    if num==1:
        nota=float(input('Agrege nota'))
        notas.append(nota)
    if num==2:
        print(notas)
    if num==3:
        longitud=len(notas)
        media=sum(notas)/longitud
        print(media)
    num=int(input('Elige la opcion'))
    if num==4:
        print('Nota minima:',{min(notas)})
        print('Nota maxima:',{max(notas)})
#EJERCICO 3
print('La palabra es palindromo')
palabra=input('Introduce la palabra')
palindromo=list(palindromo)
pvuelta=list(palindromo)
pvuelta.reverse()
if pvuelta==palindromo:
    print('Es palindromo')
else:
    print('No es palindromo')
        

    
    
    
    
    



