preco = float(input('Digite o preço para ver com desconto: '))
desconto = (preco / 100) * 5

print('De R${:.2f} por R${:.2f} com mega desconto de 5%'.format(preco, preco - desconto  ))