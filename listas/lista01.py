#1
a = int(input('Digite dois valores inteiros\n'))
b = int(input())
if a == b:
    print('Números iguais')
else:
    print(f'Maior = {max(a,b)}')

#2
num1 = int(input('Digite quatro valores inteiros\n'))
num2 = int(input())
num3 = int(input())
num4 = int(input())
media = (num1+num2+num3+num4)//4
notas = [num1, num2, num3, num4]
maiores = []
menores = []
for nota in notas:
    if nota < media:
        menores.append(nota)
    else:
        maiores.append(nota)
print(f'Média = {media}\nNúmeros menores que a média:')
for menor in menores:
    print(menor)
print('Números maiores ou iguais à média:')
for maior in maiores:
    print(maior)

#3
n1 = int(input('Digite quatro valores inteiros\n'))
n2 = int(input())
n3 = int(input())
n4 = int(input())
numeros = [n1,n2,n3,n4]
somap = 0
somai = 0
for numero in numeros:
    if numero%2==0:
        somap+=numero
    else:
        somai+=numero
print(f'Soma dos pares = {somap}\nSoma dos ímpares = {somai}')

#4

#5
num_mes = int(input('Informe o número do mês'))
meses = {
    1: ('janeiro', 'primeiro'),
    2: ('fevereiro', 'primeiro'),
    3: ('março', 'primeiro'),
    4: ('abril', 'segundo'),
    5: ('maio', 'segundo'),
    6: ('junho', 'segundo'),
    7: ('julho', 'terceiro'),
    8: ('agosto', 'terceiro'),
    9: ('setembro', 'terceiro'),
    10: ('outubro', 'quarto'),
    11: ('novembro', 'quarto'),
    12: ('dezembro', 'quarto')
}
if num_mes >=1 and num_mes <= 12:
    mes, trimestre = meses[num_mes]
    print(f'O mês de {mes} é do {trimestre} trimestre do ano')
else:
    print('Digite um número válido, ou seja, entre 1 e 12')

#6
nume1 = int(input('Digite três valores inteiros\n'))
nume2 = int(input())
nume3 = int(input())
pequeno = min(nume1, nume2, nume3)
grande = max(nume1, nume2, nume3)
print(f'A soma do maior com o menor número é {pequeno+grande}.')

#7
a = int(input('Digite os coeficientes a, b, e c de uma equação do 2° grau\n'))
b = int(input())
c = int(input())
delta = b**2-4*a*c
if a == 0:
    print('Não é uma função de segundo grau')
elif delta < 0:
    print('Impossível calcular')
else:
    print(f'As raízes são {(-b+delta**(1/2))/(2*a):.2f} e {(-b-delta**(1/2))/(2*a):.2f}')

#8
numero1 = int(input('Digite quatro valores inteiros distintos\n'))
numero2 = int(input())
numero3 = int(input())
numero4 = int(input())
numeros = [numero1, numero2, numero3, numero4]
if len(set(numeros)) != 4:
    print('Digite quatro números diferentes')
else:
    numeros.sort()
    print(f'Maior valor = {numeros[3]}\nMenor valor = {numeros[0]}\nA soma do segundo maior valor com o segundo menor = {numeros[1]+numeros[2]}')

#9

#10

#11

#12

#13
numbers = list(map(int, input('Digite dez valores inteiros\n').split()))
while len(numbers) != 10:
    numbers = list(map(int, input('Digite dez valores inteiros\n').split()))
numbers.sort()
print(f'O maior valor é {numbers[9]} e o menor é {numbers[0]}')

#14
a1 = int(input('Digite três valores inteiros\n'))
b1 = int(input())
c1 = int(input())
if a1 + b1 > c1 and a1 + c1 > b1 and b1 + c1 > a1:
    if a1 == b1 == c1:
        print('Este é um triângulo equilátero')
    if a1 == b1 or a1 == c1 or b1 == c1:
        print('Este é um triângulo isósceles')
    else:
        print('Este é um triângulo escaleno')
else:
    print('Esses valores não formam um triângulo')

#15
v1 = int(input('Digite três valores\n'))
v2 = int(input())
v3 = int(input())
valores = [v1, v2, v3]
valores.sort()
print(*valores)