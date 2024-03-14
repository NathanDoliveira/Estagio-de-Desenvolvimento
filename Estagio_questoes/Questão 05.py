palavra = input('Digite uma palavra: ')
palavra_invertida = ''

for i in range(len(palavra)-1, -1, -1):
   palavra_invertida += palavra[i]
print(f'Palavra invertida: {palavra_invertida}')