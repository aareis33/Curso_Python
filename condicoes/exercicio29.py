velocidade = float(input('qual a velocidade do carro? '))

if velocidade >80:
    print('voce esta andado a cima da velocidade. sera multado!!')
    multa = (velocidade-80) * 7
    print('voce deve pagar uma multa de {}'.format(multa))
print('voce esta dentro do limite, boa viagem')