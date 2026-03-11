tarea=[]
num=int(input('Pulse 1 para añadir una tarea, 2 para eliminar una tarea, 3 para mostrar y 4 para salir'))
while num>0 and num<4:
    if num==1:
        nombre=input('Añade una tarea')
        tarea.append(nombre)
    if num==2:
        
        quitar=input('Pon el nombre del que quieras eliminar')
        tarea.remove(quitar)
            
    if num==3:
        print(tarea)

    num=int(input('Pulse 1 para añadir una tarea, 2 para eliminar una tarea, 3 para mostrar y 4 para salir'))
            
    
