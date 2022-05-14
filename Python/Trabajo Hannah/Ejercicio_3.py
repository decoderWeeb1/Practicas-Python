#Ejercicio 3

print("Conjetura de ULAM")
num=int(input("Ingrese el numero para iniciar la secuencia: "))
print(num)

while(num>1):
    if num%2==0:
        num=num/2
        print(num)
    elif num%2!=0:
        num=(num*3)+1
        print(num)
