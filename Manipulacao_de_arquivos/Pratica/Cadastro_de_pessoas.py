nomes = []
sobrenomes = []
idades = []

N = int(input("\nQuantas pessoas serão cadastradas? "))

for i in range(N):
    nome = input(f"Digite o nome da {i + 1}ª pessoa: ")
    sobrenome = input(f"Digite o sobrenome da {i + 1}ª pessoa: ")
    idade = input(f"Digite a idade da {i + 1}ª pessoa: ")
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    idades.append(idade)

arquivo = open("Manipulacao_de_arquivos\Pratica\Pessoas_cadastradas", "w", encoding = "utf8")

arquivo.write("Há " + str(N) + " pessoas cadastradas" + "\n")
for i in range(N):
    arquivo.write("Nome: " + nomes[i] + " " + sobrenomes[i] + " Idade: " + idades[i] + "\n")
arquivo.close()

arquivo = open("Manipulacao_de_arquivos\Pratica\Pessoas_cadastradas", "r", encoding = "utf8")
print("")
print(arquivo.read())
arquivo.close()
