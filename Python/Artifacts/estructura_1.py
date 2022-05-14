nom=str(input("Nombre: "))
print("Bienvenido "+nom)
i=0
quest1=str(input("La maquina de Turing fue inventada por? "))
if quest1=="Alan Turing" or "alan turing" :
    print("Correcto!!!")
    i=i+1
else:
    print("No, fue Alan Turing")
    i=i+0

quest2=str(input("Cual fue el primer computador personal vendido a gran escala?"))
if quest2=="Apple 2" or "apple 2":
    print("Correcto!!!")
    i=i+1
else:
    print("No, fue el Apple II lanzado en 1987")
    i=i+0

quest2=str(input("Que sistema operativo comenzo a desarrollar Linus Torvalds?"))
if quest2=="Linux" or "linux":
    print("Correcto!!!")
    i=i+1
else:
    print("No, fue Linux en el año 1991")
    i=i+0

print("Preguntas correctas")
print(i)
if i==3 or 2:
    print("Muy bien")
elif i==1: 
    print("Regular")
else:
    print("Pesimo")
