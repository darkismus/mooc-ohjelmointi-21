# tee ratkaisu tänne

def ilman_vokaaleja(merkkijono : str):
    for i in merkkijono:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "u" or i == "y" or i == "å" or i == "ä" or i == "ö":
            merkkijono = merkkijono.replace(i, "")
    return merkkijono

if __name__ == "__main__":
    mjono = "tämä on esimerkki"
    print(ilman_vokaaleja(mjono))
