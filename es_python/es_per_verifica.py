
import sys
import pygame
import random
import csv

WIDTH = 500
HEIGHT = 600

TIME = 60
BLU = (0,0,255)
ROSSO = (200,150,0)

size = (WIDTH,HEIGHT)

screen = pygame.display.set_mode(size)

def isPassato(dic, newCord):
    for key, value in dic.items():
        if(value == newCord):
            print(value)
            return

def generatePath():
    dic= {}
    x = WIDTH // 2
    y = HEIGHT // 2
    dic[0] = [x,y]
    for key in range(1,TIME):
        rand = random.randint(0,3)
        if rand == 0:
            x += 10
        elif rand == 1: 
            x -= 10
        elif rand == 2:
            y += 10
        elif rand == 3:
            y -= 10
        
        newCord = [x,y]
        isPassato(dic, newCord)
        dic[key] = newCord
        
    return dic

def drawPath(dic):
    for i in range(1,TIME):
        pygame.draw.line(screen,BLU,  dic[i-1], dic[i])
        pygame.display.update()

def printCsv():

    with open("file.csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        for chiave,valore in path.items():
            lista = [chiave, valore[0], valore[1]]
            csvwriter.writerow(lista)

def main():

    pygame.init()
    screen.fill(ROSSO)

    global path
    path = {}
    path = generatePath()
    printCsv()

    drawPath(path)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        

if __name__ == "__main__":
    main()