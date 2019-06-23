#Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete 
# feita a um grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"
# As possíveis respostas são:
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outros
# Opção: 

# Você foi contratado para desenvolver um programa que leia 
# o resultado da enquete e informe ao final o resultado da mesma.
#  O programa deverá ler os valores até ser informado o valor 0, 
# que encerra a entrada dos dados. Não deverão ser aceitos valores
#  além dos válidos para o programa (0 a 6). 
# Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
# Após os dados terem sido completamente informados, 
# o programa deverá calcular a percentual de cada um dos concorrentes
#  e informar o vencedor da enquete. 
# O formato da saída dos resultados deve seguir o exemplo:

# Sistema Operacional     Votos   %
# --------------------------     --------   ---
# Windows Server           1500   17%
# Unix                               3500   40%
# Linux                              3000   34%
# Netware                          500    5%
# Mac OS                           150    2%
# Outro                               150    2%
# ---------------------------     -------
# Total                                8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, 
# correspondendo a 40% dos votos.

print("Votação: 'Qual é o melhor sistema operacional para uso em servidores?'")
print('1- Windows Server')
print('2- Unix')
print('3- Linux')
print('4- Netware')
print('5- Mac OS')
print('6- Outros')
print('Opção:')

voto = 9
votos = []
while voto != 0:
    voto = input('Insira um número de 1 a 6, de acordo com sua preferência de sistema operacional: ')
    try:
        voto = int(voto)
        if 0 < voto < 6:
            voto = str(voto)
            votos.append(voto)
        elif voto < 0 or voto > 6:
            print('Insira um voto válido')
            continue
        elif voto == 0:
            print('Votação encerrada')
            break
        else:
            voto != 0
    except:
        print('Insira um voto válido')
        voto != 0


print(votos)
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
for i in votos:
    if i == '1':
        a += 1
    elif i == '2':
        b += 1
    elif i == '3':
        c += 1
    elif i == '4':
        d += 1
    elif i == '5':
        e += 1
    else:
        f += 1


dic = {'1': a, '2': b, '3': c, '4': d, '5': e, '6': f}
l = (dic.get('1'))
m = (dic.get('2'))
n = (dic.get('3'))
o = (dic.get('4'))
p = (dic.get('5'))
q = (dic.get('6'))

total = int(l + m + n + o + p + q)
print(total)

lista = [l, m, n, o, p, q]
porcentagem1 = ((l/total)*100)
porcentagem2 = ((m/total)*100)
porcentagem3 = ((n/total)*100)
porcentagem4 = ((o/total)*100)
porcentagem5 = ((p/total)*100)
porcentagem6 = ((q/total)*100)
# print(porcentagem2, '%')
# print(porcentagem3, '%')
# print(porcentagem4, '%')
# print(porcentagem5, '%')
# print(porcentagem6, '%')
# print(porcentagem1, '%')

print('Sistema operacional', 'Votos', '%')
print('Windows Server: %d - %.2f%% ' % (a, porcentagem1))
print('Unix: %d - %.2f%% ' % (b, porcentagem2))
print('Linux: %d - %.2f%% ' % (c, porcentagem3))
print('Netware:  %d - %.2f%% '  % (d, porcentagem4))
print('Mac Os: %d - %.2f%% ' % (e, porcentagem5))
print('Outros: %d - %.2f%% ' % (f, porcentagem6))
print('O total de votos foi: ', total)
sistemas = [a, b, c, d, e, e, f]
vencedor = int(max(sistemas))
#print(vencedor)
porcentagem_win = (float(((vencedor/total)*100)))
if a == vencedor:
    sistema_vencedor = 'Windows Server'
elif b == vencedor:
    sistema_vencedor = 'Unix'
elif c == vencedor:
    sistema_vencedor = 'Linux'
elif d == vencedor:
    sistema_vencedor = 'Netware'
elif e == vencedor:
    sistema_vencedor = 'Mac Os'
else: 
    sistema_vencedor = 'Outro'

# print('O sistema mais votado foi o %s' % (sistema_vencedor))
# print('Com %d votos' % (vencedor))
# #print("Correspondendo a %.2f '%' dos votos" % porcentagem_win)
# print("Correspondendo a ", porcentagem_win, "%", "dos votos")


#Como faz para juntar tudo na última frase? 
#Como limitar as unidades depois da vírgula nas porcentagens?

print('O sistemma mais votado foi o %s, com %d votos, correspondendo a %.2f%% dos votos' % (sistema_vencedor, vencedor, porcentagem_win)) 



#Solução Rober:
# sistemas = {
#    '1': {
#        'name': "1- Windows Server",
#        'votes': 0,
#        'percent': 0.0,
#    },
#    '2': {
#        'name': "2- Unix",
#        'votes': 0,
#        'percent': 0.0,
#    },
#    '3': {
#        'name': "3- Linux",
#        'votes': 0,
#        'percent': 0.0,
#    },
#    '4': {
#        'name': "4- Netware",
#        'votes': 0,
#        'percent': 0.0,
#    },
#    '5': {
#        'name': "5- Mac OS",
#        'votes': 0,
#        'percent': 0.0,
#    },
#    '6': {
#        'name': "6- Outros",
#        'votes': 0,
#        'percent': 0.0,
#    },
# }

# print("Qual o melhor Sistema Operacional para uso em servidores? (insira zero (0) para encerrar a votacao).")
# for i in sistemas:
#    print(sistemas.get(i).get('name'))

# total_votes = 0
# opcao = -1
# while opcao != 0:
#    opcao = input('Opção: ')
#    if opcao in sistemas:
#        sistemas[opcao]['votes'] += 1
#        total_votes += 1
#    elif opcao == '0':
#        break
#    else:
#        print("opção inválida.")
#        opcao = -1
  
# for i in sistemas:
#    sistemas[i]['percent'] = sistemas[i]['votes'] * 100.0 / total_votes

# # Daqui em diante exibir os resultados formatados
# print("Resultado: ")
# for i in sistemas:
#    print(sistemas.get(i))

