# Kirjoita ratkaisu tähän

lista = []


while True:
    luku = int(input("Anna luku: "))
    if luku == 0:
        print("Moi!")
        break
    lista.append(luku)
    print(f"Lista: {lista}")
    print(f"Järjestettynä: {sorted(lista)}")