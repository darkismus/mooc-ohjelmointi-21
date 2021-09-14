# tee ratkaisu tänne


def kertaa_kymmenen(alku: int, loppu: int):
    sanakirja = {}

    while True:
        if alku <= loppu:
            sanakirja[alku] = alku*10
        else:
            break
        alku += 1


    return sanakirja




if __name__ == "__main__":
    d = kertaa_kymmenen(3, 6)
    print(d)