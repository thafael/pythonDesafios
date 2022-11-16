'''
Celsius e Fahrenheit
Utilizamos a fórmula TC/5 = (TF – 32)/9, em que TC é temperatura em graus Celsius e TF é temperatura em Fahrenheit.

Converter 40° C em F:

40/5 = (TF – 32)/9
40 x 9 = 5(TF – 32)
360 = 5TF – 160
5TF = 520
TF = 104
'''

tc = float(input('Informe a temperatura em °C:'))
tf = ((9 * tc) / 5) + 32
print(f'A temperatura de {tc}°C corresponde a {tf}°F!')
