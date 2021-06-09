# tee ratkaisu tänne
def lyhin(lista : list):
    lyhin = len(lista[0])
    sana = lista[0]
    for i in lista:
        if lyhin > len(i):
            lyhin = len(i)
            sana = i
    return sana


if __name__ == "__main__":
    lista = ['Serafiina', 'Gandalf', 'Harry', 'Väiski']

    tulos = lyhin(lista)
    print(tulos)