time1 = input("Digite o nome do primeiro time: ")
gols1 = int(input("Quantos gols o time marcou? "))

time2 = input("\nDigite o nome do segundo time: ")
gols2 = int(input("Quantos gols o time marcou? "))

if gols1 > gols2:
    print(f"\nO time {time1} foi o vencedor\n")
elif gols2 > gols1:
    print(f"\nO time {time2} foi o vencedor\n")
else:
    print("\nEMPATE\n")
    