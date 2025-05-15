lista_nomes = []
lista_idade = []
i = 1
maior_idade = 59
soma_idades = 0

N = int(input("\nQuantos funcionários estão aptos à aposentadoria? "))

while i <= N:
    nome = input("Qual o nome completo do funcionário? ")
    idade = int(input("Qual a idade? "))

    if idade < 60:
        print("O funcionário não pode se aposentar ainda")
    else:
        lista_nomes.append(nome)
        lista_idade.append(idade)
        i += 1

print("\nFuncionários a se aposentar em 2025")
print("*" * 35, "\n")

for j in range(N):
    print(f"Nome: {lista_nomes[j]}\t Idade: {lista_idade[j]}")
    soma_idades += lista_idade[j]

    if lista_idade[j] > maior_idade:
        maior_idade = lista_idade[j]
        mais_idoso = lista_nomes[j]

media = soma_idades / len(lista_idade)

print(f"\nFuncionário mais antigo: {mais_idoso}")
print(f"Média de idades das aposentadorias: {media:.2f} anos\n")