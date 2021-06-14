# tee ratkaisu tänne

def poista_isot(lista : list):
    apulista = []
    for i in lista:
        if i.isupper() == False:
            apulista.append(i)
    return apulista



if __name__ == "__main__":
    lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
    karsittu_lista = poista_isot(lista)
    print(karsittu_lista)