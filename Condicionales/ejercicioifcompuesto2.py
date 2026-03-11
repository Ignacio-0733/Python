num1=int(input("Pon un valor"))
if not num1<0 and num1!=0:
    if num1%2==0:
        print("El valor es par")
    else:
        print("El numero es impar")
else:
    print("Error")

num2=int(input("pon un valor"))
if num2>0:
    print("El numero es mayor a 0")
    if num2>9 and num2<100:
        if num2%2==0:
            print("El numero es par")
        else:
            print("El numero es impar")
    elif num2>99 and num2<1000:
        print("el resto al dividir este valor entre 2 es de",num2%2)
else:
    print("error")
        
    
            
            





