def escrita(nome_arquivo):
    arquivo = open(nome_arquivo, "w", encoding = "utf8")
    for i in range(1, 7):
        nome = input(f"Qual o nome da {i}ª pessoa? ")
        sobrenome = input(f"Qual o sobrenome da {i}ª pessoa? ")

        arquivo.write(nome + " " + sobrenome + "\n")    
    arquivo.close()
    return

def alteracoes(nome_arquivo):
    arquivo = open(nome_arquivo, "r", encoding = "utf8")
    nome_lista = arquivo.readlines()
    for i in range(len(nome_lista)):
        print("\n" + nome_lista[i].strip("\n"))
        decisao = input("Deseja alterar esse nome? ").capitalize()

        if decisao == "Sim":
            nome = input(f"\nQual o nome {i+1}ª pessoa? ")
            sobrenome = input(f"Qual o sobrenome da {i+1}ª pessoa? ")
            nome_lista[i] = nome + " " + sobrenome + "\n"
    arquivo.close()

    arquivo = open(nome_arquivo, "w", encoding = "utf8")
    arquivo.writelines(nome_lista)
    arquivo.close()

    arquivo = open(nome_arquivo, "r", encoding = "utf8")
    nomes = arquivo.read()
    return print("\n---Nomes---\n" + nomes)

escrita("Lista_Ex5\\nomes.txt")

alteracoes("Lista_Ex5\\nomes.txt")