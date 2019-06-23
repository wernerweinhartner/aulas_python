#cores

cores = {'red': 'vermelho', 'blue': 'azul', 'green': 'verde', 
'purple': 'roxo', 'yellow': 'amarelo', 'black':'preto', 'white':'branco'}

cor_ing = input('Digite uma cor em inglês: ').lower()

print('A tradução dessa cor em português é:') 
print(cores.get(cor_ing, 'Esta cor não consta no meu dicionário'))





