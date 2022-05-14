import time
nom=input("Ingresa tu nombre: ")
print("Hola "+nom+", juguemos al ahorcado")
print(" ")
time.sleep(1)
print("Comienza a adivinar")
time.sleep(0.5)
palabra="Hola"
tupalabra=''
life=4

while life>0: 
    fallas=0
    for letra in palabra:
        if letra in tupalabra:
            print(letra,end="")
        else:
            print("*",end="")
            fallas+=1
    if fallas==0:
        print("")
        print("Felicidades ganaste el juego")
        break

tuletra=input("Introduce una letra: ")
tupalabra+=tuletra

if tuletra not in palabra:
    life-=1
    print("Equivocacion")
    print("Tu tienes "+life+" vidas")
if life==0:
    print("Perdiste :(")
else:
    print("Gracias por participar")
