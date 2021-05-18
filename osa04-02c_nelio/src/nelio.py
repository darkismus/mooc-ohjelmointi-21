# kopioi edellisestä tehtävästä funktion viiva koodi tänne

def viiva(pituus, mjono):
    if len(mjono) == 0:
        print("*"*pituus)
    else:
        print(mjono[0]*pituus)

def nelio(koko, merkki):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    apuluku = 0
    while apuluku < koko:
        viiva(koko, merkki)
        apuluku += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    nelio(5, "x")
