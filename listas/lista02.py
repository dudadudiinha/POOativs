'''for num in range(1, 11):
    print(num, end=' ')
print()

for nume in range(10, 0, -1):
    print(nume, end=' ')
print()

for numb in range(1, 11):
    if numb%2==0:
        print(f'-{numb}', end=' ')
    else:
        print(numb, end=' ')
print()

for number in range(1, 31):
    if number%3==0:
        print(f'-{number}', end=' ')
    else:
        print(number, end=' ')
print()

soma_tres = 0
three = []
for numero in range(1, 31):
    print(numero, end=' ')
    three.append(numero)
    if len(three) == 3:
        soma_tres = sum(three)
        print(soma_tres, end=' ')
        three = []

frase = input('Digite uma frase:\n')
palavras = frase.split()
indice = 0
while indice < len(palavras):
    new_frase = ''
    for i in range(indice, len(palavras)):
        new_frase += palavras[i] + ' '
    print(new_frase)
    indice += 1

phrase = input('Digite uma frase:\n').split()
for letra in phrase:
    print(letra[-1], end='')
print()    

palaavra = input('Digite uma frase:\n')
for i in range(1, len(palaavra)+1):
    print(f'{i} - {palaavra}')

stringg = input('Digite uma frase:\n')
soma_nums = 0
for caractere in stringg:
    if caractere.isdigit():
        soma_nums+=int(caractere)
print(soma_nums)

frasee = input('Digite uma frase:\n').split()
print(len(frasee))

prase = input('Digite uma sequência de números separados por vírgula:\n')
prasee = list(map(int, prase.split(',')))
print(f'Soma = {sum(prasee)}')

entrada = input('Digite dez valores inteiros\n')
entradaa = list(map(int, entrada.split()))
print(f'O maior valor é {max(entradaa)} e o menor é {min(entradaa)}')

inp = input('Digite três números inteiros separados por espaços\n')
inpu = list(map(int, inp.split()))
somap = 0
for numeroo in inpu:
    if numeroo%2==0:
        somap += numeroo
print(f'Soma dos pares: {somap}')

class Circulo:
    def __init__(self):
        self.raio = 0
    def area(self):
        return 3.14*(self.raio**2)
    def perimetro(self):
        return 2*3.14*self.raio
circle = Circulo()
circle.raio = int(input('Digite o raio do círculo: '))
print(f'Area = {circle.area():.2f}\nCircunferência = {circle.perimetro():.2f}')

class Viagem:
    def __init__(self):
        self.distancia = 0
        self.horas = 1
        self.minutos = 30
    def vel_media(self):
        tempo = self.horas + self.minutos / 60
        return self.distancia/tempo
viagem = Viagem()
viagem.distancia = int(input('Digite a distância em km: '))
viagem.horas = int(input('Digite a hora: '))
viagem.minutos = int(input('Digite os minutos: '))
print(f'{viagem.vel_media():.0f}km/h')

class Conta:
    def __init__(self):
        self.nome = ''
        self.num = 0
        self.saldo = 0
    def deposito(self):
        valor = int(input('Quanto você deseja depositar? '))
        self.saldo = self.saldo + valor
        print(f'Seu saldo atual é R${self.saldo}')
    def saque(self):
        valor = int(input('Quanto você deseja sacar? '))
        if self.saldo > 0 and valor <= self.saldo: print(f'Seu saldo atual é R${self.saldo - valor}')
        else: print('Seu saldo não é suficiente para sacar essa quantia de dinheiro')
cb = Conta()
cb.nome = input('Digite seu nome: ')
cb.num = int(input('Digite o número da sua conta bancária: '))
cb.saldo = int(input('Digite o seu saldo: R$'))
print(f'Olá, {cb.nome}, N° {cb.num}!\nSeu saldo atual é R${cb.saldo}.')
cb.deposito()
cb.saque()

entrada = input('Frse: ')
print(entrada[::-1])

notas = list(map(int, input().split()))
media = sum(notas)/len(notas)
print(f'Média = {media:.2f}\nNúmeros menores que a média:')
for nota in notas:
    if nota < media:
        print(nota)
print('Números maiores que a média ou iguais a ela:')
for nota in notas:
    if nota >= media:
        print(nota)

for num in range(1, 11):
    print(f'\nTabuada de {num}')
    for mult in range(1, 11):
        print(f'{num} x {mult} = {num*mult}')

num = 1
while num <= 10:
    print(f'\nTabuada de {num}')
    for numero in range(1, 10):
        print(f'{num} x {mult} = {num*mult}')
        num += 1'''