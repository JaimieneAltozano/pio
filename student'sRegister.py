students = []
def student(dato1, dato2):
    students.append({
        "Name": dato1,
        "ID": dato2,
        "Subjects": []
    })
    
while True:
    print("\nMenu:\n1. Exit\n2. Registrar estudiante\n3. Registrar materias/notas\n")
    options = input("Option: ")
    if options == "1":
        print("Bye")
        break
    elif options == "2":
        cantidad = int(input("Cantidad de estudiantes: "))
        for i in range(cantidad):
            nameStudent = input("Nombre de estudiante: ")
            idStudent = input("ID student: ")
            student(nameStudent, idStudent)
        choose = input("Show the register?\n1. Yes\n2. No: ")
        if choose == "1":
            print(students)
        elif choose == "2":
            continue
        else: 
            print("That option doesn't exist")
    elif options == "3":
        finderStudent = input("Ingrese ID de estudiante: ")
        found = False
        for i in students:
            if i["ID"] == finderStudent:
                found = True
                print(f"This is the student: {i}")
                choose = input("1. Add subject\n2. Add grades: ")
                if choose == "1":
                    quantitySubjects = int(input("Cantidad de materias: "))
                    for j in range(quantitySubjects):
                        subject = input("Subject: ")
                        i["Subjects"].append({
                            "Name" : subject, 
                            "Grades" : []
                            })
                    choose = input("Show?\n1. Yes\n2. No: ")
                    if choose == "1":
                        print(i)
                    elif choose == "2":
                        continue
                    else:
                        print("Hey loco, qué pazza valemía, ombee")
                elif choose == "2":
                    pass
                else:
                    print("That option doesn't exist")
        if not found:
            print("Not found")
