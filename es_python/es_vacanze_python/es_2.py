#2. Un indirizzo MAC (Media Access Control address) è un indirizzo univoco 
# #associato dal produttore, a una NIC, composto da 6 coppie di cifre 
# esadecimali separate da due punti.
#Un esempio di MAC è 02:FF:A5:F2:55:12.
#Scrivi una funzione genera_mac che generi degli indirizzi MAC pseudo casuali.

import random

#la lista di tutti i caratteri che sono validi per la creazione di un indirizzo MAC
caratteri = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def generaMAC():
    #creo la stringa per il mac
    mac = ''

    #per tutta la lunghezza del MAC (hanno sempre 17 caratteri)
    for i in range(17):
        # se mi trovo in posizione 2,5,7,9 metto i :
        if (i + 1) % 3 == 0:
            mac += ':'
        else:
            #altrimenti tiro a caso un carattere dalla stringa sopra creata, meno 1 perchè lìindice della lista parte da 0
            mac += caratteri[random.randint(0, len(caratteri)-1)]
    #infine ritorno l'indirizzo
    return mac

def main():
    print (generaMAC())

if __name__ == "__main__":
    main()

