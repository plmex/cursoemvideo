frase = str(input('Digite alguma coisa: ')).strip()


qtd_letra_a = frase.lower().count('a')
primeira_vez_a = frase.lower().find('a')
ultima_vez_a = frase.lower().rfind('a')

print('Em "{}", a letra A aparece {} vez(es).'.format(frase,qtd_letra_a))
print('A primeira vez que a letra "A" aparece é na {}ª posição.'.format(primeira_vez_a + 1))
print('A ultima vez que a letra "A" aparece é na {}ª posição.' .format(ultima_vez_a))