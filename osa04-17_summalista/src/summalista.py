# tee ratkaisu tänne



def summa(eka : list, toka : list):
    apumuuttuja = 0
    summalista = []
    for i in eka:
        summalista.append(i + toka[apumuuttuja])
        apumuuttuja += 1
    return summalista



if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(summa(a, b)) # [8, 10, 12]