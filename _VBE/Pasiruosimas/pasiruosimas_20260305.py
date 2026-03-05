def val_kiekis(student):
    sum = 0
    for veikla, valandos in student.items():
        for v in valandos:
            sum += v
    return sum
    
def veiklu_valandos(students):
    for vardas, veiklos in students.items():
        if (val_kiekis(veiklos) >= 20):
            print(f"{vardas}:")
            print(f"Viso valandų: {val_kiekis(veiklos)}")
            for veikla, grades in veiklos.items():
                print(f"  {veikla} -> {grades}")      

# Create an empty dictionary to store all students
students = {}

with open("Duomenys.txt") as failas:
    n = int(failas.readline())  # Number of students

    for i in range(n):
        # Read student name and number of activities
        eilute = failas.readline()
        mokinio_info = eilute.split()
        vardas = mokinio_info[0]
        m = int(mokinio_info[1])

        # Initialize dictionary for this student
        students[vardas] = {}

        # Read each activity and its grades
        for j in range(m):
            eilute = failas.readline()
            veikla = eilute.split()
            pavadinimas = veikla[0]
            laikai = list(map(int, veikla[1:]))
            
            # Store the grades list in the nested dictionary
            students[vardas][pavadinimas] = laikai


# Example: print the dictionary
for vardas, veiklos in students.items():
    if (val_kiekis(veiklos) >= 20):
        print(f"{vardas}:")
        print(f"Viso valandų: {val_kiekis(veiklos)}")
        for veikla, grades in veiklos.items():
            print(f"  {veikla} -> {grades}")        

    
