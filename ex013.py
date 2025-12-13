salario = float(input('Insira o valor do salário atual (R$): '))


print('\nParabéns! Você é um ótimo funcionário e por isso recebeu um aumento de 15%!', end = " ")
print('A partir de hoje o seu salário passa de R$ {:.2f} para R$ {:.2f}!\n'. format(salario, salario + salario * 15/100))