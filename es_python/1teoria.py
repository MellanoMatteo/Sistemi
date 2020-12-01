#python è un linguaggio orientato agli oggetti. in python tutto è un oggetto.

num = 7 #oggetto, ovvero una istanza della classe int

#FUNZIONI:
def laMiaFunzione(arg1, arg2):
    #codice della funzione indentato
    return arg1 + arg2

print(laMiaFunzione(3,4))

#COLLEZIONI: liste, tuple, dizionari

#LISTE: in qualche maniera "simili " agli array del C

lista = [3,5,1,2,3]
print(f"la lista e': {lista}")

#python style 
#1
for elemento in lista:
    print(elemento)

print("-----")
#2
for indice,elemento in enumerate(lista):
    print(f"indice: {indice} elemento: {lista[indice]}")

#questo ciclo scorre contemporanemente su indice e elemento

print("-----")

#C style
for indice in range(0,len(lista)):
    print(f"indice: {indice} elemento: {lista[indice]}")


stringa ="Itis Delpozzo"
print(stringa[0:5])
if(stringa[0] == "I"):
    print("inizia per i")

else:
    pass #non fa nulla, esegue senza errori







