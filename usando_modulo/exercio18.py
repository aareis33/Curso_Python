from math import radians, sin, cos, tan

angulo = float(input('angulo desejado: '))

seno = sin(radians(angulo))

print('o angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))

cosseno = cos(radians(angulo))
print('o angulo de {} tem cosseno {:.2f}'.format(angulo, cosseno))

tangente = tan(radians(angulo))
print('o angulo o de {} tem a tangente de {:.2f}'.format(angulo, tangente))