# tee ratkaisu tänne
def pisimmat(lista : list):
    pisin = 0
    vastaus_lista = []
    for i in lista:
        if pisin < len(i):
            vastaus_lista = []
            vastaus_lista.append(i)
            pisin = len(i)
        elif pisin == len(i):
            vastaus_lista.append(i)
    return vastaus_lista


if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs", "seitsemä1", "seitsemäs"]

    tulos = pisimmat(lista)
    print(tulos) # ['seitsemäs']