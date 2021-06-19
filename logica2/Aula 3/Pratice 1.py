#Letra A
#O somatório de 2 e 2 é menor que 4
print(2 + 2 < 4)

#letra B
#o valor 7//3 é igual a 1+1
print(7 // 3 == 1 + 1)

#Letra C
#A soma de 3 elevado ao quadrado com 4 levado ao quadrado é igual a 25
print(3**2 + 4**2 == 25)

#Letra D
#A soma de 2, 4 e 6 é maior do que 12
print(2+ 4 + 6 > 12)

#Letra E
#1387 é divisivel or 19
print(1387 % 19 == 0)

#Letra F
#31 é par
numero = int(input('Digite um número inteiro:'))

if (numero%2) == 0:
    print('Par')
else:
    print('Impar')

#Letra G
#O menor valor entre: 34, 29 e 31 é menor do que 30.

primeiro = int(input('Primeiro numero:'))
segundo = int(input('Segundo numero:'))
terceiro = int(input('Terceiro numero: '))

#maior numero
maior = primeiro
if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro
print('Maior: ', maior)

#menor numero
menor = primeiro

if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro
print('Menor: ', menor)
print( menor < 30 )