#listas e tuplas: são sequencias de dados

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio',
'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(meses)
type(meses)

#a variavel meses é uma tuple === indicada pelos parenteses

alunos = ['joao', 'maria', 'pedro', 'helena']
type(alunos)

#a variavel alunos é uma list === indicada pelos colchetes

#len === mostra o comprimento de uma list/tuple

print(len(meses))

print(len(alunos))

#tuplas são imutaveis enquanto que as listas são mutaveis
#len + ()
#variavel[0,1,2...] == mostra a posição, indice. comeca com o numero 0
#variavel.append('') === adiciona um elemento a lista
#variavel.insert(indice, '') === insere um novo elemento a lista em uma posição 
#especifica
#variavel.sort() === coloca os elementos da lista em ordem alfabetica
#variavel.pop(indice) === remove o elemento que se encontra em determinado indice
#variavel.remove('') === remove um elemento especifico (nomeia se o elemento)






alunos[1] = 'mariah'

print(alunos)

alunos.append('ricardo')
print(alunos)

alunos.insert(1, 'paula')
print(alunos)

alunos.sort()
print(alunos)

alunos.pop(1)
print(alunos)

alunos.remove('paula')
print(alunos)

alunos2 = ['joana', 'jorge']
total = alunos + alunos2
print(total) #isso se chama concatenação

indice = 3
print(total[indice])