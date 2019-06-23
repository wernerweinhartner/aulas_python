#Faça um programa que leia um nome de usuário e a sua senha e
#não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = ''
senha = ''

while (usuario == senha): 
    usuario = input('Informe seu nome de usuário: ')
    senha = input('Informe sua senha: ')
    if usuario == senha:
        print('O nome de usuario e senha devem ser difirentes')
        


print ('Nome de usuario e senha validos')    



