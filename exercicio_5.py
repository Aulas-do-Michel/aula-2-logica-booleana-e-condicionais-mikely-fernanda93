"""
### Exercício 5 - Analisador de Variantes Genéticas.

Você está analisando uma variante genética e precisa saber se ela é relevante para análise ou não.

Obs: Esse exercício é uma simplificação!

Você vai receber 5 parametros:

1) Frequência Populacional: Frequencia da variante na população em porcentagem. Será um float de 0 a 100.
2) Gene: Gene da variante. Será um texto. Exemplo: "BRCA1", "BOLA1", "HFE", etc.
3) Impacto: Se ela está numa posição de impacto ALTO ou BAIXO. Será um texto, necessariamente ou "ALTO" ou "BAIXO".
4) Reads: Quantidade de reads da variante. Será um número inteiro.
5) Vaf: Frequencia alélica da variante. Será um float de 0 a 100.

A primeira coisa é tomar cuidado com a qualidade da leitura. 

Se a variante tiver menos de 10 reads OU uma frequência alélica abaixo de 20% a gente vai dizer que ela não é relevante, pois deve ser um artefato.

Se ela não for um artefato temos que avaliar as seguintes coisas:

1) Ela só vai ser relevante se o impacto for ALTO.

2) Ela não vai ser relevante se a frequência dela for maior que 5%, a não ser que esteja nos seguintes genes de exceção: "HFE", "MEFV" ou "GJB2".

Obs: Uma resolução desse exercício está no Colab da Aula 02. Tente primeiro fazer sozinho! 
Se não passar nos testes, qualquer coisa consulte lá depois para ver o que você poderia ter feito diferente.

Exemplos:

Digite a frequencia populacional (em porcentagem): 1

Digite o gene: BRCA2

Digite a Impacto (ALTO ou BAIXO): ALTO

Digite os reads: 1000

Digite a frequencia alélica (em porcentagem): 50

Resposta: É relevante.

-------

Digite a frequencia populacional (em porcentagem): 50

Digite o gene: HFE

Digite a Impacto (ALTO ou BAIXO): ALTO

Digite os reads: 1000

Digite a frequencia alélica (em porcentagem): 50

Resposta: É relevante.

------

Digite a frequencia populacional (em porcentagem): 10

Digite o gene: BRCA1

Digite a Impacto (ALTO ou BAIXO): Baixo

Digite os reads: 1000

Digite a frequencia alélica (em porcentagem): 50

Resposta: Não é relevante.

------

Digite a frequencia populacional (em porcentagem): 0

Digite o gene: HFE

Digite a Impacto (ALTO ou BAIXO): ALTO

Digite os reads: 1

Digite a frequencia alélica (em porcentagem): 100

Resposta: Não é relevante.
"""

"""
### Exercício 5 - Analisador de Variantes Genéticas.

Você está analisando uma variante genética e precisa saber se ela é relevante para análise ou não.
Obs: Esse exercício é uma simplificação!

Você vai receber 5 parametros:

1) Frequência Populacional: Frequencia da variante na população em porcentagem. Será um float de 0 a 100.
2) Gene: Gene da variante. Será um texto. Exemplo: "BRCA1", "BOLA1", "HFE", etc.
3) Impacto: Se ela está numa posição de impacto ALTO ou BAIXO. Será um texto, necessariamente ou "ALTO" ou 
"BAIXO".
4) Reads: Quantidade de reads da variante. Será um número inteiro.
5) Vaf: Frequencia alélica da variante. Será um float de 0 a 100.

A primeira coisa é tomar cuidado com a qualidade da leitura. 

Se a variante tiver menos de 10 reads OU uma frequência alélica abaixo de 20% a gente vai dizer que ela 
não é relevante, pois deve ser um artefato.

Se ela não for um artefato temos que avaliar as seguintes coisas:

1) Ela só vai ser relevante se o impacto for ALTO.

2) Ela não vai ser relevante se a frequência dela for maior que 5%, a não ser que esteja nos seguintes 
genes de exceção: "HFE", "MEFV" ou "GJB2".
"""

frequencia_pop = float(input("Digite a Frequencia Populacional em porcentagem (entre 0 e 100): "))
gene = input("Digite o Gene. ")
impacto = input("Digite o impacto => ALTO ou BAIXO. ")
reads = int(input("Digite quantos Reads a variante tem (inteiros). "))
vaf = float(input("Digite Frequência Alélica da variante em porcentagem (entre 0 e 100). "))

frequencia_pop = frequencia_pop / 100
vaf = vaf / 100

print('\n')
#print(f'impacto: {impacto}')

if reads < 10 or vaf < 0.20:
    print("Não é relevante, pois deve ser um artefato.")
else: 
    if impacto == 'ALTO':
        if (frequencia_pop > 0.05) and ((gene == "HFE") or (gene == "MEFV") or (gene == "GJB2")):
            print('Esta variante É Relevante!')
        elif frequencia_pop <= 0.05:
            print('Esta variante É relevante!')
        elif frequencia_pop > 0.05:
            print('Esta variante NÃO É relevante!')
    else:
        print('Esta variante NÃO É relevante!')
            
        
        
        
