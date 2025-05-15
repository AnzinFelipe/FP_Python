caixoes = 0

while True:
    codigo = int(input("Digite o código do caixão para cadastrá-lo (digite -1 para encerrar): "))

    if codigo == -1:
        break
    caixoes += 1

print(f"\n{caixoes} caixões foram cadastrados\n")
