# tee ratkaisu tänne




def rivi_oikein(sudoku : list, rivi_nro : int):
    tupla = 0
    sortattu = sorted(sudoku[rivi_nro])
    for i in range(1,10):
        for j in range(len(sortattu)):
            if sortattu[j] == 0:
                continue
            if tupla == sortattu[j]:
                return False
            tupla = sortattu[j]
    return True        








if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(rivi_oikein(sudoku, 0))
    print(rivi_oikein(sudoku, 1))