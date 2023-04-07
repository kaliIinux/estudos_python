#Disecando uma variável
i = input("Digite algo: ")
print("O tipo primitivo desse valor é: ", type(i))
print("Só tem espaços? ", i.isspace)
print("É um número? ", i.isnumeric)
print("É alfabético? ", i.isalpha)
print("É alfanumérico? ", i.isalnum)
print("Está em maiúsculas? ", i.isupper)
print("Está em minúsculas? ", i.islower)
print("Está capitalizada? ", i.istitle)

