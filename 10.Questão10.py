import os
os.system("cls")

print("""
Combústivel\tQuantidade vendida\tDesconto por litro
    Álcool\tAté 25 litros\t\t10%
    Álcool\tAcima de 25 litros\t20%
    Gasolina\taté 25 litros\t\t15%
    Gasolina\tAcima de 25 litros\t30%""")

combustivel = input("Digite o combustivel comprado (Digite a letra maiuscula correspondente):\nA-álcool\nG-gasolina")
litros = float (input("Digite a quantidade adquirida(em litros):"))
preco_alcool = litros*3.79
preco_gasolina = litros*6.59

match combustivel:
    case "A":
        if litros <= 25:
            desconto = 0.9*preco_alcool
            print(f"Valor a ser pago:R${desconto:.2F}")
        else:
            desconto = 0.8*preco_alcool
            print(f"Valor a ser pago:R${desconto:.2F}")
    case "G":
        if litros <= 25:
            desconto = 0.85*preco_gasolina
            print(f"Valor a ser pago:R${desconto:.2F}")
        else:
            desconto = 0.7*preco_gasolina
            print(f"Valor a ser pago:R${desconto:.2F}")
    case _:
        print("Valor inválido.")
            