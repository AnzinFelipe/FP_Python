matriz = [[], [], []]
salario = soma_diagonal = 0

for i in range(3):
    for j in range(3):
        if j == 0:
            valor = float(input("\nQual o salário médio? "))
        elif j == 1:
            valor = int(input("Qual o tempo mínimo de experiência? "))
        elif j == 2:
            valor = float(input("Qual o valor da hora de trabalho? "))
        matriz[i].append(valor)

print("\nMatriz:")
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]}]", end = " ")

        if j == 0:
            salario += matriz[i][j]

        if i == j:
            soma_diagonal += matriz[i][j]

    print("")

media = salario / 3

print(f"\nA média salarial das 3 profissões é {media:.2f}")
print(f"A soma dos valores da diagonal principal é {soma_diagonal:.2f}")