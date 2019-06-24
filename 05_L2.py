# Faça um programa para a leitura de duas notas de um aluno, entre 0 e 10 
# e calcule sua nota média. O programa deve calcular a média alcançada 
# pelo aluno e apresentar um dos seguintes resultados conforme a média alcançada:
#"Aprovado", se a média alcançada for maior ou igual a sete;
#"Reprovado", se a média for menor do que sete;
#"Aprovado com Distinção", se a média for igual a dez.

a = float(input('Digite a primeira nota do aluno: '))
b = float(input('Digite a segunda nota do aluno: '))


media = (a + b) / 2.0
#GGGGGGGGGGGGG
#print
print('werner')

if media >= 7 and media < 10.0:
    print('Aprovado')

elif media < 7.0:
    print('Reprovado') 

elif media == 10.0:
    print('Aprovado com distinção!')

print('Sua média eh igual a: %.2f ' %  (media))    
