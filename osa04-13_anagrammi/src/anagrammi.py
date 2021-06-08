# Tee ratkaisu tänne

def anagrammi(sana1, sana2):
    if sorted(sana1) == sorted(sana2):
        return True
    else:
        return False

if __name__ == "__main__":
    print(anagrammi("talo", "tola"))
    print(anagrammi("tammi", "mitta"))