
lista = []

value = 0

while int(value) != -1:
    value = input("inserire gli elementi della lista: ")
    lista.append(int(value))

lista.remove(-1)

for indice,elemento in enumerate(lista):
    for indice2,elemento2 in enumerate(lista):
        if int(indice) == indice and int(indice2) == indice2:
            if lista[indice2] > lista[indice]:
                lista[indice],lista[indice2] = lista[indice2],lista[indice]

print(f"{lista}")

    