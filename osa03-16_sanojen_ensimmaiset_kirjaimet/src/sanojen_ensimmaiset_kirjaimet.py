# Kirjoita ratkaisu tähän
lause = input("Anna lause: ")
apuluku = 0

print(lause[0])
while apuluku < len(lause):
    kohta = lause.find(" ")
    apuluku = kohta+1
    print(lause[apuluku])
    lause = lause[apuluku:]
    apuluku += 1
    print(apuluku)