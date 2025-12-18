# mokiniai = [["Jonas", "Pil.", 7, "Soc.", 4, "Kul.", 5]
#            ,["Kajus", "", 0]
# 		   ,[]
# 		   ,["Jonas"]
# 		   ,[]]
# # pridėti mokinį
# mokiniai.append(["Jonas"])
# # modifikuoti mokinį
# dabartis_mokinis = mokiniai[0]
# # pridėti veiklą
# dabartis_mokinis.append("Pil.")
# dabartis_mokinis.append(mokiniai = [["Jonas", "Pil.", 7, "Soc.", 4, "Kul.", 5]
# )

mokiniai = []

with open("Duomenys.txt") as failas:
    n = int(failas.readline()) # mokinių kiekis
    #  nuskaitome mokinių duomenis
    for i in range(n):
        eilute = failas.readline().split()
        print("Vardas: ", eilute[0])
        m = int(eilute[1]) 
        print("Veiklų kiekis: ", m)
        for j in range(m):
            eilute = failas.readline().split()
            print("Veiklos pavadinimas: ", eilute[0], end=" Užemė laiko: ")
            veiklu_laikai = list(map(int, eilute[1:len(eilute)]))
            print(sum(veiklu_laikai))
