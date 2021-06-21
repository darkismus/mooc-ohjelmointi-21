# tee ratkaisu tänne


def kumpi_voitti(pelilauta : list):
    pelaaja1 = 0
    pelaaja2 = 0

    for i in range(len(pelilauta)):
        for j in range(len(pelilauta[i])):
            if pelilauta[i][j] == 1:
                pelaaja1 += 1
            elif pelilauta[i][j] == 2:
                pelaaja2 += 1
    if pelaaja1 > pelaaja2:
        return 1
    elif pelaaja1 < pelaaja2:
        return 2
    else:
        return 0

if __name__ == "__main__":
    kumpi_voitti([[1]])
    kumpi_voitti([[1, 2, 1], [0, 0, 1], [2, 1, 0]])