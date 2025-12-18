mokiniai = []

# # pridėdame pirmą elementa
# mokiniai.append(["Jonas"])
# dabartinis_mokinys = mokiniai[0]
# dabartinis_mokinys.append("Pil.")
# dabartinis_mokinys.append(7)

with open("Duomenys.txt") as failas:
    n = int(failas.readline())

    for i in range(n):
        eilute = failas.readline()
        mokinio_info = eilute.split()
        print("Mokinio vardas: ", mokinio_info[0], ".", sep="")
        print("Veiklos:")
        m = int(mokinio_info[1])
        for j in range(m):
            eilute = failas.readline()
            veikla = eilute.split()
            laikai = list(map(int, veikla[1:len(veikla)]))
            print(veikla[0], sum(laikai))






