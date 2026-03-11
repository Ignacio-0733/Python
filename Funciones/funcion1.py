#Tarea 1
def primo():
    num = int(input('Pon un número: '))
    for valor1 in range(2, num):
        if num % valor1 == 0:
            print('El número no es primo')
            break
    else:
        print('El número si es primo')

primo()

#TAREA 2
lista=[]
lista1=[]
for i in range(0,5):
    lista.append(int(input('Pon un valor para la lista')))

for i in range (0,5):
    lista1.append(int(input('Pon un valor para la lista1')))
def tlistas(lista,lista1):
    for i in range(len(lista)):
        if lista[i]!=lista1[i]:
            print('No son iguales')
            break
    else:
        print('Son iguales')

tlistas(lista,lista1)






