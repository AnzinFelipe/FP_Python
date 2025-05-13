def conta_palavras(frase):
    frase = frase.split()

    return len(frase)

frase = input("\nDigite uma frase: ")
print(f"A frase possui {conta_palavras(frase)} palavras\n")