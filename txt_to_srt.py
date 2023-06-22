# program for convert txt to srt

x = 0
spisok = []
spisokNomber = []
spisokTime = []
spisokSlov = []
itog = []

with open("1.txt", "r") as file1:
    for line in file1:
        spisok.append(line)
        nomber = int(spisok.index(line)) + 1
        spisokNomber.append(nomber)

        if nomber % 2 == 0:
            print('Четное число')
            spisokSlov.append(line)

        else:
            print('Нечентное число')
            spisokTime.append(line.split())

try:
    while True:
        num = spisokNomber[x]
        itog.append(num)

        strokaTime = "00:" + str(spisokTime[x])[2:-2] + ",001" + " --> " + "00:" + str(spisokTime[x + 1])[2:-2] + ",001"
        itog.append(strokaTime)

        slova = str(spisokSlov[x])
        itog.append(slova)

        x = x + 1

except:
    itog = itog[:-1]
    print("Конец!")

print(itog)

f = open("777.srt", 'w')
for item in itog:
    f.write("%s\n" % item)
