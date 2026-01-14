nome = str(input('Digite o nome completo: ')).strip().split()

qtd_nomes = len(nome)
print(qtd_nomes)

print('Seu primeiro nome é: {}.'.format(nome[0]))
print('Seu último nome é: {}.'.format(nome[qtd_nomes - 1]))