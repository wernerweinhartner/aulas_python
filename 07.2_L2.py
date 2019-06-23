#outra forma de fazer o exercicio 7:

def calcula_reajuste(salario, valor_percentual):

   novo_salario = (salario * valor_percentual) + salario
   valor_reajuste = novo_salario - salario
   valor_percentual_int = int(valor_percentual * 100)

   print('Salário antes do reajuste: %.2f' % (salario))
   print('Percentual do reajuste: %d' % (valor_percentual_int))
   print('Valor do reajuste: %.2f' % (valor_reajuste))
   print('Novo salário: %.2f' % (novo_salario))


salario = float(input('Insira o salário atual: '))

if salario <= 280.0:
  calcula_reajuste(salario, 0.2)

elif salario > 280.0 and salario <= 700.0:
  calcula_reajuste(salario, 0.15)

elif salario > 700 and salario <= 1500.0:
  calcula_reajuste(salario, 0.10)

elif salario > 1500 and salario <= 2000:
  calcula_reajuste(salario, 0.5)

elif salario > 2000:
   calcula_reajuste(salario, 0.01)