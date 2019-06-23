arq = open('arquivos/lista_ips.txt', 'r')
texto = arq.readlines()
arq.close()
inv = []
val = []
for linha in texto:
    #192.168.0.256
    lista = linha.split('.')
    
    if len(lista) == 4:
        teste = True
        for i in lista:
            digito = i.strip()
            if digito.isdigit():
                digito = int(digito)
                if 0 <= digito <= 255:
                    #val.append(linha)
                    teste = True
                else:
                    #inv.append(linha)
                    teste = False
                    break
            else:
                #inv.append(linha)
                teste = False
                break
        if teste:
            val.append(linha)
        else:
            inv.append(linha)
        
    else:
        inv.append(linha)

print('Inválidos')
print(inv)
print('Válidos')
print(val)


novo_arq = open('ips_validos.txt', 'w')
novo_arq.write("Enderecos validos: \n")
novo_arq.writelines(val)
novo_arq.write('\n')
novo_arq.write('Enderecos invalidos: \n')
novo_arq.writelines(inv)
novo_arq.close()

# invalidos = open('ips_invalidos.txt', 'w')
# invalidos.writelines(inv)
# invalidos.close()