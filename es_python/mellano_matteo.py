import pygame
import sys
import csv

DIM_QUADRETTO =50
NERO = (0,0,0)
BIANCO = (255,255,255)
ROSSO = (255, 0, 0)

#dizionario di caratteri
caratteri ={"0": [0,0,0,0,0],
            "1": [0,0,0,0,1],
            "2": [0,0,0,1,0],
            "3": [0,0,0,1,1],
            "4": [0,0,1,0,0],
            "5": [0,0,1,0,1],
            "6": [0,0,1,1,0], 
            "7": [0,0,1,1,1], 
            "8": [0,1,0,0,0],
            "9": [0,1,0,0,1], 
            "a": [0,1,0,1,0], 
            "b": [0,1,0,1,1],
            "c": [0,1,1,0,0], 
            "d": [0,1,1,0,1], 
            "e": [0,1,1,1,0],
            "f": [0,1,1,1,1], 
            "f": [1,0,0,0,0], 
            "g": [1,0,0,0,1],
            "h": [1,0,0,1,0],
            "i": [1,0,0,1,1], 
            "l": [1,0,1,0,0],
            "m": [1,0,1,0,1], 
            "n": [1,0,1,1,0], 
            "o": [1,0,1,1,1], 
            "p": [1,1,0,0,0], 
            "q": [1,1,0,0,1], 
            "r": [1,1,0,1,0],
            "s": [1,1,0,1,1],
            "t": [1,1,1,0,0], 
            "u": [1,1,1,0,1], 
            "v": [1,1,1,1,0],
            "z": [1,1,1,1,1]}

#funzionce che data la stringa dall'utente mi restituisce la matrice 
def convertion(stringa):
    list = []
    for char in stringa:
        list.append(caratteri[char])
    return list

#funzione che data la matrice e le dimensioni della pagina, mi da in output la schermata di pygame con rappresentato il qr
def drawQR(lista, dim):
        for x in range(0,dim[0]-1, DIM_QUADRETTO):
            for y in range(0,dim[1]-1, DIM_QUADRETTO):

                if lista[int(y // DIM_QUADRETTO)][int(x // DIM_QUADRETTO)] == 0:         
                    zero = pygame.Rect(x,y, DIM_QUADRETTO, DIM_QUADRETTO)
                    pygame.draw.rect(finestra, BIANCO, zero)

                else:
                    uno = pygame.Rect(x, y, DIM_QUADRETTO, DIM_QUADRETTO)
                    #disegno la uno
                    pygame.draw.rect(finestra, NERO, uno)

#funzione che stampa sul file csv la matrice
def printCsv(lista):
    with open("file1.csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        for riga in lista:
            csvwriter.writerow(riga)

def readCsv():
    with open('file1.csv') as csv_file:
        lettura = csv.reader(csv_file)
        print(lettura)

def main():
    pygame.init()
    
    inp = ""
    #finchè la stringa richiesta non è corretta, la faccio riinserire
    stringaCorretta = False
    while stringaCorretta == False:
        inp = input("inserire al stringa da codificare(max 12 caratteri): ")
        if len(inp) < 12:
            stringaCorretta = True
    
    #print("inser. ok")
    lista = convertion(inp)
    #print("conv.ok")

    #specifiche per la pagina di pygame
    lunghezza = len(lista) * DIM_QUADRETTO
    larghezza = len(lista[0]) * DIM_QUADRETTO
    dim = (larghezza, lunghezza)
    global finestra
    finestra = pygame.display.set_mode(dim)
    finestra.fill(NERO)
    #print("finsetra ok")

    printCsv(lista)
    readCsv()
    #per sempre stampo il qr e controllo se viene chiusa la pagina di pygame 
    while True:
        drawQR(lista, dim)
        #print("drawqr ok")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   # chiude la finsetra
                sys.exit()         #chiudo il programma  python
        pygame.display.update()

if __name__ == "__main__":
    main()