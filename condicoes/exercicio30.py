numero = int(input('digite um numero: '))
resultado = numero  % 2
if resultado == 0:
    print('numero e par {}'.format(numero))
else:
    print('numero e impar'.format(numero))