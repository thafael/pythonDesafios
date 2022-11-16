salario = float(input('Digite o salário: '))
aumento = (salario / 100) * 15
print('Seu antigo R${:.2f} \ne seu novo salário R${:.2f} já com aumento de 15%'.format(salario, salario + aumento))