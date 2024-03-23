"""
#### Exercício 1

Receba um número inteiro de um usuário. Se ele for par, imprima "Par". Se não, imprima "Ímpar".

Exemplo:

Digite um número:
10

Par
--------
Digite um número:
1

Ímpar

Dica: Lembre do comando de resto da divisão inteira!
"""

"""
Exercício 1 => 
Receba um número inteiro de um usuário. 
Se ele for par, imprima "Par". Se não, imprima "Ímpar".
"""

numero = int(input('Digite um número inteiro: '))
par = numero % 2

if par == 0:
    print('Par')
else:
    print('Ímpar')
