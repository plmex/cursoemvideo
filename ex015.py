dias = int(input('Informe a quantidade de dias: '))
km = float(input('Informe a quilometragem rodada (km): '))

valor = dias * 60 + km * 0.15

print("O veículo foi alugado por {} dias e rodou {:.2f} km". format(dias, km))
print('Valor a pagar: R$ {:.2f}'. format(valor))

print('Agradecemos pela preferência!')