# tee ratkaisu tänne


def kaikki_vaarinpain(lista : list):
    apulista = []
    for i in lista:
        apulista.append(i[::-1])
    
    
    return apulista[::-1]





if __name__ == "__main__":
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)