largura = float(input('qual a largura da parede: '))

altura = float(input('qual a altura da parede:'))

area = largura * altura


print('sua parede tem a distancia de {}x{} e sua area é {}'.format(largura, altura, area))

tinta = area / 2

print('para pintar, voce vai precisar de {}l'.format(tinta))
