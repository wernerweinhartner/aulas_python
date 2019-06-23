#Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
#  Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
# A entrada é dada em dois inteiros. 
# Deve haver pelo menos duas funções: uma para fazer a conversão e
#  uma para a saída. Registre a informação A.M./P.M. 
# como um valor ‘A’ para A.M. e ‘P’ para P.M. 
# Assim, a função para efetuar as conversões
#  terá um parâmetro formal para registrar se é A.M. ou P.M.
#  Inclua um loop que permita que o usuário 
# repita esse cálculo para novos valores de entrada todas as vezes que desejar. 
def conversao(hora):
    hora = False
    tipo = ''
    while hora == False:
        hora = input('Insira um horário no formato 24 horas: ')
        try: 
            a, b = hora.split(':')
            a = int(a)
            b = int(b)
            if 12 < a < 24:
                a = a - 12
                a = str(a)
                tipo = 'P.M.'
                
            elif a == 12:
                a = 12
                a = str(a)
                tipo = 'P.M.'
                
            elif 0 <= a < 12:
                a = str(a)
                tipo = 'A.M.'
            
            elif a >= 24 or a < 0 or b < 0 or b > 59:
                print('Inválido')
                hora = False
        except:
            print('Inválido')
            hora = False 
    if 0 <= b < 10:
        b = '0' + str(b)
    b = str(b) 
    #hora = '%.2d' % (m)
    #resulta em: 02
    horário = a + ':' + b + ' ' + tipo
    hora = True
    return(horário)

hora = ''
ask = 'sim'
while ask != 'nao' and ask != 'n':
    print(conversao(hora))
    ask = input('Gostaria de repetir a operaçao?: ')
    if ask == 'nao' or ask == 'n':
        print('Obrigado por utilizar o programa')
    else: 
        ask = 'sim'


    






# hora = ''
# def conversão(hora):
#     hora = False
#     tipo = ''
#     while hora == False:
#         hora = input('Insira um horário no formato 24 horas: ')
#         try: 
#             a, b = hora.split(':')
#             a = int(a)
#             b = int(b)
#             if 12 < a < 24:
#                 a = a - 12
#                 a = str(a)
#                 tipo = 'P.M.'
                
#             elif a == 12:
#                 a = 12
#                 a = str(a)
#                 tipo = 'P.M.'
                
#             elif 0 <= a < 12:
#                 a = str(a)
#                 tipo = 'A.M.'
            
#             elif a >= 24 or a < 0 or b < 0 or b > 59:
#                 print('Inválido')
#                 hora = False
#         except:
#             print('Inválido')
#             hora = False 
#     if 0 <= b < 10:
#         b = '0' + str(b)
#     b = str(b) 
#     horário = a + ':' + b + ' ' + tipo
#     hora = True
#     return(horário)
    
    
# print(conversão(hora))