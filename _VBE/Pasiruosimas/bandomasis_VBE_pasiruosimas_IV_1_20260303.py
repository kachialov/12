def skaityti_varda(eilute):
    return eilute.split()
    
def skaityti_veikla(eilute):
    items = eilute.split()
    return items[0], items[1:]    
 
# Failo nuskaitymas
def failo_nuskaitymas(failo_pavadinimas):
    duomenys = []

    f = open(failo_pavadinimas)
    eiluciu_kiekis = int(f.readline())
    for i in range(eiluciu_kiekis):
        vardas, veiklu_kiekis = skaityti_varda(f.readline())
        print("vardas: ", vardas, "kiek:", veiklu_kiekis)
        for j in range(int(veiklu_kiekis)):
            pavadinimas, laikai =skaityti_veikla(f.readline())
            print(pavadinimas)
            print(laikai)
        #duomenys.append()
    

    return duomenys

def rezultatu_issaugojimas(duomenys, failo_pavadinimas):
    f = open(failo_pavadinimas, "w")
    # TODO: įrašyti į failą
    f.close()
    
vardai = failo_nuskaitymas("Duomenys.txt")