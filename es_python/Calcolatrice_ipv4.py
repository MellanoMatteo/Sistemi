
GRANDEZZA_IPV4 = 32 

def toBit(num):
    broadcast = []
    #per tutti i settori dell'ip
    for gruppo in num:
        #trasformo da decimale a binario
        num = bin(int(gruppo))
        #elimino i primi 2 numeri della stringa
        num = num[2:]
        #aggiungo tutti i bit mancanti all'inizio del numero, con valore 0
        while len(num) < 8:
            num = "0" + num
        #aggiungo il valore appena trovato alla lista che contiene i settori in binario
        broadcast.append(num)
    return broadcast

def toStrings(listOfNumber):
    #creo una lista 
    out = ""
    #per tutti i settori dell'ip
    for elemento in listOfNumber:
        #trasformo il numero da binario a decimale e lo aggiungo alla stringa di output
        out += str(int(elemento, 2))
        #aggiungo il punto tra un settore e l'altro
        out +='.'
    #elimino l'ultimo punto 
    out = out[:-1]
    return out

def ipMaker(broadcast, subnet):

    lista = [] #0:broadcast, 1: primo valido, 2: ultimo valido
    firstUsable = broadcast
    
    # variabiel che tiene conto di tutti i settori dell'ip
    contSettori = 4
    cont = 0
    appoggio = []

    #per tutti i numeri da trasformare in 1
    for i in range(GRANDEZZA_IPV4 - subnet):
        #se i è divisibile per 8, cambio settore all'indietro
        if i % 8 == 0:
            contSettori -= 1

        cont = 8 - (i % 8) - 1

        appoggio = list(firstUsable[contSettori])
        #procedendo da destra verso sinistra, e tenendo conto del cambio di settore, metto il bit a 1
        appoggio[cont] = "0"
        firstUsable[contSettori]  = ''.join(appoggio)

        #creo una lista del numero binario 
        appoggio = list(broadcast[contSettori])
        #procedendo da destra verso sinistra, e tenendo conto del cambio di settore, metto il bit a 1
        appoggio[cont] = "1"
        #ritrasformo la lista in stringa
        broadcast[contSettori]  = ''.join(appoggio)

        #-----

        
    

    lista.append(broadcast)
    lista.append(firstUsable)
    print(lista)

    return lista


def main():
    num = []
    ip = input("inserire indirizzo ipv4 di rete: ")
    subnet = int(input ("inserire la subnet mask in formato decimale: "))

    num = ip.split(".")
    #print(num)

    broadcast = toBit(num)

    broadcastInBit = ipMaker(broadcast, subnet)

    print(broadcastInBit)


if __name__ == "__main__":
    main()
