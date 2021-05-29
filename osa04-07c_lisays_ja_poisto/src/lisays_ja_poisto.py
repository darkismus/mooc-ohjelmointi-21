# Kirjoita ratkaisu tähän

lista = []
apuluku = 0
print(f"Lista on nyt {lista}")

while True:
    mjono = input("(l)isää, (p)oista vai e(x)it: ")
    if mjono == "x":
        print("Moi!")
        break
    elif mjono == "l":
        apuluku += 1
        lista.append(apuluku)
        print(f"Lista on nyt {lista}")
    elif mjono == "p":
        apuluku -= 1
        lista.pop(len(lista)-1)
        print(f"Lista on nyt {lista}")

