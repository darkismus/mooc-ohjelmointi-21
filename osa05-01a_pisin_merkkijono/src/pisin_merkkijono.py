# tee ratkaisu tänne

def pisin(lista : list):
    pisin_mjono = ""

    for i in lista:
        if len(pisin_mjono) < len(i):
            pisin_mjono = i
    return pisin_mjono


if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))