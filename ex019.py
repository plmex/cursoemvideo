import random
import emoji


alunos = ('Rafael', 'Maria', 'Joana', 'Pedro')


print(f'\nEntre os possíveis alunos aptos à apagar a lousa estão: {alunos[0]}, {alunos[1]}, {alunos[2]} e {alunos[3]}.')


print('No dia de hoje, o escolhido para apagar o quadro é: {} 😜!\n\n'.format(random.choice(alunos)))