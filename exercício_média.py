a = float(input('Digite a nota da primeira prova: '))
b = float(input('Digite a nota da segunda prova: '))
c = float(input('Digite o peso da primeira prova: '))
d = float(input('Digite o peso da segunda prova: '))
media_ponderada_das_notas = float(((a*c) + (b*d))/(c+d))
print(media_ponderada_das_notas)
