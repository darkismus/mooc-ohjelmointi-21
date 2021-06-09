# tee ratkaisu tänne



def uniikit(lista : list):
    lista.sort()
    vastaus_lista = []
    apumuuttuja = 0
    for i in lista:
        if i != apumuuttuja:
            vastaus_lista.append(i)
        apumuuttuja = i
    return vastaus_lista





if __name__ == "__main__":
    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(lista)) # [1, 2, 3]