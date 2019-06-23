#Faça um Programa que leia um vetor de 10 caracteres, 
# e diga quantas consoantes foram lidas. Imprima as consoantes.

word = ''
num = False
while num == False:
    num = input('Insira quantos caracteres você quer inserir: ')
    try: 
        num = int(num)
        if num > 0:
            num == True
            break
        else: 
            num = False
    except: 
        num = False

while len(word) != num:
    word = input('Insira uma palavra com o número de caracteres determinado: ')
    try:
        word = str(word)
        if len(word) == num:
            break
        else: 
            continue
    except:
        continue

#print(num, word)

vogais = ['a', 'e', 'i', 'o', 'u']
word = list(word)
#print(word)


for i in word:
    if i == 'a':
        word.remove('a')
        
    else: 
        continue
    if i == 'e':
        word.remove('e')
        
    else:
        continue
    if i == 'i':
        word.remove('i')
        
    else:
        continue
    if i == 'o':
        word.remove('o')
        
    else:
        continue
    if i == 'u':
        word.remove('u')
        
    else:
        continue
    
# for i ib list_word:
#    if i in 'aeiou':
#         list_word.remove(i)
#ELIMINA A NECESSIDADE DE MUITOS IFs
    
cons = len(word)
#print(word)
print('Número de consoantes lidas: %i' % (cons))
    

print('Consoantes: %s' % (word))

    
