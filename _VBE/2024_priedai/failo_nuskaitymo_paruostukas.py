neapdoroti_duomenys = []

with open("Olimpines.txt", "r") as failo_skaitymas:
    neapdoroti_duomenys = failo_skaitymas.readlines()

sportininku_rezultatai = []
sportininku_rezultatai2 = []
kiekis = int(neapdoroti_duomenys[0])

for i in range(1, kiekis + 1):
    elementai = neapdoroti_duomenys[i].split()
    vardas = elementai[0][0]
    pavarde = elementai[0][1:]
    rezultatas = float(elementai[1])
    
    # 1 variantas
    sportininku_rezultatai.append([vardas, pavarde, rezultatas])

    # 2 variantas
    sportininku_rezultatai2.append(vardas)
    sportininku_rezultatai2.append(pavarde)    
    sportininku_rezultatai2.append(rezultatas)


print(sportininku_rezultatai)
print(sportininku_rezultatai2)