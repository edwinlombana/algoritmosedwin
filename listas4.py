#listUno=[20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
listDos=[]
i=0
while i < 20:
    Uno=int(input("Digite Un Numero De La Lista: "))
    while Uno < 0:
        print("por favor digite numeros postivos")
        break
    listDos.append(Uno)
    i+=1
    for j in listDos:
        if j < 0:  
            listDos.remove(Uno)
print(listDos)
