
lista = [1, 2, 4, "ciao"]
lista.append("aggiungo in coda un altro elemento")

print(lista[0:4]) #stampo gli elementi della lista dal 0 al 3
print(lista[3:])  #stampo i valori della lista  dal numero inserito fino alla sua fine (discorso uguale ma inverso per stampare dall'inizio fino ad un certo punto, che sarà però escluso)


stringa = "matteomellano"
#discorso delle liste uguale per le strighe, e sarà anche uguale per le iterazioni
print(stringa[0:4])
print(stringa[3:])

#print(lista) -> stampa il valroe della lista
for elemento in lista:
    print("ciao1")
    #print(elemento) ->stampa il valroe della lista, uno per volta

for indice, el in enumerate(lista):
    print("ciao2")
    #indice è il numero della elemento a cui siamo arrivati, -1
    #el è l'elemento della lista nel  determinato indice a cui siamo arrivati
    #print(el) -> stampa il valore della lista a quel determinato indice
    #print(lista[indice]) == print8(el)

for indice in range(0 , len(lista)):
    print("ciao3")
    #range identifica un campo in cui possiamo mouverci
    #len misura la lunghezza della lista
    #indice è il numero corrispondente alla cella a cui siamo arrivati
    #print(lista[indice]) -> stampa il valore della lista a quel determinato indice


dizionario = {1:"Antonelli", 2:"Becchis", 3:"Bianco", 4:"Bongiovanni", 20:"Piumatto"}


for elemen in dizionario:
    print(dizionario[elemen])

