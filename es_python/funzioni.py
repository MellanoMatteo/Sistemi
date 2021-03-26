def somma(a,b): 
    return a+b

def moltiplicazione(a,b):
    return a*b
#dizionari di funzioni
dizionario_funzioni = {0: somma, 1: moltiplicazione}

def main():
    val_utente = int(input("0 per sommare, 1 per moltiplicare: "))
    a = int(input("primo numero: "))
    b = int(input("Secondo numero: "))
    try:
        x =dizionario_funzioni[val_utente](a,b)  #dizionario_funzioni[val_utente] è la funzione che è salvata nel dizionario, e dopo gli passo i parametri
        print(x)
    except:
        print("hai inserito una chiave sbagliata")
    
if __name__ == "__main__":
    main()

