#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm' (M=masculino, F=feminino);
#Estado Civil: 's', 'c', 'v', 'd' (S=solteiro, C=casado, V=viúvo, D=divorciado).
	#Ao final, exiba todas as informaçẽos do usuário, devidamente formatadas como no exemplo abaixo:
		#Nome: Rober Guerra
		#Idade: 26 anos
		#Salário: R$ 1.000,00
		#Sexo: Masculino
		#Estado Civil: Solteiro

        #Como fazer a variavel mauiscula?

print('Perfil pessoal: ')

nome = ''
while (len(nome) < 3):
    nome = input('Insira seu nome: ')
    if len(nome) < 3:
        print('Informe um nome com mais de 3 caracteres.')

idade = ''
while not idade.isdigit():
    idade = input('Insira sua idade: ')
    if idade.isdigit() and (0 <= int(idade) <= 150):
        idade = int(idade)
        break
    else:  
        print('Inválido')

salario = ''
while not salario.isdigit():
    salario = input('Insira seu salário: ')
    if salario.isdigit() and (float(salario) > 0.0):  
        salario = float(salario)
        break
    else: 
        print('Inválido')
     

sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = input("Informe seu sexo, 'f' para feminino e 'm' para masculino: ")
    sexo = sexo.upper()
    if sexo != 'F' and sexo != 'M':
        print('Inválido')

if sexo == 'F':
    sexo = 'Feminino'

elif sexo == 'M':
    sexo = 'Masculino'    


estado_civil = ''
tipos_estado_civil = ['c', 's', 'v', 'd'] #array ou lista
while estado_civil not in tipos_estado_civil:
    estado_civil = input('Informe seu estado civil, s para solteiro; c para casado; v para viuvo e d para divorciado: ')
    estado_civil = estado_civil.lower()
    if estado_civil not in tipos_estado_civil:
        print('Inválido')
    

# estado_civil = ''
# #tipos_estado_civil = ['c', 's', 'v', 'd'] # Array ou Lista

# # Declaracao de um dicionario de dados
# # 'chave' : 'valor'
# tipos_estado_civil = {
#    'c': 'Casado',
#    's': 'Solteiro',
#    'v': 'Viuvo',
#    'd': 'Divorciado',
# }
# nome_estado_civil = ''

# while estado_civil not in tipos_estado_civil:
#    estado_civil = input("Informe o estado civil (c: casado, s: solteiro, v: viuvo, d: divorciado): ")
#    estado_civil = estado_civil.lower()
  
#    if estado_civil not in tipos_estado_civil:
#        print("Estado civil invalido.")
#    else:
#        # Acessando a chave estado_civil de dentro do Dicionario tipos_estado_civil
#        nome_estado_civil = tipos_estado_civil[estado_civil]

# print("Estado civil: %s" % (nome_estado_civil))    

if estado_civil == 'c':
    estado_civil = 'Casado'

elif estado_civil == 's':
    estado_civil = 'Solteiro'

elif estado_civil == 'v':
    estado_civil = 'Viúvo' 

elif estado_civil == 'd':
    estado_civil = 'Divorciado'       



print('Nome: %s' % (nome))
print('Idade: %d anos' % (idade) )
print('Salário: R$ %.2f' % (salario))
print('Sexo: %s' % (sexo))
print('Estado Civil: %s' % (estado_civil))



