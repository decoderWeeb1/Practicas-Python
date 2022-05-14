#Ejercicio 2
acumEdad=0
minEdad=0
opcion=0
contH=0
contM=0
contCantEst=0
acumPeso=0
contPeso=0

print("Bienvenido al programa de gestión")
print(" ")
print("Ingrese los datos")
while opcion==0:
    edad=int(input("Ingrese la edad del alumno: "))
    acumEdad=acumEdad+edad
    contCantEst=contCantEst+1
    if edad<25:
        minEdad=minEdad+1
    
    peso=int(input("Ingrese el peso del alumno"))
    acumPeso=acumPeso+peso
    if peso>50:
        contPeso=contPeso+1
        
    gen=str(input("Ingrese si el alumno es hombre o mujer: "))
    if gen=="hombre":
        contH=contH+1
    else:
        contM=contM+1
          
    salida=str(input("Desea salir del programa? "))
    if salida=="si":
        opcion=1
    else:
        opcion=0

promedio=acumEdad/contCantEst
porcH=(contH/contCantEst)*100
porcM=(contM/contCantEst)*100

print("El promedio de edad es de: ",promedio)
print("La suma total de pesos es de: ",acumPeso)
print("Cantidad de estudiantes con peso mayor a 50Kg es de: ",contPeso)
print("Cantidad de estudiantes con edad menor a 25 años es de: ",minEdad)
print("Porcentaje de hombres procesados: ",porcH,"%")
print("Porcentaje de mujeres procesadas: ",porcM,"%")
