nome = str(input())
salario = float(input())
valorVendas = float(input())
total = (salario+(valorVendas*0.15))
print('TOTAL = R$', '{:.2f}'.format(total))