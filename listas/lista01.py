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