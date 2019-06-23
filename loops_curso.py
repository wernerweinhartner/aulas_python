# x = 0

# while x < 1:
#     nome = (input('Qual é o seu nome?'))


x = 0
pessoas = []
while x < 4:
    nome = (input('Qual é o seu nome?'))
    #evitar que o nome joao seja adicionado a lista
    if nome == 'joao': 
        continue
    pessoas.append(nome)
    x += 1
# continue === faz o programa voltar ao loop com determinada condição
#break === força a saida do loop e faz o programa seguir
print(pessoas)