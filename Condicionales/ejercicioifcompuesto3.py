edad=int(input("pon tu edad"))
altura=int(input("pon tu altura en centimetros"))

if altura<140:
    if edad<12:
        print("Puede entrar a las atracciones infantiles")
    else:
         print("No puedes acceder a las atracciones infantiles debido a la edad")
elif altura>139 and altura<171:
    if edad<12:
        print("Puedes acceder a las atracciones familiares")
    else:
        print("Puedes acceder a las atracciones familiares y de intensidad media")
elif altura>170:
    if edad<12:
        print("Puedes acceder a las familiares y de intensidad media")
    else:
        print("Puedes acceder a las familiares e intensidad media y alta")

else:
    print("Error")


    
    
            
               

