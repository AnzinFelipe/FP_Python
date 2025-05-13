def calcular_perda_de_peso(peso_inicial, peso_atual):
    diferenca = peso_inicial - peso_atual
    percentual = (diferenca / peso_inicial) * 100
    return percentual

peso_inicial = float(input("\nDigite o peso inicial em Kg: "))
peso_atual = float(input("Digite o peso atual em Kg: "))

perda_de_peso = calcular_perda_de_peso(peso_inicial, peso_atual)

print(f"O aluno perdeu {perda_de_peso:.2f}% de peso\n")