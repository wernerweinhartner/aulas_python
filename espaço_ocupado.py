arq = open('arquivos/usuarios.txt', 'r')
texto = arq.readlines()
arq.close()

lista = []
mb = []
nome = ''
for i in texto:
    i = str(i)
    nome, num = i.split()
    lista.append(nome)
    num = int(num)
    num = num/(1024**2)
    num = round(num,2)
    mb.append(num)
# print(lista) ; print(mb)
soma = sum(mb) 
media = soma/len(lista)
media = round(media,2)
media = str(media)
media = media + ' MB'

percent = []
prc = 0
for i in mb:
    prc = (i/soma) * 100
    prc = round(prc, 2)
    percent.append(prc)
# print(percent)
c = 0
# lista2 = []
lista2 = []
for i in lista:
    # lista2.append(i + ' ' + str(mb[c]) + 'MB' + ' ' + str(percent[c]) + '%')
    lista2.append(str(c+1) + ' ' + i + ' ' + str(mb[c]) + 'MB' + ' ' + str(percent[c]) + '%' + '\n')
    c += 1
print(lista2)

soma = str(soma)
soma = soma + ' MB'
print(soma)



relatorio = open('arquivos/relatorio5.txt' , 'w')
relatorio.write('ACME Inc.               Uso do espaco em disco pelos usuarios \n')
relatorio.write('------------------------------------------------------------------------ \n')
relatorio.writelines(lista2)
relatorio.write('\n')
relatorio.write('Espaco medio ocupado: ' + media + '\n')  
relatorio.write('Espaco total ocupado: ' + soma)
relatorio.close()
