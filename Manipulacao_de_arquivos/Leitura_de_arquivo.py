arquivo = open("Manipulacao_de_arquivos\\arquivo.txt", "r", encoding = "utf8")

print(arquivo.read())

arquivo.close()

arquivo2 = open("Manipulacao_de_arquivos\\arquivo2.txt", "r", encoding = "utf8")

print(arquivo2.readline())

arquivo2.close()

arquivo2 = open("Manipulacao_de_arquivos\\arquivo2.txt", "r", encoding = "utf8")

print(arquivo2.readlines())

arquivo2.close()
