#Scrivi una funzione generatrice di password. La funzione deve generare una stringa 	
#alfanumerica di 8 caratteri qualora l'utente voglia una password semplice, 
#o di 20 caratteri 	ascii qualora desideri una password più complicata.
import random, string

def generaPassword(lenght):
    #creo la variabile di nome password
    password = ''
    #per tutta la lunghezza desiderata
    for _ in range(lenght):
        #estraggo un numero a sorte da 0 a 94
        valRandom = random.randint(0,61)
        password += string.printable[valRandom]
        #la printable è una stringa di tutti i caratteri presenti. sono 100, ma escludo gli ultimi 6 perchè la stringa deve essere alfanumerica
    return password

def main():
    #input della difficoltà della password
    difficolta = int(input("vuoi una password facile(1) o difficile(2)? ")) 
    #aggiorno la lunghezza della password in base alla sua difficoltà
    if difficolta == 1:
        lenght = 8
    elif difficolta == 2:
        lenght = 20
    #stampo al password
    print (generaPassword(lenght))

if __name__ == '__main__':
    main()
