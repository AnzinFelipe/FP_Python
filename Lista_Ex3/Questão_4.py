matriz = [[], [], []]
soma_uni1 = 0
menor_freq = 100

for i in range(3):
    for j in range(3):
        if j == 0:
            valor = float(input("\nDigite a nota da unidade 1: "))
        elif j == 1:
            valor = float(input("Digite a nota da unidade 2: "))
        elif j == 2:
            valor = float(input("Digite a frequência em porcentagem: "))
        matriz[i].append(valor)

print("\nMatriz:")
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]}]", end = " ")
        
        if j == 0:
            soma_uni1 += matriz[i][j]

        if matriz[i][2] < menor_freq:
            menor_freq = matriz[i][2]
    print("")

media = soma_uni1 / 3

print(f"\nA média das notas da unidade 1 é {media:.2f}")
print(f"A menor frequência é {menor_freq:.2f}\n")