def paieska(vardas, adresai):
    #ToDo: atlikti paieška pagal vardą ir gražinti adresą
    return "adresas nerastas"

def txt_eilute(vardas):
    return vardas.split(" ")[0]

def csv_eilute(adresas):
    el = adresas.split(";")
    return el[0], el[1], el[2]

def failo_nuskaitymas(failo_pavadinimas):
    duomenys = []  
    f = open(failo_pavadinimas)
    for eilute in f.readlines():
        duomenys.append(eilute)
    f.close()
    return duomenys

# ToDo: Failo skaitymas    
vardai_raw = failo_nuskaitymas("list.txt")
adresai_raw = failo_nuskaitymas("addresses.csv")

# ToDo: Duomenų interpretavimas
vardai = []
adresai = []
for vardas in vardai_raw:
    vardai.append(txt_eilute(vardas))

for adresas in adresai_raw:
    adresai.append(csv_eilute(adresas))

# Paieška pagal vardą
for vardas in vardai:
    print(f"{vardas} gyvena {paieska(vardas, adresai)}")


# ToDo: Rezultato įrašymas į failą


