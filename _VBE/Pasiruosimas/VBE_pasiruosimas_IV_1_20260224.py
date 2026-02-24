# paieška / 
def paieska(vardas, adresai):
    # TODO: parašyti funkcijos logika
    return "adresas nerastas"

# tekstinės eilutės apdorojimas
def skaityti_txt_eilute(eilute):
    return eilute.split()[0]

# csv eilutės apdorojimas
def skaityti_csv_eilute(eilute):
    return eilute.split(";")

# Failo nuskaitymas
def failo_nuskaitymas(failo_pavadinimas, failo_tipas):
    duomenys = []

    f = open(failo_pavadinimas)
    for eilute in f.readlines():
        if failo_tipas == "txt":
            duomenys.append(skaityti_txt_eilute(eilute))
        elif failo_tipas == "csv":
            duomenys.append(skaityti_csv_eilute(eilute))
        else:
            print("Nežinomas failo tipas")
    f.close()
    return duomenys


vardai = failo_nuskaitymas("list.txt", "txt")
adresai = failo_nuskaitymas("addresses.csv", "csv")


for vardas in vardai:
    adresas = paieska(vardas, adresai)
    print(f"{vardas} gyvena adresu: {adresas}")





# rezultato saugojimas į failą