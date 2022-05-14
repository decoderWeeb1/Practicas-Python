#Ejercicio 4
acumEdad=0
contEdad=0
minEdad=100
opcion=0
contCantEst=0
acumPeso=0
contPeso=0
maxPeso=0
contEdad2=0

print("Ingrese los datos")
while opcion==0:
    edad=int(input("Ingrese la edad del alumno: "))
    acumEdad=acumEdad+edad
    contCantEst=contCantEst+1
    if edad>20:
        contEdad=contEdad+1
    elif edad<minEdad:
        minEdad=edad
        
    if edad>=21 and edad<=25:
        contEdad2=contEdad2+1
    
    peso=int(input("Ingrese el peso del alumno: "))
    acumPeso=acumPeso+peso
    if peso<60 and edad>18:
        contPeso=contPeso+1
    elif peso>maxPeso:
        maxPeso=peso

          
    salida=str(input("Desea salir del programa? "))
    if salida=="si":
        opcion=1
    else:
        opcion=0

promedio=acumEdad/contCantEst

print("El promedio de edad es de: ",promedio)
print("La suma total de pesos es de: ",acumPeso)
print("Mayor peso capturado: ",maxPeso)
print("Menor edad ingresada: ",minEdad)
print("Cantidad de estudiantes con edades superiores a 20 años es de: ",contEdad)
print("Cantidad de estudiantes con peso menor a 60 Kg y edad mayor a 18 años es de: ",contPeso)
print("Cantidad de estudiantes que están entre los 21 y 25 años de edad es de: ",contEdad2)
