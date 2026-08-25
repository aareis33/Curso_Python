dias = int(input('quantos dias alugados? '))
km = float(input('quantos km rodados?' ))
pago = (dias * 60) + (km * 0.15)

print('0 total a pagar e R${:.2f}'.format(pago))