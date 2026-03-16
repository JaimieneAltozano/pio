quantity_people = int(input("How many people would you like to add?: "))
people = []
accepted = []
rejected = []

while quantity_people > 0:
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    known = input(f"{name} has basic computation know? Y/N: ").lower()
    if known == "y":
        known = True
    elif known == "n":
        known = False
    quantity_people -= 1
    people.append((name, age, known))


for i in people:
    if age >= 15 and known == True:
        accepted.append(name, age, known)
        print(f"Sí se pudooooooo {accepted}")
    else:
        rejected.append()
        print(f"Mándese a recoger {rejected}")

for p in aceptados:
    print ("-", p)
#registrar participantes y validar si pueden
#asistir al taller.
