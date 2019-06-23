lista = []


produtos = {'arroz': 5, 'feijão': 4, 'cenoura': 7, 'leite': 4, 'café': 8}


repetir = 'sim'

while repetir == 'sim':
    a = input('Insira o produto que deseja comprar: ')
    lista.append(a)
    produto = input('Deseja continuar comprando? ')
    if produto == 'sim': 
        continue
    elif produto == 'não':
        break
    else: 
        break


total = 0

for i in lista:
    total += produtos.get(i)

print(total)    
print(lista)

print('O total de suas compras, em reais, é: %d' %(total))
print('Os produtos comprados são: %s' %(lista))











#a = input('Insira  ')

#lista.append(a)

#print(lista)
