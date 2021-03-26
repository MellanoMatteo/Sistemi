import random
import pygame

pygame.init()

RED = (255,0,0)
ORANGE = (255,127,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
GREY = (127,127,127)
BLACK = (0,0,0)

size = (600,700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Minesweeper")

done = False

clock = pygame.time.Clock()

font = pygame.font.Font("HighlandGothicFLF.ttf",20)

mouse_state = 0
mouse_x = 0
mouse_y = 0

cColumns = 0
cRows = 0
cMines = 0

# all the gamestate
CUSTOMIZE_MATCH = -2
NOT_PLAYING = -1
AT_STAKE = 0 
LOSE = 2
WIN = 1

gameState = NOT_PLAYING

class Button():
    def __init__(self):
        self.textBoxes = {}
    
    #----Clicked In----
    def clickedIn(self,x,y,width,height):
        global mouse_state, mouse_x, mouse_y
        if mouse_state == 1 and mouse_x >= x and mouse_x <= (x + width) and mouse_y >= y and mouse_y <= (y + height):
            return True

    #----Clicked Out----
    def clickedOut(self,x,y,width,height):
        global mouse_state, mouse_x, mouse_y
        if mouse_state == 1 and mouse_x < x or mouse_state == 1 and mouse_x > (x + width) or mouse_state == 1 and mouse_y < y or mouse_state == 1 and mouse_y > (y + height):
            return True

    #----Hovering----
    def hovering(self,x,y,width,height):
        global mouse_state, mouse_x, mouse_y
        if mouse_state == 0 and mouse_x >= x and mouse_x <= (x + width) and mouse_y >= y and mouse_y <= (y + height):
            return True
    
    #----Click Button----
    def clickButton(self,x,y,width,height,normalColor,hoverColor,textFont,text,textColor,stateHolding = False,stateVariable = 0,state = 1):
        if not self.clickedIn(x,y,width,height) and not self.hovering(x,y,width,height):
            pygame.draw.rect(screen,normalColor,(x,y,width,height))

        elif self.hovering(x,y,width,height):
            pygame.draw.rect(screen,hoverColor,(x,y,width,height))

        if stateHolding == True and stateVariable == state:
            pygame.draw.rect(screen,hoverColor,(x,y,width,height))

        buttonText = textFont.render(text,True,textColor)
        buttonText_x = buttonText.get_rect().width
        buttonText_y = buttonText.get_rect().height
        screen.blit(buttonText,(((x + (width / 2)) - (buttonText_x / 2)),((y + (height / 2)) - (buttonText_y / 2))))
        if self.clickedIn(x,y,width,height):
            return True

class Tile():
    
    def __init__(self,x,y,columns,rows):
        self.columns = columns
        self.rows = rows
        self.x = (x * (size[0] / self.columns))
        self.y = (y * ((size[1] - 100) / self.rows)) + 100
        self.mine = False
        self.neighbors = 0
        self.visible = False
        self.flag = False
    
    def update(self):
        global gameState
        if gameState == AT_STAKE:
            if mouse_state == 1 and mouse_x >= self.x and mouse_x <= (self.x + (size[0] / self.columns)) and mouse_y >= self.y and mouse_y <= (self.y + ((size[1] - 100) / self.rows)):
                self.visible = True
                self.flag = False
            
            if mouse_state == 3 and mouse_x >= self.x and mouse_x <= (self.x + (size[0] / self.columns)) and mouse_y >= self.y and mouse_y <= (self.y + ((size[1] - 100) / self.rows)):
                if self.flag == False:
                    self.flag = True
                elif self.flag == True:
                    self.flag = False
            if self.visible == True and self.mine == True:
                gameState = LOSE
    
    def show(self):
        
        if self.flag == True:
            pygame.draw.rect(screen,YELLOW,(self.x,self.y,(size[0] / self.columns),((size[1] - 100) / self.rows)))

        if self.visible == True :
            if self.mine == False :
                pygame.draw.rect(screen,GREY,(self.x,self.y,(size[0] / self.columns),((size[1] - 100) / self.rows)))
                if self.neighbors > 0:
                    text = font.render(str(self.neighbors),True,BLACK)
                    text_x = text.get_rect().width
                    text_y = text.get_rect().height
                    screen.blit(text,((self.x + ((size[0] / self.columns) / 2) - (text_x / 2)),(self.y + (((size[1] - 100) / self.rows) / 2) - (text_y / 2))))
            
            elif self.mine == True:
                pygame.draw.rect(screen,RED,(self.x,self.y,(size[0] / self.columns),((size[1] - 100) / self.rows)))
        
        pygame.draw.rect(screen,BLACK,(self.x,self.y,(size[0] / self.columns),((size[1] - 100) / self.rows)),2)

button = Button()

def infoBar():
    global gameState
    pygame.draw.rect(screen,GREY,(0,0,size[0],100))
    pygame.draw.line(screen,BLACK,(0,100),(500,100),2)
    
    if gameState == AT_STAKE:
        text = font.render("MINES: " + str(game.numMines),True,BLACK)
        text_x = text.get_rect().width
        text_y = text.get_rect().height
        screen.blit(text,((size[1] * 1 / 4 - (text_x / 2)),(50 - (text_y / 2))))

        text = font.render("FLAGS: " + str(game.numflaged),True,BLACK)
        text_x = text.get_rect().width
        text_y = text.get_rect().height
        screen.blit(text,((size[1] * 2 / 4  + (text_x / 2)),(50 - (text_y / 2))))
    elif gameState == WIN:      #win
        text = font.render("YOU  WIN",True,BLACK)
        text_x = text.get_rect().width
        text_y = text.get_rect().height
        screen.blit(text,((150 - (text_x / 2)),(50 - (text_y / 2))))
    elif gameState == LOSE:    #loose
        text = font.render("YOU  LOOSE",True,BLACK)
        text_x = text.get_rect().width
        text_y = text.get_rect().height
        screen.blit(text,((150 - (text_x / 2)),(50 - (text_y / 2))))
        
    if gameState == WIN or gameState == LOSE:
        if button.clickButton(325,25,150,50,RED,ORANGE,font,"RESET",BLACK):
            gameState = NOT_PLAYING
            game.reset(0,0,0)

def menu():
    
    global gameState

    widthButton = 100
    heightButton = 50
    counterButton = 1

    screen.fill(GREY)
    text = font.render("MINE",True,BLACK)
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((size[0] / 2 - (text_x / 2)),(100 - (text_y / 2))))

    text = font.render("SWEEPER",True,BLACK)
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((size[0] / 2 - (text_x / 2)),(150 - (text_y / 2))))

    if button.clickButton(size[0] / 2 - widthButton / 2, 250 , widthButton, heightButton, RED, ORANGE, font, "EASY", BLACK): #(size[1] / 2) + 60 * counterButton
        game.reset(10,10,15)
        gameState = AT_STAKE
        counterButton = counterButton + 1
    if button.clickButton(size[0] / 2 - widthButton / 2, 310 , widthButton, heightButton, RED, ORANGE, font, "MEDIUM", BLACK):
        game.reset(20,20,60)
        gameState = AT_STAKE
        counterButton = counterButton + 1
    if button.clickButton(size[0] / 2 - widthButton / 2, 370, widthButton, heightButton, RED, ORANGE, font, "HARD", BLACK):
        game.reset(25,25,80)
        gameState = AT_STAKE
        counterButton = counterButton + 1
    if button.clickButton(size[0] / 2 - widthButton / 2, 430, widthButton, heightButton, RED, ORANGE, font, "CUSTOM", BLACK):
        gameState = CUSTOMIZE_MATCH
    counterButton = 1

def custom():
    global cColumns, cRows, cMines, gameState
    dimChangeButton = 20
    limitRows = limitColumns = 100
    limitMines = 150

    #change columns
    text = font.render("COLUMNS: " + str(cColumns),True,BLACK)
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((size[0] / 3  - (text_x / 2)),(180 - (text_y / 2))))

    if button.clickButton(size[0] *2/ 3 ,160, dimChangeButton, dimChangeButton,RED,ORANGE,font," /\ ",BLACK):
        if cColumns < limitColumns:
            cColumns += 1
    if button.clickButton(size[0] *2/3 ,180, dimChangeButton, dimChangeButton,RED,ORANGE,font," \/ ",BLACK):
        if cColumns > 0:
            cColumns -= 1

    #change rows
    text = font.render("ROWS: " + str(cRows),True,BLACK)
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((size[0] / 3 - (text_x / 2)),(260 - (text_y / 2))))
    if button.clickButton(size[0] *2/3, 240, dimChangeButton, dimChangeButton, RED, ORANGE, font, " /\ ", BLACK):
        if cRows < limitRows:
            cRows += 1
    if button.clickButton(size[0] *2/3,260, dimChangeButton, dimChangeButton, RED, ORANGE, font, " \/ ", BLACK):
        if cRows > 0:
            cRows -= 1

    #change mines
    text = font.render("MINES: " + str(cMines),True,BLACK)
    text_x = text.get_rect().width
    text_y = text.get_rect().height
    screen.blit(text,((size[0] / 3 - (text_x / 2)),(340 - (text_y / 2))))
    
    if button.clickButton(size[0] *2/3, 320,dimChangeButton, dimChangeButton, RED, ORANGE, font, " /\ ", BLACK):
        if cMines < limitMines and cMines < (cColumns * cRows):
            cMines += 1
    if button.clickButton(size[0] *2/3, 340,dimChangeButton, dimChangeButton, RED, ORANGE, font, " \/ ", BLACK):
        if cMines > 0:
            cMines -= 1

    #start button
    widthStartButton = 100
    heightRestartButton = 60 
    if button.clickButton(size[0] / 2 - widthStartButton / 2, 390, widthStartButton, heightRestartButton, RED, ORANGE, font, "START", BLACK):
        game.reset(cColumns,cRows,cMines)
        gameState = AT_STAKE
    
class Game():

    def findneighbNum(self, y, x):
        self.neighbNum = 0
        if y > 0 and x > 0:
            if self.board[y-1][x-1].mine == True:
                self.neighbNum += 1
        if y > 0:
            if self.board[y-1][x].mine == True:
                self.neighbNum += 1
        if y > 0 and x < (self.columns - 1):
            if self.board[y-1][x+1].mine == True:
                self.neighbNum += 1
        if x > 0:
            if self.board[y][x-1].mine == True:
                self.neighbNum += 1
        if x < (self.columns - 1):
            if self.board[y][x+1].mine == True:
                self.neighbNum += 1
        if x > 0 and y < (self.rows - 1):
            if self.board[y+1][x-1].mine == True:
                self.neighbNum += 1
        if y < (self.rows - 1):
            if self.board[y+1][x].mine == True:
                self.neighbNum += 1
        if x < (self.columns - 1) and y < (self.rows - 1):
            if self.board[y+1][x+1].mine == True:
                self.neighbNum += 1
        return self.neighbNum

    def __init__(self,columns,rows,mines):
        self.columns = columns
        self.rows = rows
        self.numMines = mines
        self.board = []
        self.mines = []
        self.minenum = len(self.mines)
        self.neighbNum = 0
        self.numflaged = 0
        self.numvis = 0
        self.foundmines = 0
        
        #creating board
        for y in range(self.rows):
            self.board.append([])
            for x in range(self.columns):
                self.board[y].append(Tile(x,y,self.columns,self.rows))
        
        #placing mines
        while self.minenum < self.numMines:
            self.mineloc = [random.randrange(self.columns),random.randrange(self.rows)]
            if self.board[self.mineloc[1]][self.mineloc[0]].mine == False:
                self.mines.append(self.mineloc)
                self.board[self.mineloc[1]][self.mineloc[0]].mine = True
            self.minenum = len(self.mines)
        
        #neighbors
        for y in range(self.rows):
            for x in range(self.columns):
                self.board[y][x].neighbors = self.findneighbNum(y, x)
    
    def update(self):
        global gameState
        self.numflaged = 0
        self.numvis = 0
        self.foundmines = 0

        for y in range(self.rows):
            for x in range(self.columns):
                self.board[y][x].update()
                if self.board[y][x].neighbors == 0 and self.board[y][x].visible == True:
                    if y > 0 and x > 0:
                        self.board[y-1][x-1].visible = True
                    if y > 0:
                        self.board[y-1][x].visible = True
                    if y > 0 and x < (self.columns - 1):
                        self.board[y-1][x+1].visible = True
                    if x > 0:
                        self.board[y][x-1].visible = True
                    if x < (self.columns - 1):
                        self.board[y][x+1].visible = True
                    if x > 0 and y < (self.rows - 1):
                        self.board[y+1][x-1].visible = True
                    if y < (self.rows - 1):
                        self.board[y+1][x].visible = True
                    if x < (self.columns - 1) and y < (self.rows - 1):
                        self.board[y+1][x+1].visible = True

                if self.board[y][x].flag == True:
                    self.numflaged += 1

                if self.board[y][x].visible == True:
                    self.numvis += 1

        for mine in self.mines:
            if self.board[mine[1]][mine[0]].flag == True:
                self.foundmines += 1

        if self.numvis == ((self.columns * self.rows) - self.numMines):
            gameState = WIN
            
        if gameState == WIN or gameState == LOSE:
            for y in range(self.rows):
                for x in range(self.columns):
                    self.board[y][x].visible = True
        
    
    def render(self):
        for y in range(self.rows):
            for x in range(self.columns):
                self.board[y][x].show()
    
    def reset(self,columns,rows,mines):
        if columns != 0 and rows != 0 and mines != 0:
            self.columns = columns
            self.rows = rows
            self.numMines = mines
        self.board = []
        self.mines = []
        self.minenum = len(self.mines)
        self.neighbNum = 0
        self.numflaged = 0
        self.numvis = 0
        self.foundmines = 0
        
        #creating board
        for y in range(self.rows):
            self.board.append([])
            for x in range(self.columns):
                self.board[y].append(Tile(x,y,self.columns,self.rows))
        
        #placing mines
        while self.minenum < self.numMines:
            self.mineloc = [random.randrange(self.columns),random.randrange(self.rows)]
            if self.board[self.mineloc[1]][self.mineloc[0]].mine == False:
                self.mines.append(self.mineloc)
                self.board[self.mineloc[1]][self.mineloc[0]].mine = True
            self.minenum = len(self.mines)
        
        #neighbors
        for y in range(self.rows):
                for x in range(self.columns):
                    self.board[y][x].neighbors = self.findneighbNum( y, x) 

game = Game(5,5,5)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_state = event.button
            pygame.mouse.set_pos(mouse_x,mouse_y + 1)
        else:
            mouse_state = 0
    
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    
    screen.fill(WHITE)
    
    if gameState == NOT_PLAYING:
        menu()
    
    elif gameState == CUSTOMIZE_MATCH:
        custom()
    
    elif gameState >= AT_STAKE and gameState <= LOSE:
        infoBar()
        
        game.update()
        game.render()
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()