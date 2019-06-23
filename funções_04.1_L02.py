#Repita o exercício fazendo a função retornar, além do novo valor do produto 
# (somando o percentual do imposto), também o valor somente do imposto

custo = False
while custo == False:
    custo = input('Insira o custo do produto: ')
    try:
        custo = float(custo)
        if custo > 0:
            custo == True
        else:
            print('Inválido')
            custo = False
    except:
        print('Inválido')
        custo = False

imposto = False
while imposto == False:
    imposto = input('Insira a porcentagem de imposto sobre o produto: ')
    try: 
        imposto = float(imposto)
        if imposto > 0:
            imposto == True
        else:
            print('Inválido')
            imposto = False
    except:
        print('Inválido')
        imposto = False

def custo_total(custo, imposto):
    taxa_imposto = float(1 + (imposto/100))
    custo_total = custo*taxa_imposto
    valor_imposto = custo_total - custo
    #print('O valor do imposto é: %.2f' % (valor_imposto))
    return[custo_total, valor_imposto]

#print('O custo total do produto é: %.2f reais' % (custo_total(custo, imposto)))

retorno = custo_total(custo, imposto)
print('O custo total do produto é: %.2f reais' % (retorno[0]))
print('O valor do imposto é: %.2f reais' % (retorno[1]))