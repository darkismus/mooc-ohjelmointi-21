# tee ratkaisu tänne

def joulukuusi(koko):
    print("joulukuusi!")
    rivi = "*"
    loppu = " " * (koko -1) + rivi

    while koko > 0:
        print(" " * (koko -1) + rivi)
        rivi += "**"
        koko -= 1
    print(loppu)


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    joulukuusi(5)