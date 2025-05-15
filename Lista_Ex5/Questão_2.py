def escrita_votos(voto):
    arquivo = open("Lista_Ex5\Votos.txt", "w")
    for i in voto:
        try:
            arquivo.write(i + "\n")
        except ValueError:
            print("A função arquivo.write só aceita string")
    arquivo.close()
    return

def leitura_e_apuracao_votos():
    wars_votos = 0
    trek_votos = 0
    nulo = 0

    try:
        arquivo = open("Lista_Ex5\Votos.txt", "r")
        for i in range(10):
            num = (arquivo.readline().strip("\n"))

            if num == "1":
                wars_votos += 1
            elif num == "2":
                trek_votos += 1
            else:
                nulo += 1
        votos_nulos = f"A quantidade de votos nulos foi de {nulo}\n"
        arquivo.close()

        if wars_votos >= trek_votos:
            mais = f"\nStar Wars foi o filme mais votado com {wars_votos} votos\n"
            menos = f"Star Trek foi o filme menos votado com {trek_votos} votos\n"
        elif trek_votos > wars_votos:
            mais = f"\nStar Trek foi o filme mais votado com {trek_votos} votos\n"
            menos = f"Star Wars foi o filme menos votado com {wars_votos} votos\n"
        
        return print(mais + menos + votos_nulos)
    except FileNotFoundError:
        print("\nO arquivo Votos.txt não existe\n")

lista_votos = []

print("\n---VOTAÇÃO---")
print("1 - Star Wars\n"
"2 - Star Trek")
for i in range(10):
    voto = input("Digite o código do seu filme favorito: ")
    lista_votos.append(voto)
    escrita_votos(lista_votos)

leitura_e_apuracao_votos()