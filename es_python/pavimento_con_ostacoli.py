import pygame   #installata da noi
import sys  #nativa = preinstallata

NERO = (0,0,0)
BIANCO = (255,255,255)
ROSSO = (255, 0, 0)

def drawGrid():
    
    #partendo da zero, fino a dimensioni[0], ogni dimensioni
    for x in range(0,dimensioni[0]-1, dim_quadretto):
        for y in range(0,dimensioni[1]-1, dim_quadretto):
            #print(f"x: {x} y: {y}")
            # se la casella è un ostacolo
            if field[int(y // dim_quadretto)][int(x // dim_quadretto)] == 0:        
                
                ostacolo = pygame.Rect(x,y, dim_quadretto, dim_quadretto)
                pygame.draw.rect(finestra, ROSSO, ostacolo)

            else:

                # pastrella diventa un rettangolo di coordinate e dimensioni
                piastrella = pygame.Rect(x, y, dim_quadretto, dim_quadretto)
                #disegno la piastrella
                pygame.draw.rect(finestra, BIANCO, piastrella, 1 )
    
    
def main():
    pygame.init()

    global field
    field = [[0, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1],
            [0, 1, 0, 1, 1, 1],
            [1, 1, 0, 1, 0, 1],
            [1, 1, 0, 1, 1, 1]]

    global dim_quadretto
    dim_quadretto = 50 

    lunghezza = len(field) * dim_quadretto
    larghezza = len(field[0]) * dim_quadretto

    #print(len(field))
    #print(f"lunghezza {lunghezza}")
    #print(f"larghezza {larghezza}")

    global dimensioni
    dimensioni = (larghezza, lunghezza)

    global finestra 
    finestra = pygame.display.set_mode(dimensioni)
    finestra.fill(NERO)
    
    while True:
        drawGrid()

        #ciclo for gestione eventi

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   # chiude la finsetra
                sys.exit()         #chiudo il programma  python

        pygame.display.update()

if __name__ == "__main__":
    main()

