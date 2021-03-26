#parametri di default in input alle funzioni

#stampa è un valore dato di default alla funzione che può anche non essere salvato
def fun(lista_numeri = [10,11], stampa = False):
    #compressione di liste
    lista_quadrati = [x*x for x in lista_numeri]
    if stampa:
        print(lista_quadrati)
    return lista_quadrati

print(fun(stampa = True, lista_numeri=[12,13]))