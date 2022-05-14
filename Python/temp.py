#Ejercicio 1
A=int(input("Ingrese el valor de A: "))
R=A%2
if R==0:
    print("PAR")
else:
    print("IMPAR")
    
#Ejercicio 2
C1=float(input("Ingrese el valor de la calificacion 1: "))
C2=float(input("Ingrese el valor de la calificacion 2: "))
C3=float(input("Ingrese el valor de la calificacion 3: "))

ND=((C1+C2+C3)/3)

if ND>=3:
    print("APROBADO")
else:
    print("REPROBADO")

#Ejercicio 3
cat=int(input("Ingrese la categoria del trabajador: "))
sueldo=int(input("Ingrese el sueldo del trabajador: "))

if cat==1:
    NS=sueldo*1.20
    print(NS)
elif cat==2:
    NS=sueldo*1.15
    print(NS)
elif cat==3:
    NS=sueldo*1.10
    print(NS)
elif cat==4:
    NS=sueldo*1.05
    print(NS)
else:
    print("Error")

#Ejercicio 4
Dist=int(input("Ingrese la distancia recorrida por el ferrocarril: "))
T=int(input("Ingrese el tiempo de instancia (dias) en el lugar: "))

if T>7 and Dist*2>800:
    PT=(((Dist*2)*280)*0.70)
    #PT=(Dist*2*0.70)
    print(PT)
else:
    PT=((Dist*2)*280)
    print(PT)
