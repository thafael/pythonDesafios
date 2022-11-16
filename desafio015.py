dias = int(input('Digite a quatidades total de em dias alugados: '))
km = float(input('Digite a quatidades total percorridos em Km: '))
print(f'{km}Km e {dias} dias, o preço é {(dias * 60) + (km * 0.15):.2f}')