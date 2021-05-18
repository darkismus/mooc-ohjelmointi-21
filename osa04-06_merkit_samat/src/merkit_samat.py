# tee ratkaisu tänne

def samat(mjono, indeksi1, indeksi2):
    if len(mjono) -1 < indeksi1 or len(mjono) -1 < indeksi2:
        return False
    
    if mjono[indeksi1] == mjono[indeksi2]:
        return True
    else:
        return False

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    print(samat("koodari", 1, 2)) 