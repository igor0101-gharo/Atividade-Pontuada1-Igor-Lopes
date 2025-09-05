import os
os.system("cls")

a = float(input("Digite o número 'A'."))
b = float(input("Digite o número 'B'."))
c = float(input("Digite o número 'C'."))
soma = a + b

if soma < c:
    print("A soma'A'+'B' é menor 'C'.")
#elif soma == c:
    #print("A soma 'A'+'B' é igual a 'C'.")
    #retirei essa linha do codigo porque a questão não pediu para verificar se os números são iguais.
else:
    print("A soma 'A'+'B' é maior que 'C'.")
