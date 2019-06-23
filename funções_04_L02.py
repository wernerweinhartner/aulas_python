#Faça um programa com uma função chamada soma_Imposto. 
# A função possui dois parâmetros formais: taxa_Imposto,
#  que é a quantia de imposto sobre vendas expressa em porcentagem e custo, 
# que é o custo de um item antes do imposto.
#  A função “altera” o valor de custo para incluir o imposto sobre vendas.
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
    return(custo_total)

print('O custo total do produto é: %.2f reais' % (custo_total(custo, imposto)))
