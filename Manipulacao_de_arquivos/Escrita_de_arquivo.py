arquivo = open("Manipulacao_de_arquivos\\arquivo.txt", "w", encoding = "utf8")

for i in range(5):
    nome = input(f"Digite o {i + 1}º nome: ")
    sobrenome = input(f"Digite o {i + 1}º sobrenome: ")
    arquivo.write(nome + " " + sobrenome + "\n")

arquivo.close()

nomes_completos = []

for i in range(5):
    nome = input(f"Digite o {i + 1}º nome: ")
    sobrenome = input(f"Digite o {i + 1}º sobrenome: ")
    nomes_completos.append(f"{nome} {sobrenome}")

arquivo2 = open("Manipulacao_de_arquivos\\arquivo2.txt", "w", encoding = "utf8")
arquivo2.writelines("\n".join(nomes_completos) + "\n")
arquivo2.close()
