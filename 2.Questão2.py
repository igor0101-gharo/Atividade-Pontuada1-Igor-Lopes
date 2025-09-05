import os 
os.system("cls")

nome = input("Digite o seu nome:")
sexo = int (input("Identifique o seu sexo(digite o número):\n1.M\n2.F"))
civil = int (input("Identifique o seu estado civil(digite o número):\n1.Solteiro(a)\n2.Casado(a)"))

if sexo == 2 and civil == 2:
    anos = int(input("A quantos anos você é casada?\n"))
    print(f"Nome:{nome}\nSexo: F\nEstado civil: Casada\nanos de casada:{anos}")
elif sexo == 1 and civil == 1:
    print(f"Nome:{nome}\nSexo: M\nEstado civil:Solteiro")
elif sexo == 1 and civil == 2:
    print(f"Nome:{nome}\nSexo: M\nEstado civil: Casado")
elif sexo == 2 and civil == 1:
    print(f"Nome:{nome}\nSexo: F\nEstado civil: Solteira")
else:
    print("Valores inválidos")
