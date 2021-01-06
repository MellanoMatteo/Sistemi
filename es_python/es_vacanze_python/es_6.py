#  6. Il file annual.csv (allegato) contiene la anomalia della temperatura globale del pianeta Terra dal 1880 ad oggi,
#  proveniente da varie fonti (colonna “Source”). 
# Scrivere un programma che generi un dizionario che abbia come chiave l’anno (“Year”) 
# e valore la media aritmetica delle anomalie registrate dalle varie fonti durante quell’anno.
# Inoltre scrivere una funzione che dati in input due anni diversi (anno_1 e anno_2) 
# trovi la anomalia massima e minima nel periodo compreso tra anno_1 e anno_2.

import csv

def generaListaDiDizionari():

    #apro e leggo il file csv
    with open('annual.csv') as csv_file:
        #suddivido il file letto in parti delimitate dalla virgola
        lettura = csv.reader(csv_file, delimiter=',')
        
        #lista in cui salvo il massimo ed il minimo per ogni fonte
        listaMisurazioni = []
        #dizionario di tutte le misurazioni GIAG
        dizionarioGIAG = {}
        #dizionario per tutte le misurazioni GISTEMP
        dizionarioGISTEMP = {}
        #evito la prima riga che è quella d'intestazione
        primaRiga = True
        #contatore per vedere da quale fonte sto leggendo
        cont = 0
        #per tutte le righe che sono state lette
        for riga in lettura:
            #evito la prima riga
            if primaRiga:
                primaRiga = False
            else:
                
                if cont % 2 == 0:
                    #siamo nella colonna giag
                    dizionarioGIAG[riga[-2]] = riga[-1] #il penultimo valore letto è l'anno, ovvero la chiave, e l'ultimo è la misurazione
                else:
                    #simao nella riga gistemp
                    dizionarioGISTEMP[riga[-2]] = riga[-1] #il penultimo valore letto è l'anno, ovvero la chiave, e l'ultimo è la misurazione
                cont+=1
        #inserisco i dizionari all'interno della lista per poi restituirla
        listaMisurazioni.append(dizionarioGIAG)
        listaMisurazioni.append(dizionarioGISTEMP)

        return listaMisurazioni

def anomaliaMaxMin (anno1, anno2, listaMis):
    
    #liste che contengono rispettivamente il minimi ed il massimi valori per ogni dizionario
    listaMin = []
    listaMax = []
    #valori indicativi per la gestione della massimo e del minimo
    mass = -100
    minimo = 100
    
    #per la lunghezza della lista restituita dalla funzione generaListaDizionari
    for indice in range(len(listaMis)):
        #scorro per la chiave
        for key in listaMis[indice]:

            #print(key)
            #print(dizionario[key])
            #print(anno1)

            #se la chiave è contenuta all'interno dei valori che ha inserito l'utente 
            if int(key) <= anno2 and int(key) >= anno1:
                #print(f"entro per {key}")
                
                # se il valore del dizionario alla chiave corrente è maggiore del massimo, aggiorno la variabile mass con il valore massimo appena trovato
                if float(listaMis[indice][key]) > float(mass):
                    mass = float(listaMis[indice][key])

                # se il valore del dizionario alla chiave corrente è minore del minimo, aggiorno la variabile minimo con il valore minimo appena trovato 
                if float(listaMis[indice][key]) < float(minimo):
                    minimo = listaMis[indice][key]

            # se ho superato il valore minimo (i dizionari partono dall'ultima riga del file a causa della funzione append), è inutile scorrere in quanto sono fuori dal range chiesto dall'utente 
            elif int(key) < anno1:
                #quindi salvo il valore massimo e il valore minimo nelle apposite liste e fermo il ciclo
                listaMin.append(minimo)
                listaMax.append(mass)
                break
    
    #print(listaMax)
    #print(listaMin)
    
    #riinizializzo le variabili mass e minimo in modo che contengano il primo valore delle liste corrispondenti
    mass = listaMax[indice]
    minimo = listaMin[indice]
    
    #controllo per tutti i valori
    for indice in range(len(listaMax)-1):  
        #se il valore massimo, che la prima volta rappresenta il primo, è minore del successivo, mass prende il valore del successivo  
        if mass <  listaMax[indice + 1]:
            mass = listaMax[indice + 1]
        #se il valore minimo, che la prima volta rappresenta il primo, è maggiore del successivo, minimo prende il valore del successivo  
        if minimo > listaMin[indice + 1]:
            minimo = listaMin[indice + 1]
    
    #creo una lista per ritornare il minimo dei minimi ed il massimo dei massimi
    listaRisultati = []
    listaRisultati.append(mass)
    listaRisultati.append(minimo)

    return listaRisultati 

def main():
    #chiedo una prima volta gli estremi del range da considerare
    anno1 = int( input("inserire anno da cui si vuole processare i dati (primo anno rilevato: 1880): ") )
    anno2 = int(input("inserire l'ultimo anno da cui si vuole processare (ultimo anno rilevato: 2016): "))
 
    #e input errato, lo ripropongo
    while(anno1 <= 1880 or anno1 >= 2016 or anno2 >= 2016 or anno2 <= 1880):
        print("inserimento errato, prego riinserire")
        anno1 = int( input("inserire anno da cui si vuole processare i dati (primo anno rilevato: 1880): ") )
        anno2 = int(input("inserire l'ultimo anno da cui si vuole processare (ultimo anno rilevato: 2016): "))

    #massimo prende il valore della prima cella della lista restituita dalla funzione anomaliaMaxMin, e minimo la seconda
    massimo = anomaliaMaxMin(anno1, anno2, generaListaDiDizionari())[0]
    minimo = anomaliaMaxMin(anno1, anno2, generaListaDiDizionari())[1]

    #eseguo l'output
    print(f"massimo registrato: {massimo}, minimo registrato: {minimo}")

if __name__ == "__main__":
    main()