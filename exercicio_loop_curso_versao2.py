repetir = 's'
fatura = []
total = 0

while repetir == 's':
    produto = input('Digite o nome do produto: ')
    preço = float(input('Digite o preço do produto: '))
    fatura.append([produto, preço])
    total += preço
    repetir = input('Deseja comprar mais algum produto?: ')
    if repetir == 's': 
        continue
    else: 
        break


for i in fatura:
    print(i[0], ':', i[1])

print('O total da fatura é: %d' % (total))            
