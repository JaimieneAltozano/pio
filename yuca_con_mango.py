# 1:
for i in range(10):
    print(i + 1)

# 2:
for i in range(10, 0, -1):
    print(i)

# 3:
for i in range(10):
    print(f"1 + {i} = {i + 1}")

# 4:
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 5:
for i in range(1, 31):
    if i % 3 == 0:
        print(i)

# 6 y 9:
palabra = input("Palabra: ")
mayuscula = 0
minuscula = 0
contador = 0

for i in palabra:
    if i == i.upper():
        mayuscula = mayuscula + 1
    elif i == "a" or i == "A":
        contador += 1
    else:
        minuscula = minuscula + 1

print(f"Mayúsculas: {mayuscula}")
print(f"Minúsculas: {minuscula}")

print(palabra.upper())
print(palabra.lower())

# 7:
for i in range(11):
    print(f"5 x {i} = {i * 5}")

# 8:
list = [3, -1, 5, -2, 7, -8]

for num in list:
    if num >= 0:
        print(num)

# 10:
contraseña = "Py123"
for i in range(3):
    pato= input("Contraseña: ")
    if contraseña == pato:
        print("Aceptado")
        break
    else:
        print("Asesinado")