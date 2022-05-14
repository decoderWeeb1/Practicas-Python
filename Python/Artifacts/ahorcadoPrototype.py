import time
nom=input("Como te llamas: ")
print("Hola, "+nom," es hora de jugar")
print(" ")
time.sleep(1)
print("Comienza a adivinar!!!")
time.sleep(0.5)
print("Para el anfitrion del juego")
palabra_adivinar=input("Ingresa la palabra a adivinar: ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ") #La cantidad multiple de print es para que cuando se digite la palabra, el jugador no vea la palabra despues.
palabra=palabra_adivinar
tupalabra=" "
Vidas=5 #cantidad de vidas

while Vidas > 0: #Lo que se va a ejecutar mientras tengamos vidas
    fallas=0
    for letra in palabra: #Lo que determina si una letra digitada hace parte de la palabra o no
        if letra in tupalabra:
            print(letra,end="")
        else:
            print("*",end="")
            fallas+=1
    if fallas==0:
        input()
        print("")
        print("Felicidades, ganaste!!!")
        input()
        break

    tuletra=input("Introduce una letra: ") #Entrada de la letra
    tupalabra+=tuletra

    if tuletra not in palabra: #Se ejecuta cuando ingresa una letra equivocada
        Vidas-=1
        print("Equivocacion")
        print("Tu tienes ",+Vidas," vidas")
    if Vidas==0: #Si se llega a equivocar
        print("Perdiste!")
else:
    input()
    print("Gracias por participar!")
    input()
