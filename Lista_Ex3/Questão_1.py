lista = []
esfera = limpeza = troca = quebrado = 0
i = 1

N = int(input("\nQual a quantidade de mouses? "))
print("\nTipos de defeitos:" \
"\n1 - Necessita da esfera;" \
"\n2 - Necessita de limpeza;" \
"\n3 - Necessita troca do cabo ou conector;" \
"\n4 - Quebrado ou inutilizado.")

while i <= N:
    tipo = int(input("Qual o defeito do mouse? "))
    if 0 < tipo < 5:
        lista.append(tipo)
        i += 1

        if tipo == 1:
            esfera += 1
        elif tipo == 2:
            limpeza += 1
        elif tipo == 3:
            troca += 1
        elif tipo == 4:
            quebrado += 1
    else:
        print("Valor inválido, tente novamente")

print(f"\nQuantidade de mouses: {N}")
print("\nSituação\t\t\t\t Quantidade\t Percentual")
print(f"1 - Necessita da esfera\t\t\t {esfera}\t\t {esfera * 100 / N:.1f}%")
print(f"2 - Necessita de limpeza\t\t {limpeza}\t\t {limpeza * 100 / N:.1f}%")
print(f"3 - Necessita troca do cabo ou conector\t {troca}\t\t {troca * 100 / N:.1f}%")
print(f"4 - Quebrado ou inutilizado\t\t {quebrado}\t\t {quebrado * 100 / N:.1f}%")