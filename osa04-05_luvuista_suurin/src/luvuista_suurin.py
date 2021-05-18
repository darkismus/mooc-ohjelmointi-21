# tee ratkaisu tänne

def luvuista_suurin(eka, toka, kolmas):
    if eka >= toka and eka >= kolmas:
        return eka
    elif toka >= eka and toka >= kolmas:
        return toka
    elif kolmas >= eka and kolmas >= toka:
        return kolmas

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    suurin = luvuista_suurin(1, 1, 1)
    print(suurin)