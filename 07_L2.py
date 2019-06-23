#Uma empresa resolveu dar um aumento de salário aos seus
#  colaboradores e lhe contrataram para desenvolver 
# o programa para calcular os reajustes. 
# Faça um programa que recebe o salário de um colaborador e
#  o reajuste segundo o seguinte critério, baseado no salário atual:
#Salários até R$ 280,00 (incluindo) : aumento de 20%
#Salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#Salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#Salários de R$ 1500,00 em diante: aumento de 5% 
#Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

#função é chamada depois de ser declarada

salario = float(input('Insira o salário atual: '))
percentual = ''
valor_reajuste = 0
novo_salario = 0

if salario <= 280.0:
    percentual = '20%'
    novo_salario = (salario * 0.2) + salario
    valor_reajuste = novo_salario - salario

elif salario > 280.0 and salario <= 700.0:
    percentual = '15%'
    novo_salario = (salario * 0.15) + salario
    valor_reajuste = novo_salario - salario

elif salario > 700 and salario <= 1500.0:
    percentual = '10%'
    novo_salario = (salario * 0.1) + salario
    valor_reajuste = novo_salario - salario    

elif salario > 1500:
    percentual = '5%'
    novo_salario = (salario * 0.05) + salario
    valor_reajuste = novo_salario - salario    



print('Salário antes do reajuste: %.2f' % (salario))  
print('Percentual do reajuste: %s' % (percentual))  
print('Valor do reajuste: %.2f' % (valor_reajuste))
print('Novo salário: %.2f' % (novo_salario))  



