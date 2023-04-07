import random
a1 = str(input("Primeiro aluno: "))
a2 = str(input("Primeiro aluno: "))
a3 = str(input("Primeiro aluno: "))
a4 = str(input("Primeiro aluno: "))
alunos = [a1,a2,a3,a4]
escolhido = random.choice(alunos)
print("O aluno escolhido foi: {}".format(escolhido))

    
    