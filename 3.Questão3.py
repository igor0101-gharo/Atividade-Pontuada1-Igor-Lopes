import os
os.system("cls")

a = int(input("Digite um número inteiro:\n"))
b = int(input("Digite outro número inteiro:\n"))

if a == b:
    c = a+b
else:
    c = a*b

print(f"A variável 'c' para esses dois números vale {c}")

