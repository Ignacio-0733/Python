#Tarea 1
def validar_nombre(nombre):
    return len(nombre) >= 3
def validar_password(password):
    numero = False
    for cont in password:
        if '0' <= cont <= '9':   
            numero = True
            break
    return len(password) >= 8 and numero
def registrar_usuario(nombre, password):
    if not validar_nombre(nombre):
        print("Error: nombre inválido")
        return False
    else:
        print("Nombre guardado")
    if not validar_password(password):
        print("Error: contraseña inválida")
        return False
    else:
        print("Contraseña guardada")
    print("Registro completado")
    return True
nombre = input("Pon tu usuario: ")
password = input("Pon tu contraseña: ")

registrar_usuario(nombre, password)



#Tarea 2
def calcular_total(precio,cantidad,descuento):
    def calcular_subtotal(precio,cantidad):
        subtotal=precio*cantidad
        print('Subtotal:',subtotal,'€')
        return subtotal
    def aplicar_descuento(subtotal,descuento):
        total=subtotal-(subtotal*(descuento/100))
        print('Total con el descuento: ',total)
        return total
    subtotal=calcular_subtotal(precio,cantidad)
    aplicar_descuento(subtotal,descuento)
    
precio=float(input('Pon el precio'))
cantidad=int(input('Pon la cantidad'))
descuento=float(input('Pon el descuento'))
calcular_total(precio,cantidad,descuento)


#Tarea 3
notas = []
def analizar_notas(notas):
    def calcular_media(lista):
        return sum(lista) / len(lista)
    def calcular_max_min(lista):
        return max(lista), min(lista)
    def contar_aprobados(lista):
        aprobado = 0
        suspenso = 0
        for i in lista:
            if i >= 5:
                aprobado += 1
            else:
                suspenso += 1
        return aprobado, suspenso
    media = calcular_media(notas)
    maximo, minimo = calcular_max_min(notas)
    aprobado, suspenso = contar_aprobados(notas)
    print('Nota media:', media)
    print('Nota máxima:', maximo)
    print('Nota mínima:', minimo)
    print('Número de aprobados:', aprobado)
    print('Número de suspensos:', suspenso)
for i in range(1, 6):
    nota = float(input('Introduce la nota: '))
    notas.append(nota)
analizar_notas(notas)





