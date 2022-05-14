def capturar():
    global lista
    lista=[]
    print("Cuantos elementos va a tener la lista?")
    n=input()
    n=int(n)
    for i in range(0,n):
        print("Ingresa el numero del indice",i)
        elemento=input()
        lista.insert(i,elemento)
def mostrar():
    print(lista)

def agregar():
    print("Ingresa el elemento que desea agregar:")
    elemento=input()
    print("Ingrese el indice donde desea agregarlo:")
    indice=input()
    indice=int(indice)
    longitud=len(lista)
    longitud=int(longitud)
    if(indice>longitud or indice<0):
        print("El indice debe estar entre 0 y",longitud)
    else:
        lista.insert(indice,elemento)
        print("Elemento agregado")

def eliminar():
    print("Ingresa el elemento que desea eliminar:")
    indice=input()
    indice=int(indice)
    longitud=len(lista)
    longitud=int(longitud)
    if(indice>longitud or indice<0):
        print("El indice debe estar entre 0 y",longitud-1)
    else:
        del lista[indice]
        print("Elemento eliminado")

def modificar():
    print("Ingresa el elemento que desea modificar:")
    indice=input()
    indice=int(indice)
    print("Ingrese el nuevo valor del elemento")
    elemento=input()
    longitud=len(lista)
    longitud=int(longitud)
    if(indice>longitud or indice<0):
        print("El indice debe estar entre 0 y",longitud-1)
    else:
        lista[indice]=elemento
        print("Elemento modificado")

capturar()
mostrar()
agregar()
mostrar()
eliminar()
mostrar()
modificar()
mostrar()