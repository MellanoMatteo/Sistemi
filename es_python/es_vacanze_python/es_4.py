#Il ROT-15 è un semplice cifrario monoalfabetico, 
# in cui ogni lettera del messaggio da cifrare viene 
# sostituita con quella posta 15 posizioni più avanti nell'alfabeto.
#Scrivi una semplice funzione in grado di criptare una stringa passata, 
# o decriptarla se la stringa è già stata precedentemente codificata.

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 

#la A viene considerata come la 1a lettera, non come la numero 0

def cripta(stringa, index):
    strCriptata = ''        #inizializzo la stringa da criptare 

    for carattere in stringa:   #per tutti i caratteri della stringa data in input
        cont = 0

        while alfabeto[cont] != carattere:      #cerco la lettera della stringa all'interno dell'alfabeto
            cont += 1

            if(cont > len(alfabeto)-1):                     # se non sono stati inserite lettere nella stringa 
                print("sono stati inseriti valori non validi")
                return -1

        if cont+index > len(alfabeto):                      # se la somma dell'indice della stringa e la chiave superano la lunghezza dell'alfabeto
            carattere = alfabeto[cont+index-len(alfabeto)]  # la lettera criptata sarà la lettera data dalla differenza tra l'indice + la chiave meno l'alfabeto
        else:
            carattere = alfabeto[cont+index]                #altrimenti la lettera corrisponde semplicemente all'indice della lettera dell'alfabeto + la chiave

        strCriptata += carattere                            #aggiungo la lettera criptata alla stringa che verrà data in output
    return strCriptata


def decripta(stringa, index):
    strDecriptata = ''

    for carattere in stringa:                               #per tutti i caratteri della stringa 
        cont = 0

        while alfabeto[cont] != carattere:                  #finchè ci sono caratteri 
            cont += 1

            if(cont > len(alfabeto)-1):                     #se il carattere della stringa è contenuto all'interno dell'alfabeto
                print("sono stati inseriti valori non validi")
                return -2

        if cont-index < 0:                                  #se l'indice della lettera da decriptare è minore della chiave 
            carattere = alfabeto[len(alfabeto)-(index - cont)]  #il carattere sarà quello datto dalla differenza tra la lunghezza dell'alfabeto e la differenza tra la chiave e l'indice della lettera
        else:
            carattere = alfabeto[cont-index]                #altrimenti la lettera decriptata corrisponderà a quella con indice dato dalla differenza tra l'indice della lettera criptata e la chiave

        strDecriptata += carattere
    return strDecriptata

def main():
    stringa= input("inserire la stringa da codificare o decodificare (SOLO LETTERE AMMESSE)")
    criptata = cripta(stringa, 15)
    print (criptata)
    decriptata = decripta(criptata, 15)
    print(decriptata)

if __name__ == "__main__":
    main()
