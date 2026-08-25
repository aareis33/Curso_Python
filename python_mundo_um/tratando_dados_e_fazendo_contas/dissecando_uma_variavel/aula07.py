n1 = int(input('um valor: '))

n2 = int(input('outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('a soma é {}, \n 1o produto é {}, e a divisao e {:.3f}'.format(s, m, d), end=' ')
print('a divisao inteira {}, e potencia {}'.format(di, e))


#5 + 2 == 7 #adição
#5 - 2 == 3 #subtração
#5 * 2 == 10 #multiplicação 
#5 / 2 == 2.5 #divisao 
#5 ** 2 == 25 #potencia 5 ELEVADO AO QUADRADO
#5 // 2 == 2 #divisão inteira 1\
#5 %  2 == 1 #resto da divisao

#ORDEM DE PRECEDENCIA 

#1  ()TEM PARENTES, EXECUTA PRIMEIRO
#2  **
#3  * / // %
#4  + - 

# exercio 

#5+3*2==11

#3*5+4**2 == 31

#3*(5+4)**2 == 243