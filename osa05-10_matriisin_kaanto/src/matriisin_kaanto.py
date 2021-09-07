# tee ratkaisu tänne


def transponoi(matriisi: list):
    uusimatriisi = []
    rivi = 0
    sarake = 0

    for r in matriisi:
        uusimatriisi.append(r[:])
        
        


    for i in range(len(uusimatriisi)):
        for j in range(len(uusimatriisi[i])):
            matriisi[j][i] = uusimatriisi[i][j]





if __name__ == "__main__":
    matriisi  = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(matriisi)
    transponoi(matriisi)
    print(matriisi)