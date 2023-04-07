#Pintando parede
l = float(input("Largura da parede: "))
a = float(input("Altura da parede: "))
area = l*a
print(f"Sua parede tem a dimensão de {l}x{a} e sua área é de {area:.2f}m².")
print(f"Para pintar essa parede, você precisará de {area/2:.2f}l de tinta.")
