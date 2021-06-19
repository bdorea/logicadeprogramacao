frase = input('Digite uma frase:')
tam = len(frase)

#Para pegar a primeira metade da frase,funciona dessa maneira
frase2 = frase[:int(tam/2)]
#Adicionando o [-2:] tira dois caracteres do inicio da frase e então imprime so os 2 ultimos caracters da frase.
print(frase2[-2:])
