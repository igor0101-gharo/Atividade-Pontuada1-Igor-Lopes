import os
os.system("cls")

operador = input("Digite um operador(+,-,* ou /):\n")
a = float (input("Digite um número:\n"))
b = float (input("Digite outro número:\n"))

match operador:
    case "+":
        resultado = a+b
        print(f"Resultado:{resultado}")
    case "-":
        resultado = a-b
        print(f"Resultado:{resultado}")
    case "*":
        resultado = a*b
        print(f"Resultado:{resultado}")
    case "/":
        resultado = a/b
        print(f"Resultado:{resultado}")
    case _:
        print("Operador inválido.")