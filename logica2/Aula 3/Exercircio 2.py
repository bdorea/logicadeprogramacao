print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('/ Divisão')
print('* Multiplicação')
print('PRESSIONE OUTRA TECLA PARA SAIR')

op = input('Qual operação deseja fazer? ')
if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))

if (op == '+'):
    res = x + y
    print('Resultado: {} + {} = {}'. format(x , y, res))

elif (op == '-'):
    res = x - y
    print('Resultado: {} - {} = {}'.format(x, y, res))

elif (op == '/'):
    res = x / y
    print('Resultado: {} / {} = {}'.format(x, y, res))

elif (op == '*'):
    res = x * y
    print('Resultado: {} * {} = {}'.format(x, y, res))

else:
    print('Operação Inválida')
print('Encerrando o programa...')