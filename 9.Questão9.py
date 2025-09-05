import os
os.system("cls")

renda = float(input("Digite sua renda mensal:\nR$"))
emprestimo = float(input("Digite o valor do empréstimo desejado:\nR$"))
prestacao = int(input("Digite em quantas prestações deseja pagar:\n"))
valor_prestacao = emprestimo/prestacao

if emprestimo > 10*renda or valor_prestacao > 0.3*renda:
    print("Não é possível conceder um empréstimo com os valores estipulados.")
else:
    print("O empréstimo pode ser concedido.")


