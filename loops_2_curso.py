# Loop FOR: funciona com sequências === listas, tuplas, dicionarios, strings...

compras = ['arroz', 'feijão', 'macarrão', 'carne']

nome = 'joaquim'

#for i in compras:
 #   print(i)

# for i in nome:
#      print(i)


#somatorio com for

# vendas = [1000, 450, 300, 920, 600]
# total = 0

# for i in vendas:
#     total += i

# print(total)

# for com dicionários

# cores = {'verde': 'green', 'preto': 'black', 'azul': 'blue'}

# for i in cores:
#     print(i,':',cores[i])


#for aninhado

compras = [['arroz', 'feijão','macarrão'], ['carne', 'frango', 'peixe'], ['iogurte', 'leite']]

for i in compras:
    for item in i:
        print(item)

for i in range (0,10):
    print(i + 1)
    #print(10 - i) === contagem regressiva







