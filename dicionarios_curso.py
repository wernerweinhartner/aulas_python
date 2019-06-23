#dicionarios
#são formados sempre em pares: chave + valor
joao = {'nome': 'joao', 'sobrenome': 'pereira', 'profissão': 'programador python',
'filhos': ['pedro', 'maria']}
print(joao['sobrenome'])
print(joao['profissão'])
print(joao['filhos'])

print(len(joao))

del joao['filhos']
print(joao)

joao ['profissão'] = 'aposentado'
print(joao)

'sobrenome' in joao
'idade' in joao

for x in joao:
    print(x)  #isso se chama loop

for x in joao:
    print(x+': '+joao[x])


print(joao.get('nome', 'Essa informação não consta no cadastro'))
print(joao.get('idade', 'Essa informação não consta no cadastro'))
#o get seleciona a informação associada a uma key(chave) 
joao['filhos'] = ['maria', 'pedro']
print(joao)

joao['filhos'].append('jorge')
print(joao)
