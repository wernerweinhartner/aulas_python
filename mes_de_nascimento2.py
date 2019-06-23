meses = ('ss', 'janeiro', 'fevereiro', 'março', 'abril','maio','junho', 'julho',
'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

nasc = input('Insira sua data de nascimento no formato DD-MM-AAAA: ')

#para colocar um intervalo no indice: variavel[1:5]. O ultimo numero que se colocar
#nao conta.

indice = int(nasc[3:5])
mes = meses[indice]

print('Você nasceu no mês de', mes)