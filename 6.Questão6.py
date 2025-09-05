import os
os.system("cls")

nota1 = float(input("Digite sua primeira nota:\n"))
nota2 = float(input("Digite sua segunda nota:\n"))
media = (nota1+nota2)/2

if media <= 4:
    print(f"Sua média é de {media}.\nVocê foi reprovado.")
elif media > 4 and media <= 5.9:
    print(f"Sua média é de {media}.\nVocê está de recuperação.")
else:
    print(f"Sua média é de {media}.\nParabéns! Você foi aprovado.")     
