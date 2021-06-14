# tee ratkaisu tänne

def pisin_naapurijono(lista : list):
    pisin = 0
    nykyinen = 1
    apumuuttuja = 0
    for i in lista:
        if apumuuttuja+1 < len(lista) and (i == (lista[apumuuttuja+1]+1) or i == (lista[apumuuttuja+1]-1)):
            nykyinen += 1
        else:
            if pisin < nykyinen:
                pisin = nykyinen
            nykyinen = 1
        apumuuttuja += 1
    return pisin



if __name__ == "__main__":
    lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(pisin_naapurijono(lista))

c = "moi kaikki".count("i ")
print(c)