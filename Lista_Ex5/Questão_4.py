while True:
    print("\nDigite Escrever para escrever um arquivo\n"
          "Digite Ler para ler um arquivo\n"
          "Digite Sair para sair")
    opcao = input("Qual opção você quer? ").capitalize()

    if opcao == "Sair":
        break
    if opcao == "Ler":
        try: 
            arquivo = open("Lista_Ex5\\Numeros.txt", "r")
            print(arquivo.read())
            arquivo.close()
        except FileNotFoundError:
            print("\nO arquivo Numeros.txt não existe")
    if opcao == "Escrever":    
        try:
            primeira_escrita = 1
            maior = 0

            arquivo = open("Lista_Ex5\\Numeros.txt", "r")
            lista_num = arquivo.readlines()
            for i in lista_num:
                if int(i.strip("\n")) >= maior:
                    maior = int(i)
            arquivo.close()
        except FileNotFoundError:
            primeira_escrita = 0

        arquivo = open("Lista_Ex5\\Numeros.txt", "a") 
        try: 
            num = int(input("\nDigite um número: "))
            if primeira_escrita == 0:
                arquivo.write(str(num) + "\n")
            else:
                if num > maior:
                    arquivo.write(str(num) + "\n")
        except ValueError:
            print("\nErro: é preciso escrever um número inteiro")
        arquivo.close()
        