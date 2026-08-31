##Crie um programa que leia o nome completo de uma pessoa e mostre:
##O nome com todas as letras maiúsculas
##O nome com todas minúsculas.
##Quantas letras ao todo (sem considerar espaços).
##Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('analisando seu nome...')
print('seu nome em maiuscukas é {}'.format(nome.upper()))
print('seu nome em minusculas é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
##nome.find('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('seu primeiro nome e {} e tem tantas letras {}'.format(separa[0], len(separa[0])))