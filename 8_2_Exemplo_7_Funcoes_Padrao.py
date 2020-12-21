print('\nCurso Ciência de Dados - Fundamentos em Python (Funções)\nfernandoluismc@gmail.com\n')
print('Parte 1: Funções Nativas do Pyhton, como abs()Absoluto,\n')
print('Parte 2:Função Com Valor de Retorno\n')
print('Parte 3:Função Com Parâmetros de Intervalo, ou mais de um parâmetro\n')

#---------------------------------
#----- Parte 1 -------------------
print('----------------------------------------------\n---------- Parte 1----------------------------')

print('\n',abs(-200))

from statistics import*
x =[10,20,30]
print('\nMédia: ',mean(x))
print('\nDesvio Padrão: ',stdev(x))

#---------------------------------
#----- Parte 2 -------------------
print('----------------------------------------------\n---------- Parte 2----------------------------')

from numpy import*
a = random.random((8,8)) # Gera uma matriz (Lista com listas dentro) de números aleatórios
print(type(a))
print(a)