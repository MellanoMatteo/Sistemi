from turtle import *

lati = int(input("inserire il numero dei lati: "))

simone = Turtle()

simone.begin_fill()
cont = lati

while(cont > 0):
    simone.forward(50)
    simone.left(360/lati)
    cont -= 1

simone.end_fill()
done()