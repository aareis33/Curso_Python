##💡 Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cid = str(input('em que cidade voce nasceu? ')).strip()
print(cid[:5].upper() == 'Santo')