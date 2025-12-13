import emoji
import math

print('\n' ,'='*20, 'Vamos à aula de trigonometria!', '='*20, '\n' )



print("""Motivação: O Teorema de Pitágoras é um princípio matemático que afirma que, 
em qualquer triângulo retângulo, o quadrado do comprimento da hipotenusa 
(o lado mais longo do triângulo)  é igual à soma dos quadrados dos comprimentos 
dos outros dois lados, que são chamados de catetos.\n

Então tem-se que: \n
H² = (cateto a)² + (cateto b)² \n""")


print('Vamos testar! \n')
catetoa = float(input('Insira o comprimento do cateto a: '))
catetob = float(input('Insira o comprimento do cateto b: '))


hipotenusa = (catetoa**2 + catetob**2) ** 0.5

print("""\nFazendo o cálculo, temos:\n

H² = {:.2f}² + {:.2f}² = {:.2f}""". format(catetoa, catetob, hipotenusa))