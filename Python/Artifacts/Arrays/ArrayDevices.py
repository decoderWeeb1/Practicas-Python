import winsound
frequency=2500
duration=1000 #1000ms=1sec


print("Device 1")
def histogram1(items):
    for n in items:
        output=''
        times=n
        while(times>0):
            output+='*'
            times=times-1
        print(output)
histogram1([4,1,6,8])


for i in [1]:
    winsound.Beep(frequency,duration)

#Prototype
print(" ")
print("Prototype Device")
global histogram
def histogram2(items):
    for n in items:
        output=''
        times=n
        while(times>0):
            output+='*'
            times=times-1
        print(output)        
histogram2([2,1,2,5])
x=input("Deseas cambiar el histograma? ")
if x=="si":
    histogramX=[2,2,2,5]
    histogramX[0]=int(input("Ingrese el numero de la posicion 0: "))
    histogramX[1]=int(input("Ingrese el numero de la posicion 1: "))
    histogramX[2]=int(input("Ingrese el numero de la posicion 2: "))
    histogramX[3]=int(input("Ingrese el numero de la posicion 3: "))
    items=histogramX
    histogram2(items)
else:
    print("Prototype Device")
    histogram2([2,1,2,5])