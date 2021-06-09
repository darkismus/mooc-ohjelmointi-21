# tee ratkaisu tänne

def pisimman_pituus(lista : list):
    pisin = 0
    for i in lista:
        if pisin < len(i):
            pisin = len(i)
    return pisin


if __name__ == "__main__":
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]

    tulos = pisimman_pituus(lista)
    print(tulos)