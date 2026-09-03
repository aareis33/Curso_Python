distancia = float(input('qual a distancia: '))
print(' voce esta preste a começar sua viagem de {}KM'.format(distancia))

if distancia <= 200:
    preço = distancia * 0.45
else: 
    preço = distancia * 0.50
print('o preço da passagem sera {:.2f}'.format(preço))