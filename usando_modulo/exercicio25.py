## Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('qual e seu nome completo? ')).strip()
print("seu nome tem silva? {}".format('Silva' in nome.lower()))