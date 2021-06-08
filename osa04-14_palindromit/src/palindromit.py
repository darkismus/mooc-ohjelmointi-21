# tee ratkaisu tänne
# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
# if __name__ == "__main__":
# sisälle!

def palindromi(sana):
    palindromi = False
    viimeinen = -1
    for i in sana:

        if i == sana[viimeinen]:
            palindromi = True
        else:
            palindromi = False
            return palindromi
        viimeinen -= 1
    
    return palindromi




while True:
    sana = input("Anna sana: ")
    if palindromi(sana):
        print(f"{sana} on palindromi!")
        break
    else:
        print("ei ollut palindromi")
    




if __name__ == "__main__":
    print("ankka")