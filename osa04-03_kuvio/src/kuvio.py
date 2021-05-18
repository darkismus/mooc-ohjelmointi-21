# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen
def viiva(pituus, mjono):
    if len(mjono) == 0:
        print("*"*pituus)
    else:
        print(mjono[0]*pituus)

def kuvio(kolmiopituus, kolmiomerkki, neliopituus, neliomerkki):
    apuluku = 1
    while apuluku <= kolmiopituus:
        viiva(apuluku, kolmiomerkki)
        apuluku += 1
    apuluku = 1
    while apuluku <= neliopituus:
        viiva(kolmiopituus, neliomerkki)
        apuluku += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kuvio(5, "x", 2, "o")
    kuvio(5, "X", 3, "*")