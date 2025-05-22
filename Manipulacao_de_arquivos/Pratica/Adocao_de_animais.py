nomes_animais = []
racas_animais = []

for i in range(5):
    nome = input("Digite o nome do cachorro: ")
    raca = input("Digite a raça do cachorro: ")
    nomes_animais.append(nome)
    racas_animais.append(raca)

cadastro_adocao = open("Pratica\Cadastro_de_adocao", "w", encoding = "utf8")

for i in range(5):
    cadastro_adocao.writelines("Nome: " + nomes_animais[i] + " Raça: " + racas_animais[i] + "\n")

cadastro_adocao.close()

cadastro_adocao = open("Pratica\Cadastro_de_adocao", "r", encoding = "utf8")
print("\n---------Animais Cadastrados---------\n")
print(cadastro_adocao.read())
cadastro_adocao.close()
