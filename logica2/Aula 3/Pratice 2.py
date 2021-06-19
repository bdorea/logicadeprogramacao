if (idade > 60):
    print('Você te direito aos beneficios')

#Se o dano é maior do que 10 e escudo é igual a 0, escreva 'Você está morto!'

if (dano > 10 and escudo == 0):
    print('Você esta morto!')

#Se pelo menos uma das variaves booleanas norte, sul, leste e oeste resultarem em True, escreva: você escapou!
if (norte or sul or leste or oeste):
    print('Você escapou!')

# Se ano é divisivel por 4 escreva "Ano bissexto". Caso contrario escreva "Ano não bissexto"
if ( ano % 4 == 0):
    print ('Ano Bissexto')
else:
    print('Ano não bissexto')

#Se ambas as variaveis booleanas cima e baixo forem true, escreva "DECIDA-SE", caso contrario escreva "Você escolheu
#um caminho"

if (cima and baixo == True):
    print('DECIDA-SE')
else:
    print('Você escolheu um caminho!')