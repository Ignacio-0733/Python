#Ejercicio 1
palabra=input("Introduce una palabra y se te mostrara 40 veces")
for dato in range(40):
              print (palabra)


#Ejercicio 2
num1=int(input("Introduce un numero del 1 al 100 o mayor que 100 para parar"))
while num1<=100:
    num1=int(input("Introduce un numero"))
    if num1%2==0:
        print ("el numero es par")
    else:
        print ("el numero es impar")

#Ejercicio 3

num2=int(input("Pon un numero entreo mayor que 0 y se te mostrara la cuenta atras de ese"))
for valor in range(num2+1):
    print(num2)
    num2=num2-1

#Ejercicio 4
num3=int(input("Pon un numero entero y se te mostrara una piramide de asteriscos con la base de numero de astericos que has puesto"))

for num3 in range(num3+1):
         print ("*" *  num3)

#Ejercicio 5
num4=int(input("Pon un numero entero y te dira si es primo o no"))
for i in range(2, num4):
        if num4 % i == 0:
            print(" no es primo")
        else:
            print("es primo")
#Ejercico 6
palabra=input("Pon una palabra, si poner salir se cerrara")
while palabra!="salir":
    print(palabra)
    palabra=input("Pon una palabra, si poner salir se cerrara")
    
    



         
    
    
         
         
    
