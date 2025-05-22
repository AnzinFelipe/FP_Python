def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n1 > n2:
        return n1 / n2
    else:
        return n2 / n1

continuar = input("Deseja realizar uma operação? [S]/[N] ").upper()

while continuar == "S":
    num1 = int(input("\nDigite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    print("\n[S] Soma;\n"
    "[B] Subtração;\n"
    "[M] Multiplicação;\n"
    "[D] Divisão.")
    opcao = input("Qual opção você deseja? ").upper()
    print()

    if opcao == "S":
        print(soma(num1, num2))
    elif opcao == "B":
        print(subtracao(num1, num2))
    elif opcao == "M":
        print(multiplicacao(num1, num2))
    elif opcao == "D":
        print(divisao(num1, num2))

    continuar = input("\nDeseja realizar outra operação? [S]/[N] ").upper()
    