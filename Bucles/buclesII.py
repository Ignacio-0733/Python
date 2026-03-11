#PRIMER EJERCICIO
n=1
while n!=10:
    for n in range(1,11):
        resul=2*n
        print('2x',n,'=',resul)

#SEGUNDO EJERCICIO
num21=0
num22=1

for cont2 in range(0,10):
    num23=num21+num22
    print(num23)
    num21=num22
    num22=num23


#TERCER EJERCICIO
num3=1
for cont3 in range(1,16):
    num31=num3*cont3
    num3=num31
    print(num31)
                
#CUARTO EJERCICIO
num4=int(input('Introduce un numero del 0 al 999: '))
while num4!=0:
    if num4<=9:
        print('El numero tiene 1 digito')
    elif num4>=10 and num4<=99:
        print('El numero tiene 2 digitos')
    elif num4>=100 and num4<=999:
        print('El numero tiene 3 digitos')
    else:
        print('El numero no está en el rango')
        
    num4=int(input('Introduce un numero del 0 al 999: '))
