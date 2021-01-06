#SNAKE
import turtle
import random
import time

larghezzaCampo = 260
lunghezzaCampo = 260
contMeleMangiate = 0

#finestra di gioco
wnd = turtle.Screen()
wnd.title("My snake")
wnd.bgcolor("green")
wnd.setup(width=lunghezzaCampo * 2, height = larghezzaCampo * 2)

#snake
direction = "start"
sn = turtle.Turtle()
sn.shape("square")
sn.color("dark blue")
sn.penup()          # penup mi permette di non far disegnare la turtle 
sn.speed(0)         #speed 0 mi permette di eliminare la transizione tra cambio di posizione e l'altro
parti = [] 

#funzione che genera la mela ogni volta che viene mangiata
def generaMela():
    x = y = 1
    while x % 20 != 0: 
        x = random.randint(-(lunghezzaCampo- 10), lunghezzaCampo- 10)
    while y % 20 != 0: 
        y = random.randint(-(larghezzaCampo- 10), larghezzaCampo- 10)
    food.goto(x,y)

#cibo
food = turtle.Turtle()
food.penup()
generaMela()
food.shape("square")
food.color("red")
food.speed(0)

#le funzioni che vengono utilizzate per il movimento 
#per ogni direzione controllo che non si proceda nella direzione opposta
def up():
    global direction
    if  direction != "down":
        direction =  "up"
def down():
    global direction
    if  direction != "up":
        direction = "down"
def right():
    global direction
    if  direction != "left":
        direction = "right"
def left():
    global direction
    if  direction != "right":
        direction = "left"

#funzione per gestire il movimento effettivo del serpente
def move():
    global direction
    if direction == "up":
        sn.sety(sn.ycor() + 20)

    if direction == "down":
        sn.sety(sn.ycor() - 20)

    if direction == "left":
        sn.setx(sn.xcor() - 20)

    if direction == "right":
        sn.setx(sn.xcor() + 20)

#quando si perde si resetta il gioco
def perso():
    #resetto il gioco
        wnd.bgcolor("black")
        sn.hideturtle()
        sn.goto(0,0)
        food.hideturtle()
        sn.color("white")
        #faccio comparire una scritta al centro col font liberation serif di grandezza 30 e in grassetto
        sn.write("HAI PERSO \n", False, align="center", font=("Liberation Serif", 30, "bold"))
        sn.write(f"score : {contMeleMangiate}", False, align="center", font=("Liberation Serif", 30, "bold"))
        
        #per tutte le parti dello snake lo nascondo
        for indice in range(len(parti)-1, 0, -1):
            parti[indice].hideturtle()
            #nascondo anche la testa dello snake
        if contMeleMangiate > 0:
            parti[0].hideturtle()

#rimango in attesa di una qualsiasi pressione dei tasti di movimento
wnd.listen()
wnd.onkeypress(up, "w")
wnd.onkeypress(down, "s")
wnd.onkeypress(left, "a")
wnd.onkeypress(right, "d")

#setto un timer per far aumentare la velocità dello snake tutte le volte
timer = 0.30

#ciclo pricipale
while True:
    #aggiorno la pagina
    wnd.update()

    #se il serpente va troppo vicino ai bordi
    if(sn.xcor() > lunghezzaCampo- 10 or sn.xcor() < -(lunghezzaCampo- 10) or sn.ycor() < -(lunghezzaCampo- 10) or sn.ycor() > lunghezzaCampo- 10):
        perso()

    #MANGIATO
    if sn.distance(food) < 20:
        #riposiziono la mela
        generaMela()

        #aggiungo un nuovo quadrato alla coda
        pezzoCoda = turtle.Turtle()
        pezzoCoda.color("green")
        pezzoCoda.shape("square")
        pezzoCoda.penup()
        pezzoCoda.speed(0)
        pezzoCoda.color("blue")    
        parti.append(pezzoCoda)
        contMeleMangiate += 1
        if float(timer) > 0:
            timer -= 0.02

    #per tutti i pezzi della coda aggiorno la posizione perndendo la posizione della casella prima

    #range da len(parti)-1 a 0, ma andando a ritroso
    for indice in range(len(parti)-1, 0, -1):
        scalax = parti[indice-1].xcor()
        scalay = parti[indice-1].ycor()
        parti[indice].goto(scalax, scalay)

    #gestisco il primo pezzo di coda subito dopo la testa (il for non lo conta)
    if len(parti)>0:
        x = sn.xcor()
        y = sn.ycor()
        parti[0].goto(x,y)

    #muovo lo snake
    move()

    # per tutti i pezzi della coda controllo che la testa non stia sopra un altra parte di coda
    for pezzoCoda in parti:
        if pezzoCoda.distance(sn) < 20:
            #altrimenti cambio colore del pezzo di coda in questione, aspetto un secondo e faccio vedere la schermata di perso
            pezzoCoda.color("yellow")
            time.sleep(1)
            perso()


    time.sleep(float(timer))

wnd.mainloop()