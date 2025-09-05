import os
os.system("cls")

print ("""
Cores Disponíveis
    verde
    azul
    amarelo
    vermelho""")
cor = input("Digite a cor do CD(sem letras maiúsculas):\n")

match cor:
    case "verde":
        print("Preço: R$10,00")
    case "azul":
        print("Preço: R$20,00")
    case "amarelo":
        print("Preço: R$30,00")
    case "vermelho":
        print("Preço: R$40,00")