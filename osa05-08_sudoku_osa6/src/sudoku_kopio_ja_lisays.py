# tee ratkaisu tänne

def kopioi_ja_lisaa(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int):
    # kopio = sudoku[:]
    kopio = []
    tokakopio = []
    for alkio in sudoku:
        for i in alkio:
            tokakopio.append(i)
        kopio.append(tokakopio)
        tokakopio = []
    kopio[rivi_nro][sarake_nro] = luku
    return kopio


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

    kopio = kopioi_ja_lisaa(sudoku, 0, 0, 2)
    print("Alkuperäinen:")
    tulosta(sudoku)
    print()
    print("Kopio:")
    tulosta(kopio)