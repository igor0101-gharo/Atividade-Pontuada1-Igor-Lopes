import os
os.system("cls")

morangos = float (input("Digite a quantidade de morangos(em kg):"))
macas = float (input("Digite a quantidade de maçãs(em kg):"))

if morangos <= 5:
    preco_morango = 2.5*morangos
else:
    preco_morango = 2.2*morangos

if macas <= 5:
    preco_macas = 1.8*macas
else:
    preco_macas = 1.5*macas

preco_total = preco_macas + preco_morango
peso_total = morangos + macas
desconto = 0.9*preco_total

if peso_total >= 10 or preco_total >= 15:
    print (f"O valor de sua compra foi de R${desconto:.2f}")
else:
    print (f"o valor de sua compra é de R${preco_total:.2f}")
    

