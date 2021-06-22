# tee ratkaisu tänne


def rivi_oikein2(sudoku : list, rivi_nro : int):
    tupla = 0
    sortattu = sorted(sudoku[rivi_nro])
    for i in range(1,10):
        for j in range(len(sortattu)):
            if sortattu[j] == 0:
                continue
            if tupla == sortattu[j]:
                # print(f"{sortattu} tupla on {tupla} i on {i} j on {j}")
                return False
            tupla = sortattu[j]
    return True

def rivi_oikein(sudoku: list, rivi: int):
    luvut = []
    for luku in sudoku[rivi]:
        if luku > 0 and luku in luvut:
            return False
        luvut.append(luku)
 
    return True

def sarake_oikein(sudoku : list, sarake_nro : int):
    luvut = []

    for luku in sudoku:
        if luku[sarake_nro] > 0 and luku[sarake_nro] in luvut:
            return False
        luvut.append(luku[sarake_nro])
    return True   

def nelio_oikein(sudoku : list, rivi_nro : int, sarake_nro : int):
    luvut = []

    for luku in range(rivi_nro, rivi_nro+3):
        for luku2 in range(sarake_nro, sarake_nro+3):
            if sudoku[luku][luku2] > 0 and sudoku[luku][luku2] in luvut:
                return False
            luvut.append(sudoku[luku][luku2])
    return True

def sudoku_oikein(sudoku : list):
    rivit = True
    sarakkeet = True
    neliot = True
    for i in range(0, 9):
        rivit = rivi_oikein(sudoku, i)
        sarakkeet = sarake_oikein(sudoku, i)
        if rivit == False or sarakkeet == False:
            # print(f"monesko {i} ja rivit {rivit} sarakkeet {sarakkeet}")
            return False
        if i == 0 or i == 3 or i == 6:
            for j in range(0, 7, 3):
                neliot = nelio_oikein(sudoku, i, j)
                if neliot == False:
                    # print(f"j: {j} ja i: {i}")
                    return False
    return True
        
        



if __name__ == "__main__":
    

    sudoku3 = [
        [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
        [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
        [ 0, 5, 1, 6, 0, 0, 8, 3, 9 ],
        [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
        [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
        [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
        [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
        [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
        [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ]
    ]
    print(sudoku_oikein(sudoku3))

    sudoku = [
        [ 3, 4, 0, 5, 2, 6, 1, 0, 0 ],
        [ 5, 2, 0, 8, 1, 9, 0, 3, 0 ],
        [ 0, 0, 0, 0, 4, 7, 0, 5, 0 ],
        [ 0, 0, 3, 0, 0, 0, 0, 0, 0 ],
        [ 0, 9, 8, 0, 0, 3, 6, 4, 5 ],
        [ 0, 6, 5, 0, 9, 8, 7, 1, 3 ],
        [ 7, 0, 0, 0, 8, 2, 3, 0, 0 ],
        [ 9, 0, 0, 7, 5, 0, 8, 6, 0 ],
        [ 0, 8, 2, 9, 3, 1, 0, 0, 4 ],
    ]
    print(sudoku_oikein(sudoku))