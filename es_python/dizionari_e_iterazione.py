

lista = [3,2,-1,6,5]


#python style
#for elemento in lista:
#    print(elemento)

#c style

#for i in range(0,len(lista)):
 #   print(lista[i])

#python style con enumerate

#for i, elemento in enumerate(lista):
#    print(f"{i} , {elemento}")


#while
contatore = 0
while(contatore < len(lista)):
    print(lista[contatore])
    contatore= contatore + 1 


############################################

#I  DIZIONARI
#un dizionario è una collezine di elementi
    #ciascuno dei quali è costituito da una chiave ed un valore
#ogni elemento di un dizionario è una coppi del tipo chiave:"valore"
#la chiave può anche non essere un intero, ma anche uan stringa o cosa si voglia

dizionario = {1:"Antonelli", 2:"Becchis", 3:"Bianco", 4:"Bongiovanni", 20:"Piumatto"}

#per accedere al valore di un elemento del dizionario si utilizza la notazione : 
#nome_dizionario[chiave]

print(dizionario)

dizionario[19] = "Orlando" #non ordina in base all'indice
for elemen in dizionario:
    print(elemen)

print(dizionario)

canzone ={"numero" : 1 , "titolo" : "Francesco Totti", "autore" : "Bello Figo"}

print(canzone["titolo"])

#lettura da file

file = open("domande italiano.txt", "r")

#leggere la riga del file
for riga in file:
    print(riga, end="")
#end serve per non stampae il doppio a capo, (1 del print, uno dello \n della stringa)
file.close()

