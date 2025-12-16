nome_completo = str(input('Insira o nome completo: '))

nome_completo = nome_completo.strip().split()
nome_completo = " ".join(nome_completo)
print(nome_completo)

#print('{}'.format(nome_completo.upper()))
#print('{}'.format(nome_completo.lower()))
#print('O nome {} possui {} letras.'. format(nome_completo, len(nome_completo.replace(" ", ""))))
print('O primeiro nome {}, possui {} letras.'.format(nome_completo.split()[0], len(nome_completo.split()[0]))) 