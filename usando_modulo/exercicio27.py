##Desafio 027
##Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
##Ex: Ana Maria de Souza
##primeiro = Ana
##último = Souza]


n = str(input('digite seu nome completo: ')).strip()
nome = n.split()

print('muito prazer em te conhecer')
print('seu primeiro nome e {}'.format(nome[0]))
print('seu primeiro nome e {}'.format(nome[len(nome)-1]))
