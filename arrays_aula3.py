#crescimento EUA X China

pib_eua = 21.5
cresc_eua = 0.029

pib_china = 13.4
cresc_china = 0.065

pib_eua = pib_eua*1.029
pib_china = pib_china*1.065

i = 0
while pib_china <= pib_eua:
    i += 1
    pib_eua = pib_eua*1.029
    pib_china = pib_china*1.065


# print(i)
# print(pib_china)
# print(pib_eua)

print('Em %d anos, o PIB da China vai ultrapassar o PIB dos EUA' %(i))
print('Quando isso ocorrer, o PIB chinês será de US$ %.2f trilhões, enquanto que o americano será de US$ %.2f trilhões' %(pib_china, pib_eua))
