a = int(input('numero1 '))
b = int(input('numero1 '))
c = int(input('numero1 '))

menor = a

if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('numero menor é {}'.format(menor))
print('numero maior é {}'.format(maior))
