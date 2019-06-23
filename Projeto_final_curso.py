# Equação de segundo grau:
eq = False
while eq == False:
    eq = input('Insira os valores de a, b e c de uma equação de segundo grau (a*x**2 + b*x + c): ')
    try:
        a, b, c = eq.split(',')
        a = float(a)
        b = float(b)
        c = float(c)
        eq == True
    except:
        print('Números inválidos')
        eq = False
        
def function(a, b, c):
    bhaskara = float((b**2 -4*a*c)**(1/2))
    solution1 = float((((-b) + bhaskara))/(2*a))
    solution2 = float(((-b) - bhaskara)/(2*a))
    print('As soluções, se existirem, da equação de segundo grau são: %.2f e %.2f' % (solution1, solution2))

function(a, b, c)
