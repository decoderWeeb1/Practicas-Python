def capturar():
    global lista
    lista=[]
    print("Cuantos elementos va a tener la lista?")
    n=input()
    n=int(n)
    for i in range(0,n):
        print("Ingresa el numero del indice",i+1)
        elemento=input()
        lista.insert(i,elemento)
def mostrar():
    print(lista)

capturar()
mostrar()
