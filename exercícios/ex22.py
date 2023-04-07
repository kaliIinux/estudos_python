nome = str(input("Digite seu nome completo: ")).strip()
nomeseparado = nome.split()

print("Seu nome em maiúsculo é: {}".format(nome.upper()))
print("Seu nome em minúsculo é: {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome)-nome.count(" ")))
print("Seu primeiro nome é {} e ele tem {} letras".format(nomeseparado[0], len(nomeseparado[0])))