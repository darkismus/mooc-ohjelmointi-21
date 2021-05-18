# tee ratkaisu tänne

def eka_sana(lause):
    apuluku = 0
    sana = ""

    while lause[apuluku] != " ":
        sana += lause[apuluku]
        apuluku += 1
    return sana

def toka_sana(lause):
    apuluku = 0
    sana = ""

    while lause[apuluku] != " ":
        apuluku += 1
    
    apuluku += 1
    while lause[apuluku] != " ":
        sana += lause[apuluku]
        apuluku += 1
        if apuluku >= len(lause):
            break
    return sana

def vika_sana(lause):
    apuluku = -1
    sana = ""

    while lause[apuluku] != " ":
        apuluku -= 1

    apuluku += 1
    while apuluku < 0:
        sana += lause[apuluku]
        apuluku += 1
    return sana



# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lause = "eka toka"
    print(eka_sana(lause))
    print(toka_sana(lause)) 
    print(vika_sana(lause))