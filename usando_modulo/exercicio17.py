## co =  float(input('cateto oposto '))
## ca =  float(input('cateto adiacente '))
## hi = (co ** 2 + ca ** 2) ** (1/2) 
## print('a hipotenusa vai medir {:.2f}'.format(hi))

from math     import hypot 
co =  float(input('cateto oposto '))
ca =  float(input('cateto adiacente '))
hi = hypot(co, ca)

print('a hi vai medir {:.2f}'.format(hi))