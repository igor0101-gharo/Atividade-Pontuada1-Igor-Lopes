import os
os.system("cls")

nome = input("Digite o nome do produto:\n")
quantidade = int(input("Digite a quantidade comprada:\n"))
precou = float (input("Digite o preço unitário:\nR$"))
total = precou*quantidade

if quantidade <= 5:
    desconto = 2
    final = 0.98*total
elif quantidade > 5 and quantidade <= 10:
    desconto = 3
    final = 0.97*total
else:
    desconto = 5
    final = 0.95*total

print(f"Produto:{nome}\nValor total da compra:R${total:.2f}\nDesconto:{desconto}%\nTotal a pagar:R${final:.2f}")
    
