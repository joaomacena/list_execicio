print(f'''
# 6. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após
# isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que
# mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
''')


meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho', 'Agosto',
'Setembro','Outubro', 'Novembro','Dezembro']
temperatura = []
for temp in range(len(meses)):
    temperatura.append(float(input(f'Digite a temperatura do mês de {meses[temp]}')))
media = sum(temperatura ) / len(temperatura)
print(f'A média do ano {media}')
for i in range(len(temperatura)):
    if temperatura[i] > media:
        print(str( i + 1) + '-' + meses[i] )
