
#controllare che le parentesi all'interno della stringa siano state chiuse tutte correttamente

def push_(pila, elemento):
    pila.append(elemento)



def pop_(pila):
    return pila.pop()

def main():
    str_parentesi = input("inserire la stringa con le parentesi da controllare")
    pila = []

    #leggo tutti gli elementi all'interno della stringa e li salvo nella pila dedicata
    for elemento in str_parentesi:
        if (elemento == "(") or (elemento == ")") or (elemento == "[") or (elemento == "]") or (elemento == "{") or (elemento == "}"):
           push_(pila, elemento)

    #controllo che per tutte le parentesi aperte ci sia la corrispettiva chiusa
    verifica_parentesi = 0
    for elemento in pila:
        if len(pila)  % 2 == 0:
            if elemento == "(":
                ricerca_parentesi(")", pila)
            if elemento == "[":
                ricerca_parentesi("]", pila)
            if elemento == "{":
                ricerca_parentesi("}", pila)
        pop_(elemento)
    
    #il contatore deve essere la meta esatta delle parentesi
    if len(pila) == 0:
        print("la stringa è valida")
    else:
        print("la stringa non è valida")

            
        
def ricerca_parentesi(par_aperta, pila):
    for el in pila:
        if par_aperta is el:
            pop_(el)




if __name__ == "__main__":
    main()
