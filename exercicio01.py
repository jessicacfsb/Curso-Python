velocidade = int(input('Digite a velocidade: '))
if velocidade >= 110:
    print ('Você foi multado!')
    multa = (velocidade-110) * 5
    print (f'Multa R${multa:.2f}')
else:
    print('Siga em frente!')
