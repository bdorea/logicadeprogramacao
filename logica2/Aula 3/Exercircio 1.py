A = int(input('Digite o 1º lado do triangulo: '))
B = int(input('Digite o 2º lado do triangulo: '))
C = int(input('Digite o 3º lado do triangulo: '))

if (A > 0) and (B > 0) and (C > 0):
    if (A + B > C) and (A + C > B) and (B + C > A):
    #Se você chegou até aqui, é porque o triangulo é valido
        if (A != B) and (A != C) and (B != C):
            print('Triangulo Escaleno')
        else:
            if (A == B) and (A == C) and (B == C):
                print('Triangulo Equilatero')
            else:
                print('Triangulo Isosceles')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo')