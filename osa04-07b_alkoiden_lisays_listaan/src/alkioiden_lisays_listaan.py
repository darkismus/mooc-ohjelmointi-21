# Kirjoita ratkaisu tähän
montako = int(input("Kuinka monta lukua: "))
apuluku = 1
lista = []

while apuluku <= montako:
    lista.append(int(input(f"Anna luku {apuluku}: ")))
    apuluku += 1

print(lista)
