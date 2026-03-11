#EJERCICIO 1
#Bucle while
num=1
while num<100:
    num=num+1
    print(num)
#Bucle for
for valor in range(1,101):
    print(valor)

#EJERCICIO 2
num2=0
num1=int(input('Introduce un numero positivo, un negativo para salir'))
while num1>0:
    resultado=num2+num1
    print(resultado)
    num2=resultado
    print('Acomulado: ',resultado)
    num1=int(input('Introduce un numero positivo, un negativo para salir'))
  
    
else:
    print('Has salido')
    print ('Resultado: ',resultado)

#EJERCICIO 3
num3=int(input('Introduce 1 para sumar, 2 para restar, 3 para multiplicar, 4 para salir'))
while num3==1:
    num3=int(input('Introduce el primer numero para sumar'))
    num4=int(input('Introduce el segundo numero para sumar'))
    num5=num3+num4
    print('Resultado de la suma:',num5)
    num3=int(input('Introduce 1 para sumar, 2 para restar, 3 para multiplicar, 4 para salir'))
    
while num3==2:
    num3=int(input('Introduce el primer numero para restar'))
    num4=int(input('Introduce el segundo numero para restar'))
    num5=num3-num4
    print('Resultado de la resta:',num5)
    num3=int(input('Introduce 1 para sumar, 2 para restar, 3 para multiplicar, 4 para salir'))
while num3==3:
    num3=int(input('Introduce el primer numero para multiplicar'))
    num4=int(input('Introduce el segundo numero para multiplicar'))
    num5=num3*num4
    print('Resultado de la multiplicacion:',num5)
    num3=int(input('Introduce 1 para sumar, 2 para restar, 3 para multiplicar, 4 para salir'))
while num3==4:
    print ('Has salido')
    break

    
    


               
    
    


