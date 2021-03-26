from turtle import * #importo tutti i file da turtle1

pen = Turtle()      #istanzio un oggetto di tipo Turtle con nome pen
# bordo = Turtle()
window = Screen()   #istanzio un oggetto di tipo Screen con nome window

lung = 50

def controllo():
    risultato = 0
    #controllo prima i lati
    if (pen.ycor() + lung) > window.window_height() / 2:            #controllo verso l'alto
        risultato = 1
    if (pen.ycor() - lung) < -1 * window.window_height() / 2:       #controllo verso il basso
        risultato = 2
    if (pen.xcor() + lung) > window.window_width() / 2:             #controllo verso destra 
        risultato = 3
    if (pen.xcor() - lung) < -1 * window.window_width() / 2:        #controllo verso sinistraa
        risultato = 4

    #controllo gli angoli
    if (pen.ycor() + lung) > window.window_height() / 2 and  (pen.xcor() - lung) < -1 * window.window_width() / 2:           #alto a sinistra 
        risultato = 5
    if (pen.ycor() + lung) > window.window_height() / 2 and  (pen.xcor() + lung) > window.window_width() / 2:                #alto a destra
        risultato = 6
    if (pen.ycor() - lung) < -1 * window.window_height() / 2 and (pen.xcor() + lung) > window.window_width() / 2:            #basso a destra 
        risultato = 7
    if (pen.ycor() - lung) < -1 * window.window_height() / 2 and (pen.xcor() - lung) < -1 * window.window_width() / 2:       #basso a sinistra 
        risultato = 8
    return risultato


def avanti():
    if controllo() != 1 and controllo() != 5 and controllo() != 6: 
        pen.setheading(90)
        pen.forward(lung)
        #print(controllo())

def indietro():
    if controllo() != 2 and controllo() != 7 and controllo() != 8: 
        pen.setheading(270)
        pen.forward(lung)
        #print(controllo())

def sinistra():
    if controllo() != 4 and controllo() != 5 and controllo() != 8: 
        pen.setheading(180)
        pen.forward(lung)
        #print(controllo())

def destra():
    if controllo() != 3 and controllo() != 6 and controllo() != 7: 
        pen.setheading(0)
        pen.forward(lung) 
        #print(controllo())

window.title("turtle")

""" definisco le coordinate di partenza della turtle che colorerà il bordo
bordo.color('red')

contlungy = 0
while contlungy < window.window_height() / 2: 
    contlungy = contlungy + 50
contlungx = 0  
while contlungx < window.window_width() / 2:  
    contlungx = contlungx + 50

bordo.setx(-contlungx)
bordo.sety(contlungy)
bordo.setheading(90)

print (bordo.position())

while bordo.xcor() < window.window_width() / 2 :
    bordo.forward(lung)
    print (bordo.position())
while bordo.ycor() > -1 * window.window_height() / 2: 
    bordo.forward(lung)
while bordo.xcor() > -1 * window.window_width() / 2:
    bordo.forward(lung)
while bordo.ycor() < window.window_height() / 2: 
    bordo.forward(lung) """


window.listen()
window.onkeypress(avanti, "w")
window.onkeypress(destra, "d")
window.onkeypress(sinistra, "a")
window.onkeypress(indietro, "s")

window.mainloop()