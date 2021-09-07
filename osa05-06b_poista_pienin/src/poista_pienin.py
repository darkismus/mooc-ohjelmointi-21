# tee ratkaisu tänne


def poista_pienin(luvut : list):
    pienin = luvut[0]
    kohta = 0

    for alkio in luvut:
        if alkio < pienin:
            pienin = alkio

    luvut.remove(pienin)



if __name__ == "__main__":
    luvut = [2, 4, 6, 1, 3, 5]
    poista_pienin(luvut)
    print(luvut)