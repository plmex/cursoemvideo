dinheiro = float(input("Insira o valor(R$): "))

dolar = float(input("Insira o valor atual do dólar: "))

print('R$ {:.2f}, equivale a US$ {:.2f}.' .format(dinheiro, dinheiro/dolar))