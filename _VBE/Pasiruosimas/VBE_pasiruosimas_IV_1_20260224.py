# paieška
def paieska(vardas, adresai):
    # TODO: parašyti funkcijos logika
    return "adresas nerastas\n"

# tekstinės eilutės apdorojimas
def skaityti_txt_eilute(eilute):
    # TODO: ieskoti ne tik pagal vardą, bet pagal vardą pavardę
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

def rezultatu_issaugojimas(duomenys, failo_pavadinimas):
    f = open(failo_pavadinimas, "w")
    # TODO: įrašyti į failą
    f.close()

vardai = failo_nuskaitymas("list.txt", "txt")
adresai = failo_nuskaitymas("addresses.csv", "csv")

rezultatas = []
for vardas in vardai:
    adresas = paieska(vardas, adresai)
    rezultatas.append(f"{vardas} gyvena adresu: {adresas}")     

# rezultato saugojimas į failą
rezultatu_issaugojimas(rezultatas, "rezultatas.txt")
print("Programa baigė darbą")
