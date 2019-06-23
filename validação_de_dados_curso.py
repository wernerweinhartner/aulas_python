repetir = 's'
fatura = []
total = 0
valid_preço = False 

#função TRY === tenta  fazer alguma coisa. Ex: conversão de string para float
#se não conseguir, ele cai no EXCEPT === manda fazer outra ação instead
#O TRY não funciona para avaliar numeros (<, >, etc). Para isso usar IF

while repetir == 's':
    produto = input('Digite o nome do produto: ')
    while valid_preço == False:
        preço = input('Digite o preço do produto: ')
        try: 
            preço = float(preço)
            
            if preço <= 0:
                continue
            else: 
                valid_preço = True    
                break
        
        except:
            print('Formato de preço inválido')
            continue


    fatura.append([produto, preço])
    total += preço
    valid_preço = False
    repetir = input('Deseja comprar mais algum produto?: ').lower()
    if repetir == 's' or repetir == 'sim': 
        valid_preço = False
        continue
       
    else: 
        break


for i in fatura:
    print(i[0], ':', i[1])

print('O total da fatura é: %d' % (total)) 