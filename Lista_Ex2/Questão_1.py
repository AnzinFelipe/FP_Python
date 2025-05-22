
while True:
    cord_x = int(input("Digite a coordenada do eixo X: "))
    cord_y = int(input("Digite a coordenada do eixo Y: "))

    if cord_x > 0 and cord_y > 0:
        print("\nPertence ao primeiro quadrante\n")
    elif cord_x < 0 and cord_y > 0:
        print("\nPertence ao segundo quadrante\n")
    elif cord_x < 0 and cord_y < 0:
        print("\nPertence ao terceiro quadrante\n")
    elif cord_x > 0 and cord_y < 0:
        print("\nPertence ao quarto quadrante\n")
    elif cord_x == 0 or cord_y == 0:
        break
    