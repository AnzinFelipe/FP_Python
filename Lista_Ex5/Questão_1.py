try:
    n = int(input("\nQuantos IPs você quer escrever? "))
    arquivo = open("Lista_Ex5\\Enderecos_IPs.txt", "w")

    for i in range(n):
        for j in range(1, 5):
            if j == 4:
                valor = int(input("Digite o último valor dor IP: "))
                arquivo.write(str(valor) + "\n")
            else:
                valor = int(input(f"Digite o {j}º valor do IP: "))
                arquivo.write(str(valor) + ".")
        print("")
    arquivo.close()

    arquivo = open("Lista_Ex5\\Enderecos_IPs.txt", "r")
    for i in range(n):
        invalido = 0

        IP = arquivo.readline().strip("\n")
        nums_IP = IP.split(".")

        for i in nums_IP:
            if int(i) > 255:
                invalido += 1
        if invalido > 0:
            print(f"O IP {IP} é inválido")
        else:
            print(f"O IP {IP} é válido")
    print("")
    arquivo.close()
except ValueError:
    print("\nErro: é preciso digitar um valor numérico\n")