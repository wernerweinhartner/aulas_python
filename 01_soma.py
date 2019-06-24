# Faça um Programa que peça dois números e imprima a soma.
# A função input só aceita números
# A função raw_input aceita strings

# int (variável) converte para inteiro
# int (variável) converte para string 

a = input('Informe o valor de A:')
b = input('Informe o valor de B:')

resultado = float(a) + float(b)

# Forma primitiva de concatenação
#print('A soma de ' + a +' + '+ b +' = ' + str(resultado))
# Forma mais eficiente %s=string e %d=int e %f=float(decimais)
# Para float: colocar %(0).5(ex) para o numero de casas decimais que se quer obter. O zero é opcional

print('O resultado de %s + %s = %0.4f' % (a, b, resultado) )

# fim do arquivo.