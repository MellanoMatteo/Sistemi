"""memorizzazione pavimento ostacoli  per un robot di pulizia"""

#stanza rettangolare

#pavimento composto da piastrelle quadrate (matrice)

#nx = numero di piastrelle sul lato alto/basso
#ny = numero di piastrelle sul lato sinistro/destro

#pavimento con ostacoli

#array(pavimento) -> lista di liste [[], [], ...]

#dalla lsita di liste si trovano le celle libere e le si da un ID

#costruire un dizionario {casella_in_cui_si_è : [lista_delle_celle_a_cui_può_accedere], ...}


def main():
    nx = 6
    ny = 5
    field = [[0, 0, 1, 1, 1, 1],
             [1, 1, 1, 1, 0, 1],
             [0, 1, 0, 1, 1, 1],
             [1, 1, 0, 1, 0, 1],
             [1, 1, 0, 1, 1, 1]]

    field = renameDict(field, nx, ny)
    
    dizionario = creaDizionario(field, nx, ny)

    print(dizionario)



def creaDizionario(field, nx, ny):
    MURO = 0
    diz = {}
    celle_adiacenti = [[-1, 0], [0 ,1], [1, 0], [0, -1]]
    
    k = 1
    for i,ei in enumerate(field):
        for j,ej in enumerate(field[i]):     #i rappresenta la riga, j la colonna
            if field[i][j] != 0:

                celleAccessibili = []     #celle in cui il robot può transitare
                for ca in celle_adiacenti:  #per tutte le celle adiacenti
                    # se la casella su cui siamo si trova su un bordo e cerchiamo di trovare la casella oltre il bordo, continua
                    if i + ca[0] < 0 or i + ca[0] >= len(field) or j + ca[1] < 0 or j + ca[1] >= len(field[0]):
                        continue
                    #se la casella adiacente non è un muro, la salvo nella lista di caselle a cui si può accedere
                    if field[i+ca[0]][j+ca[1]] != MURO:
                        celleAccessibili.append(field[i+ca[0]][j+ca[1]])

                diz[k] = celleAccessibili   #salvo la lista di caselle nel dizionario apposito
                k += 1                      #aggiorno il contatore che indica la chiave del dizionario
    #ritorno il dizionario 
    return diz


def renameDict(field, nx, ny):
    cont = 1
    #per tutto il campo
    for i,ei in enumerate(field):
        for j,ej in enumerate(field[i]):
            #se la cella che cosnidero non è un ostacolo, viene numerata
            if field[i][j] != 0:
                field[i][j] = cont
                cont += 1
    #ritorno il campo numerato
    return field


if __name__ == '__main__':
    main()