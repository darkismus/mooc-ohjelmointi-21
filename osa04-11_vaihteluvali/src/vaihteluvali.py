# tee ratkaisu tänne

def vaihteluvali(lista : list):
    pienin = min(lista)
    suurin = max(lista)
    vastaus = suurin - pienin
    return vastaus

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = vaihteluvali(lista) 
    print(tulos)