def media_num(num1, num2):
    media = (num1 + num2) / 2
    return media

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

media = media_num(num1, num2)

print(f"A média dos valores é: {media}")
