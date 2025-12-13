largura = float(input('Insira a largura em metros: '))
altura = float(input('Insira a altura em metros: '))

area = largura * altura 

print('Sua parede possui {:.2f} m² de área e serão necessários {:.2f} litros de tinta para pintá-la'. format(area, area / 2))