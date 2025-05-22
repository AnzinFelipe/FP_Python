def idade(ano_atual, ano_nascimento):
    idade = ano_atual - ano_nascimento
    return idade

def maioridade(nome, idade):
    if idade >= 18:
        print(f"{nome} é maior de idade")
    else:
        print(f"{nome} é menor de idade")

nome = input("\nDigite seu nome: ")
ano_atual = int(input("Digite o ano atual: "))
nascimento = int(input("Digite seu ano de nascimento: "))

idade_pessoa = idade(ano_atual, nascimento)
maioridade(nome, idade_pessoa)
