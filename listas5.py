tex= str(input("Digite el una palabra: "))          
tex= tex.upper()
listTex= tex.split(" ")
list1=list(set(listTex))

print(list1)