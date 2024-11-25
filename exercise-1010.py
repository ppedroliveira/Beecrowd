codpeca1, numPeca1, valPeca1 = [float(x) for x in input().split(" ")]
codPeca2, numPeca2, valPeca2 = [float(x) for x in input().split(" ")]
resultado = ((numPeca1*valPeca1)+(numPeca2*valPeca2))
print('VALOR A PAGAR: R$', '{:.2f}'.format(resultado))