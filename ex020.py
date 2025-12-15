import random


alunos = ('Rafael', 'Maria', 'Joana', 'Pedro')


alunos_sorteados = random.sample(alunos,4)



print("""\nA ordem de apresentação dos trabalhos será feita por sorteio do nome do integrante do grupo! 
Logo, a ordem de apresentação será:\n""")

print("""1º grupo: {} 
2º grupo: {} 
3º grupo: {} 
4º grupo: {}""".format(alunos_sorteados[0], alunos_sorteados[1], alunos_sorteados[2], alunos_sorteados[3]))
