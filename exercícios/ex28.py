from random import randint

sorteado = randint(0, 5)
print(sorteado)

while True:
    tentativa = int(input("Tente adivinhar o número que estou pensando: "))

    if tentativa == sorteado:
        print("Parabéns! Você acertou.")
        break
    
    else:
        print("Você errou, tente novamente")