#Nella serie di Fibonacci, ciascun numero della serie è la somma dei due numeri 
# #nella serie che lo precedono, ad esempio:1, 1, 2, 3, 5, 8, 13 (...)
#Scrivi una funzione ricorsiva che restituisce in output 
# i numeri della sequenza di Fibonacci, entro una soglia 
# specifica impostata dall'utente.


def serieFibonacci(limite, ultimoVal, penultimoVal, cont):
    #se ho oltrepassato il limite esco
    if cont >= limite:
        exit(1)
    #altrimenti stampo il valore
    print(ultimoVal)
    #aggiorno l'ultimo ed il penultimo valore, ed aggiorno il contatore delle volte che si stampa
    valAppoggio = ultimoVal
    ultimoVal += penultimoVal
    penultimoVal =  valAppoggio
    cont +=1
    #richiamo la funzione 
    serieFibonacci(limite, ultimoVal, penultimoVal, cont)


def main():
    #chiedo quanti valori si devono calcolare della serie
    limite = int(input("inserire quanti numeri si vogliono in output"))
    #inizializzo i valori
    ultimoVal = cont = 0
    penultimoVal = 1
    #richiamo per la prima volta la funzione 
    serieFibonacci(limite, ultimoVal, penultimoVal, cont)

if __name__ == "__main__":
    main()