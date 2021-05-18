# kopioi edellisestä tehtävästä funktion viiva koodi tänne

def viiva(pituus, mjono):
    if len(mjono) == 0:
        print("*"*pituus)
    else:
        print(mjono[0]*pituus)

def kolmio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    apuluku = 1
    while apuluku <= koko:
        viiva(apuluku, "#")
        apuluku += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kolmio(5)
