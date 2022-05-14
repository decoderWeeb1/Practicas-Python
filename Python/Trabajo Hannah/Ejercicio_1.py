#Ejercicio 1
max=0
min=100
opcion=0
contH=0
contM=0

print("Bienvenido al programa de gestión")
print(" ")
print("Ingrese los datos")
while opcion==0:
    gen=str(input("Ingrese si el alumno es hombre o mujer: "))
    if gen=="hombre":
        contH=contH+1
    else:
        contM=contM+1
    
    edad=int(input("Ingrese la edad del alumno: "))
    if edad>max:
        max=edad
    elif edad<min:
        min=edad
        
    salida=str(input("Desea salir del programa? "))
    if salida=="si":
        opcion=1
    else:
        opcion=0


print("Cantidad de Hombres: ",contH)
print("Cantidad de Mujeres: ",contM)
print("Edad mayor: ",max)
print("Edad menor: ",min)
