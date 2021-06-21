# tee ratkaisu tänne


def laske_alkiot(matriisi : list, alkio : int):
    montako = 0
    for i in range(len(matriisi)):
        for j in range(len(matriisi[i])):
            if matriisi[i][j] == alkio:
                montako += 1
    return montako


if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1))
    laske_alkiot([[1, 2]], 1)