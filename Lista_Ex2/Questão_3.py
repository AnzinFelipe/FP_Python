
while True:
    pH = int(input("Digite o pH da solução (digite -1 para encerrar): "))

    if pH == -1:
        break

    if pH < 7:
        print("\nA solução é ácida\n")
    elif pH > 7:
        print("\nA solução é básica\n")
    else:
        print("\nA solução é neutra\n")
        