numero = input('Digite um número: ')


tamanho = len(numero)
numero = numero[tamanho::-1]

print('unidade: {} \ndezena: {}\ncentena: {}\nmilhar: {}'. format(numero[0], numero[1], numero[2], numero[3]))