# Kirjoita ratkaisu tähän

def valmis_lista():
    luvut = ['15 87', '10 55', '11 40', '4 17']
    return luvut

def lue_kayttajalta():
    lista = []
    while True:
        luvut = input("Koepisteet ja harjoitusten määrä:")
        if luvut == "":
            break
        lista.append(luvut)
    return lista

def siivoa_syotteet(lista : list):
    siivottu_lista = []
    
    for i in lista:
        siivottu_lista.append(i.split())
    return siivottu_lista

def pisteet(lista : list):
    pisteet = []

    for i in lista:
        hpisteet = muotoile_harjoituspisteet(int(i[1])) 
        apulista = []
        if int(i[0]) < 10:
            apulista.append(0)
            apulista.append(int(i[0]) + hpisteet)
        elif int(i[0]) + hpisteet < 15:
            apulista.append(0)
            apulista.append(int(i[0]) + hpisteet)
        else:
            apulista.append(1)
            apulista.append(int(i[0]) + hpisteet)
        pisteet.append(apulista)

    return pisteet

def muotoile_harjoituspisteet(harjoituspisteet : int):
    todelliset_pisteet = 0
    if harjoituspisteet < 10:
        todelliset_pisteet = 0
    elif harjoituspisteet < 20:
        todelliset_pisteet = 1
    elif harjoituspisteet < 30:
        todelliset_pisteet = 2
    elif harjoituspisteet < 40:
        todelliset_pisteet = 3
    elif harjoituspisteet < 50:
        todelliset_pisteet = 4
    elif harjoituspisteet < 60:
        todelliset_pisteet = 5
    elif harjoituspisteet < 70:
        todelliset_pisteet = 6
    elif harjoituspisteet < 80:
        todelliset_pisteet = 7
    elif harjoituspisteet < 90:
        todelliset_pisteet = 8
    elif harjoituspisteet < 100:
        todelliset_pisteet = 9
    elif harjoituspisteet >= 100:
        todelliset_pisteet = 10
    
    return todelliset_pisteet

def tulosta(pisteytys_lista : list):
    print("Tilasto:")
    ka = keskiarvo(pisteytys_lista)
    print(f"Pisteiden keskiarvo: {ka}")
    hyvaksymiset = hyvaksytyt(pisteytys_lista)
    print(f"Hyväksymisprosentti: {hyvaksymiset:.1f}")
    print("Arvosanajakauma: ")
    arvosanalista = luo_arvosana_lista(pisteytys_lista)

    #print(arvosanalista)
    apumuuttuja = 5

    while apumuuttuja >= 0:
        print(f"  {apumuuttuja}: ",end="")
        for i in arvosanalista:
            if i == apumuuttuja:
                print("*",end="")
        print("")
        apumuuttuja -= 1
    
def keskiarvo(pisteet_lista : list):
    summa = 0
    ka = 0
    for i in pisteet_lista:
        summa += i[1]
    ka = summa / len(pisteet_lista)

    return ka

def hyvaksytyt(hyvaksymis_lista : list):
    montako = 0
    for i in hyvaksymis_lista:
        if i[0]:
            montako += 1
    
    return montako / len(hyvaksymis_lista) * 100

def luo_arvosana_lista(pisteytys_lista):
    arvosanalista = []

    for i in pisteytys_lista:
        if i[0]:
            arvosanalista.append(anna_arvosana(i[1]))
        else:
            arvosanalista.append(0)
        arvosanalista.sort(reverse=True)
    return arvosanalista

def anna_arvosana(yhteispisteet : int):

    arvosana = 0
    if yhteispisteet >= 0 and yhteispisteet< 15:
        arvosana = 0
    elif yhteispisteet >= 15 and yhteispisteet < 18:
        arvosana = 1
    elif yhteispisteet >= 18 and yhteispisteet < 21:
        arvosana = 2
    elif yhteispisteet >= 21 and yhteispisteet < 24:
        arvosana = 3
    elif yhteispisteet >= 24 and yhteispisteet < 28:
        arvosana = 4
    elif yhteispisteet >= 28 and yhteispisteet <= 30:
        arvosana = 5

    # Oikeastaan sortattu lista olisi JEES JEES!
    return arvosana


# syotteet = valmis_lista()

syotteet = lue_kayttajalta()

# syotteet = ["20 100"]

#print(syotteet)

syotteet = siivoa_syotteet(syotteet)

#print(syotteet)

pisteytys = pisteet(syotteet)

#print(pisteytys)

tulosta(pisteytys)

# for i in pisteytys:
#    print(f"{i[0]},{i[1]}")



