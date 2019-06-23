Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> nome = 'Werner'
>>> sobrenome_mae = 'Heckler'
>>> sobrenome_pai = 'Weingartner'
>>> nome_completo = nome + ' ' + sobrenome_mae + ' ' + sobrenome_pai
>>> nome_completo
'Werner Heckler Weingartner'
>>> nome * 3
'WernerWernerWerner'
>>> len (nome_completo)
26
>>> len (nome)
6
>>> nome |0|
SyntaxError: invalid syntax
>>> nome {0}
SyntaxError: invalid syntax
>>> nome [0]
'W'
>>> nome [4]
'e'
>>> nome [-1]
'r'
>>> nome [-4]
'r'
>>> nome[-5]
'e'
>>> nome [-6]
'W'
>>> nome[0:7]
'Werner'
>>> nome[0:3]
'Wer'
>>> nome[-5:]
'erner'
>>> nome[:3]
'Wer'
>>> palavra = 'paralelepipedo'
>>> palavra[4:8]
'lele'
>>> palavra[-1:-5]
''
>>> palavra[-5]
'i'
>>> palavra[-1]
'o'
>>> palavra[:-4:-1]
'ode'
>>> palavra[-4:-1]
'ped'
>>> palavra[-4:0]
''
>>> palavra[-5]
'i'
>>> palavra[1:6]
'arale'
>>> nome = 'Werner'
>>> sobrenome_mae = 'Heckler'
>>> sobrenome_pai = 'Weingartner'
>>> iniciais = nome[1] + sobrenome_mae[1] + sobrenome_pai[1]
>>> iniciais
'eee'
>>> iniciais = nome[0] + sobrenome_mae[0] + sobrenome_pai[0]
>>> iniciais
'WHW'
>>> empresa = 'MR_Serviços_Médicos'
>>> nome = 'Werner'
>>> sobrenome_pai = 'Weingartner'
>>> email = nome + '.' + sobrenome_pai + '@' + nome[0] + sobrenome_pai + empresa + '.' + 'com'
>>> email
'Werner.Weingartner@WWeingartnerMR_Serviços_Médicos.com'
>>> empresa = 'mr_serviços_médicos
SyntaxError: EOL while scanning string literal
>>> empresa = 'mr_serviços_médicos'
>>> nome = 'werner'
>>> sobrenome_pai = 'weingartner'
>>> email = nome + '.' + sobrenome_pai + '@' + nome[0] + sobrenome_pai + empresa + '.' + 'com'
>>> email
'werner.weingartner@wweingartnermr_serviços_médicos.com'
>>> 
