# tee ratkaisu tänne


def eniten_kirjainta(merkkijono : str):
    eniten = 0
    kirjain = ""
    for i in merkkijono:
        if eniten <= merkkijono.count(i) or kirjain == "":
            eniten = merkkijono.count(i)
            kirjain = i
    return kirjain


if __name__ == "__main__":
    mjono = "abcbdbe"
    print(eniten_kirjainta(mjono))

    toinen_jono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(toinen_jono))    