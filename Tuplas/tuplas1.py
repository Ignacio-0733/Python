valores2=(1,2,3,4)
valores1=(5,6,7,8)
suma=()
resta=()
producto=()
for i in range(4):
    suma=suma+(valores1[i]+valores2[i],)

for i in range(4):
    resta=resta+(valores1[i]-valores2[i],)

for i in range(4):
    producto=producto+(valores1[i]*valores2[i],)

print('La suma es: ',suma)
print('La resta es: ',resta)
print('La multiplicacion es: ',producto)

