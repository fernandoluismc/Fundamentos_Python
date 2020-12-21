print('\nCurso Ciência de Dados - Fundamentos em Python (Estruturas de Decisão)\nfernandoluismc@gmail.com\n')
print('Parte 1: Utilização do if, elif e else\n')
print('Parte 2:\n')



#---------------------------------
#----- Parte 1 -------------------
print('----------------------------------------------\n---------- Parte 1----------------------------')

nota_corte_input = float(input('Digite a Nota de corte: '))
desvio = float(input('Digite o desvio aceitável para nota de corte (exemplo0.2 = 20%): '))
nota_input=float(input('Digite a Nota do Aluno: '))

if nota_input >=nota_corte_input:
    print('Aprovado!')
elif nota_input >(nota_corte_input-(desvio*nota_corte_input)) and nota_input<=nota_corte_input:
    print('Substitutiva, vai estudar!')
else:
    print('Reprovado!')