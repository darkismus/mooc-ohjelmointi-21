# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti

def viiva(pituus, mjono):
    if len(mjono) == 0:
        print("*"*pituus)
    else:
        print(mjono[0]*pituus)

if __name__ == "__main__":
    viiva(5, "x")
    viiva(5, "")
