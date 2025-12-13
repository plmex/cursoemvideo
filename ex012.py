produto = float(input('Digite o valor do produto (R$): '))

print('O produto custa R${:.2f}, mas com 5% de desconto ele sai a R${:.2f}'. format(produto, produto - produto * 5/100 ))