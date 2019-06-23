meses = ('ss', 'janeiro', 'fevereiro', 'março', 'abril','maio','junho', 'julho',
'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

data_nasc = str(input('Insira sua data de nascimento no formato DD-MM-AAAA: '))

#print(len(data_nasc))
#a = str(data_nasc[3])
#b = str(data_nasc[4])
#c = a + b
#c = int(c)
#print(c)

mes = int(data_nasc[3:5])

mes_nasc = (meses[mes])
print('Você nasceu no mês de',mes_nasc)
