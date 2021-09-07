# tee ratkaisu tänne

def lisays(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int):
    sudoku[rivi_nro][sarake_nro] = luku

def tulosta(sudoku: list):
    vali = 0
    alekkain = 0
    for i in sudoku:
        # print(i)
        for j in i:
            if j != 0:
                print(f"{j} ", end="")
            else:
                print("_ ", end="")
            vali += 1
            if vali % 3 == 0:
                print(" ", end="")
        alekkain += 1
        if alekkain % 3 == 0:
            print()
        print()


if __name__ == "__main__":

    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    tulosta(sudoku)
    lisays(sudoku, 0, 0, 2)
    lisays(sudoku, 1, 2, 7)
    lisays(sudoku, 5, 7, 3)
    print()
    print("Kolme numeroa lisätty:")
    print()
    tulosta(sudoku)