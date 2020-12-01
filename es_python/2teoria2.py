#inserire dei valori dell'utente caricati su una lista 

lista = []
valore = 0
while(int(valore) != -1):
    valore = input("inerisci un valore: ")
    lista.append(int(valore))

print(lista)

#slicing di lista

lista = [23, 43, 23, 1, 5, 4, 78, -13, 232]

print(lista[4])

print(lista[2:5]) #da quello con indice due fino a quello con indice 5 escluso

print(lista[-1]) #ultimo elemento della lista

print(lista[0:-1]) #stampa dal primo all'ulitmo escluso

stringa = 'Matteo mellano'

print(stringa[0:7]) #stampa matteo

print(stringa.startswith("Matteo")) #controlla che la stringa inizi con questa passata in parentesi

a = 10
b = 20

a,b = b,a #scambia le variabili
